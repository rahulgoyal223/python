from itertools import combinations
string = input().split()
for n in range (1,int(string[1])+1):
    listPermutations =list(combinations("".join(sorted(string[0])),n))
    #print(listPermutations)
    for per in listPermutations:
        print("".join(per))
