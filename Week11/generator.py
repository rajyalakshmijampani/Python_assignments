def squares_upto(a):
  x=1
  while x<=a:
    yield x*x
    x+=1

n=int(input("Enter a number below 10:"))
res=squares_upto(n)
permission=input(f"You asked for squares upto {n},Shall I start printing:(y/n)")
while permission=='y':
  try:
    print(next(res))
    permission=input("Shall I Continue:(y/n)")
  except:
    print("That's it")
    break
  