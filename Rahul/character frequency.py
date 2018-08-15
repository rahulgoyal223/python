s = input('Sample String :')

d={}

for x in s:
    d[x]=d.get(x,0)+1

print(d)