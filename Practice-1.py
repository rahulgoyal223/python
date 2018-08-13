# Prime number
for i in range(1, 101):
    z = 0
    for j in range(2, i):
        if (i % j == 0):
            z = 1
            break
    if (z == 0):
        print(i)

# runner-up score
l = eval(input("Enter list:"))
l.sort(reverse=True)
for i in range(1, len(l)):
    if (l[i - 1] > l[i]):
        print(l[i])
        break
