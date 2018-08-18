A1=[[1,2],[3,4]]
A2=[3]
dot=0
cross=0
for i in range(len(A1)):
    cross = -cross
    dot+=A1[i]*A2[i]
    cross=cross-A1[i]*A2[len(A2)-(i+1)]


print(dot)
print(cross)



