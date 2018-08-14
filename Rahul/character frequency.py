s = input('Sample String :')
stringSet = set()
stringSet.update(s)
frequency = {}

for i in stringSet:
    k = 0
    for j in s:
        if (i == j):
            k += 1
    frequency[i] = k
print('Expected Result : ', frequency)
