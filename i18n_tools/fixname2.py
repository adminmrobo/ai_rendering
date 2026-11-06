# fixname2.py L bundle ids → 저자 이름 한글(안상선)을 Ahn Sangsun으로 바꿔 받아들임
import sys, json, subprocess
L, b, ids = sys.argv[1], sys.argv[2], sys.argv[3].split(',')
o = json.load(open('out/%s.json' % b)); fx = {i: o[i].replace('안상선', 'Ahn Sangsun') for i in ids}
p = '/tmp/claude-0/-home-claude/3f8116dd-983e-51d7-b8bf-9862cada8489/scratchpad/fx_%s.json' % b
json.dump(fx, open(p, 'w'), ensure_ascii=False); subprocess.run(['python3', 'accept.py', L, b, sys.argv[3], p])
