n=100
d={}
def digits(n):
  if n<10:
    return [n]
  else:
    return [n%10]+digits(n//10)
for i in range(10):
  d[i]=0
for i in range(1,n+1):
  for j in digits(i):
    d[j]+=1
print(d)    
