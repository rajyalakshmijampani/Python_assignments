class AgeError(Exception):
  pass

a=int(input())
if a<18:
  #raise AgeError('You are underage')
  raise Exception('You are underage')