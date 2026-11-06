# 손 보정: accept.py L 묶음 id [새 번역 파일(json {id:text})] — 검사 오탐이거나 손으로 고친 번역을 메모리에 넣는다
import sys, json
sys.path.insert(0, '/home/claude/i18n'); import check
L, b = sys.argv[1], sys.argv[2]; ids = sys.argv[3].split(',')
out = json.load(open('/home/claude/i18n/out/%s.json' % b))
if len(sys.argv) > 4: out.update(json.load(open(sys.argv[4]))); json.dump(out, open('/home/claude/i18n/out/%s.json' % b, 'w'), ensure_ascii=False)
check.absorb('/home/claude/i18n/bundles/%s.json' % b, {i: out[i] for i in ids}, L); print('accepted', ids)
