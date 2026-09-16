# With initializing a new matrix
'''
m = [[1,2,3],[4,5,6],[7,8,9]]
n = len(m)
new_m = []
for i in range(n):
    new_m.append([])
    for j in range(n):
        new_m[i].append(0)
for i in range(n):
    for j in range(n):
        new_m[i][j] = m[n-1-j][i]
print(new_m)
'''
# Without initializing a new matrix
mat = [[1,2,3],[4,5,6],[7,8,9]]
n = len(mat)
# Transpose of the matrix
for i in range(n):
    for j in range(i+1,n):
        mat[i][j] , mat[j][i] = mat[j][i] , mat[i][j]
# Reverse of each row of the matrix
for i in range(n):
    mat[i].reverse()
print(mat)