# Prime number
print("Prime numbers in range 1 to 100 are:", end=' ')
for i in range(2, 101):
    z = 0
    for j in range(2, i):
        if (i % j == 0):
            break
    else:
        print(i,end=' ')
