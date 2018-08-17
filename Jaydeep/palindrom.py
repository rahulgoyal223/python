#find longest palindrome 

def isPalindrome(val):
    # print(val)
    if(len(val)%2 == 0):
        rangeFromI = int(len(val) / 2)-1
    else:
        rangeFromI = int(len(val)/2)

    for i,j in zip(range( rangeFromI, -1,-1 ) , range(int(len(val)/2), len(val)+1) ): 
        if(val[i] != val[j]):
            break
    else:
        return True
    return False

answer = ""
a= input()
for i in range(0, len(a)):
    last = a.rfind(a[i],i+1)
    # print("last %s"% last)
    if(last >= 0):
        res = isPalindrome(a[i:last+1])
        if(res == True and len(a[i:last+1]) > len(answer)):
            answer = a[i:last+1]

print (answer)