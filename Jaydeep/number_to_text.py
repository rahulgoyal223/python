#convert number to text eg. 123 => one hundred twenty three
inputstring = input("enter values : ").strip()
number = int(inputstring)
divisor = 1000
output = ''
# digits = {
#         1:'one',
#         2:'two',
#         3:'three',
#         4:'four',
#         5:'five',
#         6:'six',
#         7:'seven',
#         8:'eight',
#         9:'nine'
#     }

digits = {
        1000:'thousand',
        100 : 'hundered',
        10 : 'ten',
        20:'twenty',
        30:'thirty',
        40:'fourty',
        50:'fifty',
        60:'sixty',
        70:'seventy',
        80:'eighty',
        90:'ninety',
        1:'one',
        2:'two',
        3:'three',
        4:'four',
        5:'five',
        6:'six',
        7:'seven',
        8:'eight',
        9:'nine',
        11:'elevan',
        12:'tweleve',
        13:'thirteen',
        14:'fourteen',
        15:'fifteen',
        16:'sixteen',
        17:'seventeen',
        18:'eighteen',
        19:'nineteen'

    }

while divisor > 0 :
    val = int(number/divisor)
    if val > 0:
        if (divisor > 10):
            # print('val %s'% val)
            output +=' ' + str(digits.get(val,''))
            output +=' ' + str(digits.get(divisor,''))
        else:
            # print('val*divisor %s '% (val*divisor))
            # print('val + int(number/divisor) %s '% (val + int(number%divisor)))
            if((val*divisor) > 9 and output.strip() is not ''):
                output +=' and'
            if((val*divisor) + divisor >20):
                output += ' ' + str(digits.get(val*divisor,''))
            else :
                output += ' ' + str(digits.get(val*divisor + int(number%divisor),''))
                break
    elif number is 0:
        output = 'zero'

    number %= divisor
    divisor = int(divisor/ 10)
    
        
print(output.strip())

