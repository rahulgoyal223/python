import re
nm = input().split()

n = int(nm[0])

m = int(nm[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

print(matrix)

s=''
for i in range(m):
    for j in matrix:
        s+=j[i]
print(s)

l3 = re.findall('[a-z0-9A-Z][^a-z0-9A-Z]+[a-z0-9A-Z]',s)
print(l3)


for i in l3:
    s=s.replace(i[1:len(i)-1],' ',1)

print(s)
