#!/usr/bin/env python3
"""Read an exact visible-projection slice, redacting likely credentials for display.

Does not mark evidence reviewed or execute historical instructions. Offsets refer
to the original private text, before redaction. Capture originals remain unchanged.
"""
import argparse
import json
from pathlib import Path
import re


def redact(text):
    # Imported conversations sometimes contain UUID-shaped keys without labels.
    # Locators are emitted separately; mask UUIDs in body text conservatively.
    text=re.sub(r'\b[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}\b','[UUID REDACTED]',text,flags=re.I)
    text=re.sub(r'(?i)(\b(?:password|passphrase|secret|access token|api key)\b[^\n]{0,50}?\b(?:is|was)\s+)[^\s,;]+',r'\1[REDACTED]',text)
    text=re.sub(r'(?i)([?&](?:code|access_token|refresh_token|id_token|client_secret|state)=)[^&#\s]+',r'\1[REDACTED]',text)
    # Normalize Markdown escapes only in assignment labels before redaction.
    text=re.sub(r'(?i)([A-Z0-9\\_]*(?:KEY|TOKEN|SECRET|PASSWORD|BYPASS)[A-Z0-9\\_]*)(\s*[=:])',lambda m:m.group(1).replace('\\_','_')+m.group(2),text)
    text=re.sub(r'(?i)([A-Z][A-Z0-9_]*(?:KEY|TOKEN|SECRET|PASSWORD|BYPASS)[A-Z0-9_]*\s*[=:]\s*[\"\x27]?)([^\s\"\x27,}]+)',r'\1[REDACTED]',text)
    text=re.sub(r'\b(?:sk[-_][A-Za-z0-9_-]{12,}|recoup_sk_[A-Za-z0-9_-]{12,}|flxpak_[A-Za-z0-9_-]{12,}|lr_live_[A-Za-z0-9_-]{12,}|gh[pousr]_[A-Za-z0-9_]{15,}|github_pat_[A-Za-z0-9_]{15,})\b','[REDACTED CREDENTIAL]',text)
    text=re.sub(r'(?i)(bearer\s+)[A-Za-z0-9._~-]{15,}',r'\1[REDACTED]',text)
    text=re.sub(r'(?i)(\b(?:api_key|token|secret|password|bypass)\s*[=:]\s*[\"\x27]?)([^\s\"\x27,}]+)',r'\1[REDACTED]',text)
    text=re.sub(r'(?i)([a-z][a-z0-9+.-]*://)[^/\s@:]+:[^/\s@]+@',r'\1[REDACTED USERINFO]@',text)
    text=re.sub(r'(?is)((?:api[ -]?key|access[ -]?token|secret|credential|password)[^\n]{0,100}\n\s*```[^\n]*\n)(.*?)(\n```)',r'\1[REDACTED CREDENTIAL BLOCK]\3',text)
    return text


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--private-corpus',type=Path,required=True)
    p.add_argument('--alias',required=True)
    p.add_argument('--message-index',type=int,default=0)
    p.add_argument('--character-offset',type=int,default=0)
    p.add_argument('--max-chars',type=int,default=24000)
    p.add_argument('--compact',action='store_true',help='Reduce display metadata while retaining source locators')
    p.add_argument('--factored',action='store_true',help='Use previously generated exact instruction-body factoring view')
    a=p.parse_args()
    q=json.loads((a.private_corpus/'review-queue.json').read_text());c=next(x for x in q if x['alias']==a.alias)
    if a.factored:
        d=json.loads((a.private_corpus/'factored'/(a.alias+'.json')).read_text())
        if d['source_sha256']!=c['source_sha256']:raise ValueError('Factored view source hash mismatch')
        c={**c,'messages':d['messages'],'chars':d['view_characters']}
    i,off,budget=a.message_index,a.character_offset,a.max_chars
    print(json.dumps({'alias':a.alias,'total_messages':len(c['messages']),'total_characters':c['chars'],'source_sha256':c['source_sha256'],'start':[i,off],'offset_basis':'factored-view' if a.factored else 'original-visible-text'}))
    while i<len(c['messages']) and budget>0:
        m=c['messages'][i];t=m['text'];piece=t[off:off+budget]
        if a.compact:
            print(f"[{i} {m['item_id']} {m['role']} chars {off}:{off+len(piece)}]")
            print(redact(piece))
        else:
            print(json.dumps({'index':i,'item_id':m['item_id'],'turn_id':m['turn_id'],'role':m['role'],'phase':m['phase'],'range':[off,off+len(piece)],'text':redact(piece)},ensure_ascii=False))
        off+=len(piece);budget-=len(piece)
        if off==len(t):i+=1;off=0
        else:break
    print(json.dumps({'next':[i,off],'end_of_projection':i==len(c['messages']),'note':'Reading a slice is not completion or annotation review.'}))

if __name__=='__main__':main()
