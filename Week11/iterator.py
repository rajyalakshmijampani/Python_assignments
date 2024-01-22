names=['Raji','Santosh','DK','Akshaya','DAV','KPHB']
noun=iter(names)
a=next(noun)
while a!='':
  print(f'Hi {a}')
  try:
    a=next(noun)
  except:
    break