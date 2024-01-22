L=[150,20,0,100,120,201,50,101,141,40,20]
streak_len=0
max_streak=0
for score in L:
  if score>=100:
    streak_len+=1
    if streak_len>max_streak:
      max_streak=streak_len
  else:
    streak_len=0
print(max_streak)    
    