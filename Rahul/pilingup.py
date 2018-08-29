decisionlist=[]
x=int(input())
for i in range(x):
    mat=input()
    l = [int(x) for x in input().split()]
    if l[0] >= l[len(l) - 1]:
        k = l[0]
    elif l[0] <= l[len(l) - 1]:
        k = l[len(l) - 1]
    decision = True
    while len(l) > 0 and decision == True:
        if l[0] >= l[len(l) - 1] and l[0] <= k:
            k = l.pop(0)
        elif l[0] <= l[len(l) - 1] and l[len(l) - 1] <= k:
            k = l.pop()
        else:
            decision = False
            break

    if decision == True:
        decisionlist.append('Yes')
    else:
        decisionlist.append('No')


for i in decisionlist:
    print(i)
