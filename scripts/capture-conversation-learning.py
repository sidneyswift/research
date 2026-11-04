#!/usr/bin/env python3
"""Capture visible local chat projections read-only into an explicitly private directory.

No source databases are changed. No model/embedding/training API is called.
Internal subagent/guardian threads are inventoried separately, not mislabeled user chats.
"""
from __future__ import annotations
import argparse
import collections
import hashlib
import json
import os
from pathlib import Path
import sqlite3


def write(path, value):
    payload=json.dumps(value,ensure_ascii=False,indent=2)+'\n'
    with path.open('x') as f:
        os.chmod(path,0o600)
        f.write(payload)
    return hashlib.sha256(payload.encode()).hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--codex-home',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    repo=Path(__file__).resolve().parents[1]
    output=args.output.resolve()
    if output==repo or repo in output.parents:
        p.error('Private capture output must be outside the Research repository')
    output.mkdir(parents=True,exist_ok=True);output.chmod(0o700)
    (output/'chats').mkdir(exist_ok=True,mode=0o700)
    if (output/'local-inventory.json').exists():
        p.error('Inventory already frozen; use that snapshot instead of silently recapturing')
    state=sqlite3.connect(f'file:{args.codex_home}/state_5.sqlite?mode=ro',uri=True)
    history=sqlite3.connect(f'file:{args.codex_home}/thread_history_1.sqlite?mode=ro',uri=True)
    state.row_factory=sqlite3.Row;history.row_factory=sqlite3.Row
    state.execute('BEGIN');history.execute('BEGIN')
    metadata=[dict(x) for x in state.execute('SELECT id,source,title,rollout_path,created_at,updated_at,archived,model,model_provider,cli_version FROM threads ORDER BY id')]
    roots=[]; internal=collections.Counter(); excluded=[]
    for row in metadata:
        try:source=json.loads(row['source'])
        except ValueError:source=row['source']
        if isinstance(source,dict) and 'subagent' in source:
            kind='guardian' if source['subagent'].get('other')=='guardian' else 'subagent'
            internal[kind]+=1;excluded.append({'id':row['id'],'kind':kind,'source':source})
        else:roots.append(row)
    result=[];types=collections.Counter()
    for n,row in enumerate(roots,1):
        tid=row['id']; alias=f'C{n:04}'
        turns=[dict(t) for t in history.execute('SELECT thread_id,turn_id,rollout_ordinal,status,error_json,started_at,completed_at FROM thread_turns WHERE thread_id=? ORDER BY rollout_ordinal',(tid,))]
        messages=[]; errors=[]; total=0; decode_errors=[]
        for item in history.execute('SELECT item_id,turn_id,rollout_ordinal,item_type,item_json FROM thread_items WHERE thread_id=? ORDER BY rollout_ordinal',(tid,)):
            total+=1;types[item['item_type']]+=1
            try:body=json.loads(item['item_json'])
            except ValueError:decode_errors.append(item['item_id']);continue
            kind=body.get('type',item['item_type'])
            entry={'item_id':item['item_id'],'turn_id':item['turn_id'],'ordinal':item['rollout_ordinal'],'item':body}
            if kind in ('userMessage','agentMessage'):messages.append(entry)
            elif kind=='commandExecution' and (body.get('exitCode') not in (None,0) or 'Traceback (most recent call last)' in str(body.get('output',{}))):errors.append(entry)
        doc={'capture_kind':'local-history-visible-projection','alias':alias,'thread':row,'turns':turns,'messages':messages,'command_error_candidates':errors,'projection_items_examined':total,'json_decode_errors':decode_errors,'limitations':['Not a native export; hidden reasoning excluded.','Only visible user/assistant messages plus command-error candidates retained.','Attachments and complete tool results not reconstructed.','Read-only snapshot boundary; active chats can later advance.']}
        name=alias+'.json';digest=write(output/'chats'/name,doc)
        result.append({'alias':alias,'thread_id':tid,'title':row['title'],'archived':bool(row['archived']),'projection_file':'chats/'+name,'sha256':digest,'turns':len(turns),'messages':len(messages),'command_error_candidates':len(errors),'items_examined':total,'capture_status':'captured' if messages else 'empty_projection','review_status':'pending','source_rollout_exists':Path(row['rollout_path']).exists(),'decode_errors':len(decode_errors)})
    write(output/'local-inventory.json',{'kind':'frozen-local-history-inventory','chats':result,'internal_session_counts':dict(internal),'internal_sessions':excluded,'item_type_counts':dict(types),'scope':'User-facing roots selected by non-subagent source; internal sessions inventoried as supporting/system records, not human conversation threads.','snapshot_note':'Separate read transactions for metadata and projection database; no claim of global cross-database atomicity.'})
    print(json.dumps({'user_facing_chats':len(result),'turns':sum(x['turns'] for x in result),'messages':sum(x['messages'] for x in result),'empty_projections':sum(x['messages']==0 for x in result),'internal_sessions':dict(internal),'decode_errors':sum(x['decode_errors'] for x in result)}))

if __name__=='__main__':main()
