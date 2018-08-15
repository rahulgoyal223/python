ones={0:'Zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
twenties={0:'',10:'ten',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety'}
teens={11:'eleven',12:'twelve',13:'thirteen',18:'eighteen'}
t= input("Enter number:")
l=[int(x) for x in t]

while l[0]==0:
    l.remove(0)
s=''
if len(l)==1:
    s=s+ones[l[0]]

elif len(l)==2:
    k= int(str(l[0])+str(l[1]))
    if k in twenties.keys():
        s = s + twenties[k]
    elif k in teens.keys():
        s = s + teens[k]
    elif k in [14,16,17,19]:
        s=s+ones[l[1]]+'teen'
    else:
        s = s + twenties[(k // 10) * 10] + '  ' + ones[k % 10]

elif len(l)==3:
    if l[2]!=0:
        s=s+ones[l[0]]+' hundred '+twenties[l[1]*10]+' '+ones[l[2]]
    else:
        s = s + ones[l[0]] + ' hundred ' + twenties[l[1]*10]


elif len(l)==4:
    if l[1]==0 and l[3]==0:
        s=s+ones[l[0]]+' thousand '+twenties[l[2]*10]
    elif l[1] == 0:
        s = s + ones[l[0]] + ' thousand '+ twenties[l[2] * 10] + ' ' + ones[l[3]]
    elif l[3] == 0:
        s = s + ones[l[0]] + ' thousand ' + ones[l[1]] + ' hundred ' + twenties[l[2] * 10]
    else:
        s = s + ones[l[0]] + ' thousand ' + ones[l[1]] + ' hundred ' + twenties[l[2] * 10] + ' ' + ones[l[3]]

print('Output: '+s)
