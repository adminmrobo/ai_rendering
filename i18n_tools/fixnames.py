import json,os,sys
sys.path.insert(0,'/home/claude/i18n');import merge
d=json.load(open('/home/claude/i18n/2-5.units.json'));U={u['ko']:u for u in d['units'] if u['ko'] in ('안','상선')}
for L in ['en','zh','ja','ru','uz','vi']:
    p='/home/claude/i18n/tm/%s.json'%L
    if not os.path.exists(p):continue
    tm=json.load(open(p));tm[merge.key(U['안'])]='Ahn';tm[merge.key(U['상선'])]='Sangsun';json.dump(tm,open(p,'w'),ensure_ascii=False)
