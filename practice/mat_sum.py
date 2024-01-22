A=B=[[1,2],[3,4]]
C=[[1,2]]
res=[]
if len(A)==len(B)==len(C):
  if len(A[0])==len(B[0])==len(C[0]):
    for i in range(len(A)):
      res.append([])
      for j in range(len(A[0])):
        res[i].append(0)
        res[i][j]=A[i][j]+B[i][j]+C[i][j]
  else:
    print(-1)
else:
  print(-1)

print(res)
      