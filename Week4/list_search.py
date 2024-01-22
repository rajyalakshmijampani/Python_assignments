import random
l=[]
for i in range(100000):
  l.append(random.randint(1,100000))
n=int(input("Enter a number, Type -1 to exit:"))
while (n!=-1):
  flag=0
  for j in range(len(l)-1):
    if l[j]==n:
      print("Element found")
      flag=1;
      break
  if flag==0:
    print("Element not found")
  n= int(input("Enter a number, Type -1 to exit:")) 