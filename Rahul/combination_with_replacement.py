import itertools

x=input().split()
s=sorted(x[0])
a=int(x[1])

l=list(itertools.combinations_with_replacement(s,a))

for x in sorted(l):
    for j in range(a):
        print(x[j],end='')
    print()