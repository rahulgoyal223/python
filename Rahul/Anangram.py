s1= input("Enter string1:")
s2= input("Enter string2:")

if len(s1)!=len(s2):
    print('Not Anangram')
elif len(s1)==0:
    print('Not Anangram')
else:
    l = [x for x in s2]
    counter = 0
    for x in s1:
        for i in range(len(l)):
            if l[i] == x:
                l[i] = ''
                counter += 1
    if counter == len(s1):
        print('Anangram')
    else:
        print('Not Anangram')





