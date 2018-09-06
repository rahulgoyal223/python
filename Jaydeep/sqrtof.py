import math
count = int(input())
  
def is_square(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer:
        return True
    else:
        return False
    

hypL = []
tringles = []
for i in range(0, count):
    n = int(input())
    hypL  = [ x for x in range(2,n+1) if is_square(x) == True]
    print(hypL)
    for j in hypL:
        trigs = [ (x,y) for x in range(1,j) for y in  range(1,j) if( (x*x + y*y == j*j) and ((x*y/2)%6 != 0) and ((x*y/2)%28 != 0) and (math.gcd(x,y) == 1 ) and (math.gcd(y,j) == 1 ) ) ]
        tringles.extend(trigs)
        
    print(tringles)
if(len(tringles)> 0):
    tringles.sort()
    print(len(list(k for k,_ in itertools.groupby(tringles))))
else:
    print (0)
  