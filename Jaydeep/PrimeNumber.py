i = 1
j = 100
for number in range(i, j + 1):
    for ind in range(2, number + 1):
        if (number % ind is 0 and number is not ind):
            break
        else:
            if (number - ind == 1 or number - ind == 0):
                print(number)
                break
