#!/usr/bin/env python
import sys
from collections import defaultdict

# forward key-value pairs to reducer
C = defaultdict(int)

for line in sys.stdin: 
    key, value = line.split('\t')
    value = int(value)
    if not key in C:
        C[key] = value
        continue
    C[key] = C[key] + value
        

for key in C:       
    print '%s\t%s' % (key, C[key])