import itertools

A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

l=list(itertools.product(A,B))

for x in l:
    print(x,end=' ')



