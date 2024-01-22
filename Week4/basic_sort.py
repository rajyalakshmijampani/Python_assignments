l=[12,10,52,8,69,7,1]
x=[]
while len(l)>0:
  min=l[0]
  for j in range(1,len(l)):
    if l[j]<min:
      min=l[j]
  x.append(min)
  l.remove(min)
print(x)  