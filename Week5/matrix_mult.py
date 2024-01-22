def initialize_matrix(dim):
  matrix=[]
  for i in range(dim):
    row=[]
    for j in range(dim):
      row.append(0)
    matrix.append(row)
  return matrix

def dot_product(a,b):
  sum=0
  for i in range(len(a)):
    sum+=a[i]*b[i]
  return sum

def row(M,r):
  return(M[r])

def column(M,c):
  ans=[]
  for i in range(len(M)):
    ans.append(M[i][c])
  return ans

def mat_mult(A,B):
  dim=len(A)
  C=initialize_matrix(dim)
  for i in range(dim):
    for j in range(dim):
      C[i][j]=dot_product(row(A,i),column(B,j))
  return C

A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[1,2,3],[4,5,6],[7,8,9]]
print(mat_mult(A,B))