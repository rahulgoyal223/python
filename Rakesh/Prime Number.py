for number in range(2,101):
    for index in range(2,number):
        if(number%index)==0:
            break
    else:
        print(number)
