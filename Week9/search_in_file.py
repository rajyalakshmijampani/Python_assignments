f = open('Week9/firstFile.txt', 'r')
check1 = 9848245693
check2 = 9848255693
c1 = c2 = False
s = f.readline()
while s != '':
  if str(check1) in s:
    c1 = True
  if str(check2) in s:
    c2 = True
  if c1 and c2:
    break
  s = f.readline()
f.close()
if c1 and c2:
  print("Both strings found")
elif c1:
  print('Only string 1 found')
elif c2:
  print('Only string 2 found')
