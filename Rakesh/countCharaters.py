kvp ={}
inputstring = "google.com"
for key in inputstring:
    if key in kvp :
        kvp[key] +=1
    else:
        kvp[key] =1
print(kvp)        
    
