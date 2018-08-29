import itertools

n=int(input())
l=input().split()
k=int(input())
temp=[]

l = list(itertools.combinations(l, k))
print(l)
print(len(l))
c=0
for i in l:
    if 'a' in ''.join(i):
        c+=1

print(round(c/len(l),4))