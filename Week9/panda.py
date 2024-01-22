#Find max total - File Handling
'''
f=open('Week9/scores.csv','r')
s=f.readlines()[1:]
max=0
for student in s:
  report=student.split(',')
  if int(report[2])>max:
    max=int(report[2])
print(max)
f.close()
'''

#Using Pandas
import pandas as pd
scores=pd.read_csv('Week9/scores.csv')
#print(scores)
#print(scores['Total'].max())
#print(scores['Total'].min())
#print(scores['Total'].mean())
#print(scores['Total'].sort_values())
#print(scores['Total'].sort_values(ascending=False))
#print(scores.shape) #Tuple (number of rows,number of columns)
#print(scores.count())
#print(type(scores),type(scores['Name']))
#print(scores[scores['Name']=='Nisha'])
#print(scores[scores['Gender']=='M']['Total'].max())
#print("Physics Grade A count: ",scores[scores['Physics'] > 85].shape[0])
#print("Physics Grade B count: ",scores[scores['Physics'].between(70,85)].shape[0])
subject=['Mathematics','Physics','Chemistry']
for sub in subject:
  print(sub,"Male Grade A count: ",scores[(scores[sub] > 85) & (scores['Gender']=='M')].shape[0])
  print(sub,"Female Grade A count: ",scores[(scores[sub] > 85) & (scores['Gender']=='F')].shape[0])


print("All students \n",scores.groupby('Gender').groups)
  
for sub in subject:
  avg = scores[sub].mean()
  print(sub, "above averagae \n",scores[(scores[sub] > avg)].groupby('Gender').groups)