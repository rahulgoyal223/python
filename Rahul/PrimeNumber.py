# Prime number
print("Prime numbers in range 1 to 100 are:", end=' ')
for i in range(1, 101):
    z = 0
    for j in range(2, i):
        if (i % j == 0):
            z = 1
            break
    if (z == 0):
        print(i, end=',')
