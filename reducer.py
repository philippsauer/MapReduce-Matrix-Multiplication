#!/usr/bin/env python
import sys
from collections import defaultdict

dictA = defaultdict(list)
dictB = defaultdict(list)

# hashing
for line in sys.stdin: 
    key, value = line.split('\t')
    stripped = value.strip('[]\n')
    name, i, value = stripped.split(', ')
    
    if name == "'A'":
        dictA[key].append(int(value))     
    else:
        dictB[key].append(int(value))

print dictA 
print dictB
  
# calculate
for key in dictA:
    ergebnis = 0
    for v in range(len(dictA[key])):
        ergebnis += int(dictA[key][v]) * int(dictB[key][v])
    print '%s\t%s' % (key, ergebnis) 
        
