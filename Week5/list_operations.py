def list_min(l):
  mini=l[0]
  for i in range(len(l)):
    if l[i]<mini:
      mini=l[i]
  return mini

def list_max(l):
  maxi=l[0]
  for i in range(len(l)):
    if l[i]>maxi:
      maxi=l[i]
  return maxi

def list_prefix(l,z):
  new_list=[]
  for i in range(len(z)):
    new_list.append(z[i])
  for i in range(len(l)):
    new_list.append(l[i])
  return new_list 

def list_suffix(l,z):
  new_list=[]
  for i in range(len(l)):
    new_list.append(l[i])
  for i in range(len(z)):
    new_list.append(z[i])
  return new_list 

def list_avg(l):
  sum=0
  for i in range(len(l)):
    sum += l[i]
  avg=sum/len(l)
  return avg

#Executes when run directly. Not when imported also
if __name__ == "__main__":
  l=[12,4,2,39,-85,120]
  print(list_min(l))
  print(list_max(l))
  z=[5,6,8]
  print(list_prefix(l,z))
  print(list_suffix(l,z))
  print(list_avg(l))