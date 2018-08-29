import itertools

x=input().split()
s=sorted(x[0])
a=int(x[1])

for i in range(1,a+1):
    l = list(itertools.combinations(s, i))
    for x in sorted(l):
        for j in range(i):
            print(x[j], end='')
        print()
