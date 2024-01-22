import random
import numpy

# ------- Dot Product --------

l=random.sample(list(range(100)),5) 
#list(range(100)) generates [0,1,...99] list. random.sample takes a random sample of length 5 from it
m=random.sample(list(range(10)),5)
dot_product=0
for i in range(len(l)):
  dot_product+=l[i]*m[i]
print("------Dot Product-----")
print(l,m)
print("Dot product is :",dot_product)  


# ------ Matrix addition -------

dim=3
A=[]
B=[]
C=[]
for i in range(dim):
  A.append(random.sample(list(range(10)),dim))
  B.append(random.sample(list(range(10)),dim))
  C.append([0]*dim)
for i in range(dim):
  for j in range(dim):
    C[i][j] = A[i][j] + B[i][j]
print("--------Matrix Addition---------")    
print(A,B,C,sep='\n') 

# ----- Matrix multiplication -------

dim=3
A=[]
B=[]
C=[]
for i in range(dim):
  A.append(random.sample(list(range(10)),dim))
  B.append(random.sample(list(range(10)),dim))
  C.append([0]*dim)
for i in range(dim):
  for j in range(dim):
    for k in range(dim):
      C[i][j]+=A[i][k]*B[k][j]
print("------Matrix multiplication-----")    
print(A,B,C,sep='\n')


# ------Matrix multiplication by numpy----
dim=3
A=[]
B=[]
for i in range(dim):
  A.append(random.sample(list(range(10)),dim))
  B.append(random.sample(list(range(10)),dim))
X=numpy.mat(A)
Y=numpy.mat(B)
print("--------By numpy-------")
print(X,Y,X*Y,sep='\n')