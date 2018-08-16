# A = [ [1, 2, 3], [4,5,6] ]
# B = [ [7, 8], [9,10], [11,12] ]
A = [ [1, 2], [3,4] ]
B = [ [2, 0], [1,2] ]
# A = [ [3,4,2] ]
# B = [ [13, 9, 7, 15], [8,7,4,6], [6,4,0,3] ]
# A = [[4,-4], [-2,-3], [-1,0]]
# B = [[1,2,3], [4,5,6]]

def dot(A,B):
    if not ( len(A)>0 and len(B)>0 and  type(A[0]) == type([]) and len(A[0]) == len(B) ):
        print("invlaid matrix")
    else:
        # print('2x2')
        res = [0] * len(A)
        for i in range(0,len(A)):
            res[i] = [0] * len(B[0])
            # print(res)
            for j in range(0,len(B[0])):
                # print("i %s j %s " %(i, j))
                res[i][j] = 0
                for k in range(0,len(B)):
                    # print("A[ %s  %s] " %(i, k)) 
                    # print("B[ %s  %s] " %(k, i))
                    res[i][j] += A[i][k] * B[k][j]
    return  res

print(dot(A,B))
