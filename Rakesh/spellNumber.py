# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 19:43:18 2018
display number in words
@author: Rakesh
"""
teenplace = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen"
            ,"eighteen","nineteen"]
tensplace = ["", "","twenty","thirty","fourty","fifty","sixty","seventy","eighty", "ninty"]

digitplace = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
def ProcesslessThanHunred(number):
    part = number
    strNumber = ""

    if part >= 20:
        strNumber +=  " " + tensplace[int(part/10)]
        part = part % 10

    elif part >= 10:
        strNumber += " " + teenplace[int(part%10)]
        part = 0

    if part >= 0:
        strNumber += " " + digitplace[part]
    return strNumber


number = 9521
strthoudand = ""
strHundred = ""
numThousand = int(number/1000)
numHundred = int(int(number/100)%10)
numdigit = number % 100
strdigit = ProcesslessThanHunred(numdigit)

if numThousand > 0:
    strthoudand = digitplace[numThousand]+" thousand "
    strthoudand
if numHundred > 0:
    strHundred = digitplace[numHundred]+" hundred "
print( strthoudand + strHundred+ strdigit)
         