#!/usr/bin/env python3
"""Factor only byte-identical repeated instruction bodies within one chat.

The first occurrence stays in full; later occurrences carry a SHA-256 reference.
Every surrounding byte, timestamp and outcome remains. This is a reading view,
not a new source capture, a summary, or evidence that a reviewer read the body.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--private-corpus',type=Path,required=True)
    p.add_argument('--alias',required=True)
    a=p.parse_args()
    q=json.loads((a.private_corpus/'review-queue.json').read_text());c=next(x for x in q if x['alias']==a.alias)
    seen={}; occurrences=[]; messages=[]
    for index,m in enumerate(c['messages']):
        def replace(match):
            body=match.group(1);h=hashlib.sha256(body.encode()).hexdigest()
            occurrences.append({'message_index':index,'item_id':m['item_id'],'start':match.start(1),'end':match.end(1),'sha256':h})
            if h not in seen:
                seen[h]={'first_message_index':index,'body':body};return match.group(0)
            return '<instructions>[EXACT REPEAT sha256='+h+'; first message index='+str(seen[h]['first_message_index'])+']</instructions>'
        text=re.sub(r'(?s)<instructions>(.*?)</instructions>',replace,m['text'])
        messages.append({**m,'text':text,'original_characters':len(m['text'])})
    d=a.private_corpus/'factored';d.mkdir(exist_ok=True,mode=0o700)
    out=d/(a.alias+'.json');out.write_text(json.dumps({'alias':a.alias,'source_sha256':c['source_sha256'],'messages':messages,'original_characters':c['chars'],'view_characters':sum(len(m['text']) for m in messages),'exact_body_dictionary':seen,'occurrences':occurrences},ensure_ascii=False));out.chmod(0o600)
    print(json.dumps({'alias':a.alias,'unique_instruction_bodies':len(seen),'occurrences':len(occurrences),'raw_characters':c['chars'],'factored_characters':sum(len(m['text']) for m in messages),'output':str(out)}))

if __name__=='__main__':main()
