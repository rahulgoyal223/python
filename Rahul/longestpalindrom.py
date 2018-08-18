s= input("Enter String number:")
length=len(s)
lonpal=''
if length<3:
    print("No palindrome")
else:
    for z in range(3, len(s) + 1):
        for i in range(length):
            a = s[i:i + z]
            if len(a) == z:
                if a == a[::-1]:
                    lonpal = a
            else:
                break
    if lonpal == '':
        print("No palindrome")
    else:
        print(lonpal)



