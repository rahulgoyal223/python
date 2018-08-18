# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 10:52:37 2018
find given two input strings are anagram or not
@author: Rakesh
"""

str1 = input("enter 1st string : ")
str2 = input("enter 2nd string : ")

if sorted(str1)==sorted(str2):
    print("string are anagram")
else:
    print("string NOT are anagram")

