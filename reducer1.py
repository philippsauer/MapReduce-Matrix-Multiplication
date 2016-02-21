#!/usr/bin/env python
import sys
from collections import defaultdict
#from pprint import pprint

A = defaultdict(list)
B = defaultdict(list)

# hashing

#list = []
#for line in sys.stdin: 
#    if line.startswith('[[') or line.startswith(' ['):
#        if ']]' in line:
#            print line
#            continue
#    else:   
#        # non debug
#        # print stdin to list
#        list.append(line.strip()) 
#        
#    print line.strip('\n')   
#print ''
#
# mapping
 
#print 'dict   k  i/j value'
for line in sys.stdin: #for line in list:
    line = line.strip()	
    k, value = line.split('\t')
    stripped = value.strip('[]')
    sourceMatrix, iBzwJ, value = stripped.split(',')
    iBzwJ = iBzwJ.strip()	
    if sourceMatrix == "'A'":
        A[int(k)].append((int(iBzwJ), int(value)))
        #print 'A: '+k+ ' ' +A[k][0]+'  '+value
    else:
        B[int(k)].append((int(iBzwJ), int(value)))
        #print 'B: '+k+ ' ' +B[k][0]+'  '+value

# calculate
#pprint(A)
#pprint(B)	

for i in range(len(A[0])):
    for j in range(len(B[0])):
        for k in A:
            value = int(A[k][i][1]) * int(B[k][j][1])
            key = '[%s, %s]' % (i, j)
            print '%s\t%s' % (key, value)
    

        
