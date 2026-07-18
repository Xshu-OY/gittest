import numpy as np
N = 4
MAX_value = 999999
edge = np.mat([[0,2,6,4],[ MAX_value,0,3, MAX_value],[7, MAX_value,0,1],[5, MAX_value,12,0]])
A = edge[:]
path = np.zeros((N,N))
 
def Floyd():
    for i in range(N):
        for j in range(N):
            if(edge[i,j] != N and edge[i,j] != 0):
                path[i][j] = i
    print('init:')
    print(A)
    for a in range(N):
        for b in range(N):
            for c in range(N):
                if(A[b,a]+A[a,c]<A[b,c]):
                    A[b,c] = A[b,a] + A[a,c]
                    path[b][c] = path[a][c]
 
    print('result:')
    print(A)
 
if __name__ == "__main__":
    Floyd()








"""
init:
[[  0    2     6   4]
 [999999  0    3  999999]
 [  7  999999  0   1]
 [  5  999999  12   0]]
result:
[[ 0  2  5  4]
 [ 9  0  3  4]
 [ 6  8  0  1]
 [ 5  7 10  0]]

"""