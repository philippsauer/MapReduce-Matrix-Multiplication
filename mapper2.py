#!/usr/bin/env python
import sys

# forward key-value pairs to reducer
for line in sys.stdin: 
    line = line.strip()
    key, value = line.split('\t')
    print '%s\t%s' % (key, value)