i = 1
while (i<100):
    j=2
    while (j<=i):
        #print j
        if (i%j is 0 and i is not j):
            break
        else:
            if (i-j == 1 or i-j is 0):
                print(i)
                break
            else:
                j = j+1
    i = i+1

print("good bye")