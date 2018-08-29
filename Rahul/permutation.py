import itertools

x=input().split()
s=x[0]
a=int(x[1])

l=list(itertools.permutations(s,a))

for x in sorted(l):
    for j in range(a):
        print(x[j],end='')
    print()