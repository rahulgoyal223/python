# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 11:04:46 2018
Find Longest Palindrom in given string 
@author: Rakesh
"""
def Substring(string):
    length = len(string)
    for end in range(length, 0,-1):
        for i in range(length-end+1):
            yield string[i:i+end]

lst = []
inputstring =input("Enter string : ")            
for l in Substring(inputstring):
    if len(l) > 1 and l.lower() == l.lower()[::-1]:
        lst.append(l)
        
if len(lst) >=1:
    print(lst[0])
else:
    print("No Palindrom found")
