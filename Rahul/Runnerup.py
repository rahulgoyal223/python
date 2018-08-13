# runner-up score
l = eval(input("Enter list:"))
l.sort(reverse=True)
for i in range(1, len(l)):
    if (l[i - 1] > l[i]):
        print(l[i])
        break
