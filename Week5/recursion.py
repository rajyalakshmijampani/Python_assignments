def sum(n):
  if n==1:
    return 1
  else:
    return n+sum(n-1)

def comp_interest(p,t,r):
  if t==1:
    return p*(1+r/100)
  else:
    return (comp_interest(p,t-1,r))*(1+r/100)

print(sum(100))
print(comp_interest(2000,5,10))