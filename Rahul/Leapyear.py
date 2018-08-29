year=2100

def isleap(year):
    leap = False
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    return leap

l=list(filter(isleap,range(1900,2019)))

print(l)

