s=input()
d={}
for i in s:
    d[i]=d.get(i,0)+1

l=sorted(list(set(d.values())),reverse=True)
c=0
for i in l:
    k = []
    for j in d:
        if d[j]==i:
            k.append(j)
    k=sorted(k)
    for j in k:
        if c < 3:
            print(j, i)
            c += 1
        else:
            break





