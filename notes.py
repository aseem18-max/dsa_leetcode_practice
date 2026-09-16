mat = [[1,2,3],[4,5,6],[7,8,9]]
n = len(mat)
for i in range(n):
    for j in range(i+1,n):
        mat[i][j] , mat[j][i] = mat[j][i] , mat[i][j]
print(mat)
for i in range(n):
    mat[i].reverse()
print(mat)
