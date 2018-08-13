inputstring = input("enter values : ").strip()
values = [int(i) for i in inputstring.split()]  # covert string to list
if (len(values) == 1):
    print(values[0])

elif (len(values) < 1):
    print("Not a valid input")
else:
    values = list(set(values))  # remove duplicate
    values.sort(reverse=True)  # sort in reverse
    print(values[1])
