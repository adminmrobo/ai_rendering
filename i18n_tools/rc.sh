#!/bin/bash
cd /home/claude/i18n
for b in "$@"; do L=${b%%_*}; rm -f bundles/${b}r.json; python3 check.py $L bundles/$b.json out/$b.json; done
