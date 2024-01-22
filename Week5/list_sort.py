from Week5.list_operations import list_min

def sorting(l):
  if len(l)!=0:
    mini=list_min(l)
    l.remove(mini)
    return [mini]+sorting(l)  
  else:
    return []

l=[5,60,7,1,-2,9,1]
print(sorting(l))
