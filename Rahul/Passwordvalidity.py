import re
def isCorrectNum(word):
    if len(word) in range(6,13):
        return word

a='sss'

re.fullmatch(r'(?P=<d>[a-z]).(?P=d)',a)