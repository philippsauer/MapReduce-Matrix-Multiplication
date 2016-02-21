#!/usr/bin/env python
import os, sys
import numpy as np

# anzahl spalten A & C
m = int(sys.argv[1])
# anzahl Zeilen A & Spalten B
n = int(sys.argv[2])
# anzahl Zeilen B & C
p = int(sys.argv[3])
# hoehe der werte
h = int(sys.argv[4])

# A = m x n
# B = n x p
# C = m x p

# generate random matrix A and B having values from '0' to 'h'	
A = np.random.randint(h, size=(m, n))
B = np.random.randint(h, size=(n, p))

#print A
#print B

for i in range(m):
    for k in range(n):
        print '%s\t%s' % (k,['A',i, A[i][k]])

for k in range(n):
    for j in range(p):
        print '%s\t%s' % (k,['B',j, B[k][j]])