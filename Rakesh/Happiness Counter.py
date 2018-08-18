# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 15:18:57 2018

3 2
1 5 3
3 1
5 7

Sample Output

1

https://www.hackerrank.com/challenges/no-idea/problem

@author: Rakesh
"""

mn = str(input()).split()
array = str(input()).split()
setA = set(str(input()).split())
setB = set(str(input()).split())
hapinessCount =0
for arrayElement in array:
    if arrayElement in setA:
        hapinessCount +=1
    elif arrayElement in setB:
        hapinessCount -=1
print(hapinessCount)