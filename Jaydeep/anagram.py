#check whether two strings are anagram of each other

def areAnagram(a,b):
    if(len(a)!=len(b)):
        return False
    else:
        for i in range(0,len(a)):
            print("a %s b %s" %(a,b))
            if(a[i] in b):
                b = b.replace(a[i],'',1)
            else:
                break
        else:
            return True
        return False


print(areAnagram("12314123131231231","12314123131231230"))
# print(areAnagram("12314123131231231","12314123131231230"))