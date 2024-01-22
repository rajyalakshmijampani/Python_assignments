L=[1,6,8,10,38,94,219,834,1009]

def search(L,n,start,end):
  if len(L)!=0 and start<end:
    mid=(start+end)//2
    if L[mid]<n:
      return search(L,n,mid+1,end)
    elif L[mid]>n:
      return search(L,n,start,mid)
    else:
      return mid
  return -1  

print(search(L,1009,0,len(L)))