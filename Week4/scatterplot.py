import matplotlib.pyplot as plt
import csv

maths_list=[]
physics_list=[]

f=open('Week4/scores.csv','r')
f.readline()
for line in f:
  l=line.split(",")
  maths_list.append(int(l[0]))
  physics_list.append(int(l[1])) 
f.close()  

plt.scatter(maths_list, physics_list)
plt.xlabel("Maths")
plt.ylabel("Physics")
plt.show()