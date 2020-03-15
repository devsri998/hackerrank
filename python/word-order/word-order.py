#!/usr/bin/env python

from collections import Counter

n=int(input())


l=list(input() for i in range(n))
m=Counter(l)
        
print(len(m))
for i in m:
    print(m[i],end=" ")

