#!/bin/bash
# logc.sh L fNN model tokens  → cost.csv 한 줄
python3 -c "import json;b=json.load(open('bundles/$1_$2.json'));print('$1,$2,%d,%d,$3,$4'%(len(b['units']),sum(len(u['ko']) for u in b['units'])))" >> cost.csv
