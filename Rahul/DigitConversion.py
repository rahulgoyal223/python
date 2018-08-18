tenths={100:'hundred',1000:'thousand'}
numbers= {
    0: 'Zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
    10: 'ten', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
    90: 'ninety',
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
    18: 'eighteen', 19: 'nineteen'
}

#number= int(input("Enter a 4 digit number:"))
number=112
divisor=1000
s=''

m=0

while divisor>0:
    c=number=number//divisor

    print(m)


    m=number%divisor
    if m in numbers.keys():
        s+=numbers[m]
    divisor/=10
print(s)