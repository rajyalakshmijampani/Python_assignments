def add_sub(c,a=10,b=20 ): # default argument
  return a+b-c

print(add_sub(10,30,20)) #positional arguments
print(add_sub(b=30,a=10,c=20)) #keyword arguments
print(add_sub(30,10,a=20)) #mixed arguements
print(None)

def printing():
  global x
  x=x+5
  print("From function" , x)

x=6
printing()
print(x)