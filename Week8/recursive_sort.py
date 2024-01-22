L=[3,5,1,9,40,-3]
def Sort(L):
  if len(L)!=0:
    m=min(L)
    L.remove(m)
    return [m]+Sort(L)
  else:
    return L
print(Sort(L))  
  