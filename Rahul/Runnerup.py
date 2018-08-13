# runner-up score
print("Enter list:", end=" ")
l = [int(x) for x in input().split()]
l.sort(reverse=True)
if len(l)>1:
 for i in range(1, len(l)):
    if (l[i - 1] > l[i]):
        print(l[i])
        break
elif len(l)==1:
    print(l[0])
else:
    print("Enter valid value")