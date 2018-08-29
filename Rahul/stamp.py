s='1222311'
i=0
d={}
d=''
while i<len(s):
    count=1
    j=i+1
    while j<len(s):
        if s[i]==s[j]:
            count+=1
            j+=1
        else:
            break
    d+= '({}, {}) '.format(count,s[i])
    i = j

print(d)