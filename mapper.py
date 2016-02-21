#!/usr/bin/env python
import os, sys
import numpy as np

m = int(sys.argv[1])
n = int(sys.argv[2])
p = int(sys.argv[3])
h = int(sys.argv[4])

A = np.random.randint(h, size=(m, n))
B = np.random.randint(h, size=(n, p))

# print key-value pairs for A where key = target in C
# print '%s\t%s' % ('length',['A',m])
for i in range(m):
    for j in range(n):
        for k in range(p):
            print '%s\t%s' % ([i,k],['A',j, A[i][j]])

# print key-value pairs for B where key = target in C	
# print '%s\t%s' % ('length',['B',p])
for i in range(n):
   for j in range(p):
        for k in range(m):
            print '%s\t%s' % ([k,j],['B',i,B[i][j]])