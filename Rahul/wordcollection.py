i=int(input())
l=[]
for x in range(i):
    l.append(input())

d={}
for i in l:
    d[i]=d.get(i,0)+1

print(len(d))
for i in l:
    if i in d:
        print(d[i],end=' ')
        d.pop(i)

