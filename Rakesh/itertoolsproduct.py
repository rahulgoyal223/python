#https://www.hackerrank.com/challenges/itertools-product/problem
from itertools import product
A =[int(n) for n in input().split(" ")]
B =[int(n) for n in input().split(" ")]
lstProduct =list(product(A,B))
for prd in lstProduct:
    print(prd,end=" ")
