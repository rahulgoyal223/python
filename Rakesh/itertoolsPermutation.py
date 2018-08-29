from itertools import permutations
string = input().split()
listPermutations =list(permutations("".join(sorted(string[0])),int(string[1])))
for per in listPermutations:
    print("".join(per))
