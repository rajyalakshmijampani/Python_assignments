import random
l=[]
for i in range(30):
  l.append(random.randint(1,365))
l.sort()  
print(l)
repeated=[]
flag=0
i=0
while(i<=len(l)-2):
  if l[i]==l[i+1]:
    flag=1
    if l[i] not in repeated:
      repeated.append(l[i])
  i+=1  
if flag==0:
  print("All distinct birthdays")
else:
  print("Repeated birthdays : ",repeated)
  
