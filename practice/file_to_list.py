f=open('practice/details.csv','r')
l=[]
keys_list=f.readline().strip().split(",")
line=f.readline()
while line!="":
  line_list=line.split(",")
  d={}
  for i in range(len(line_list)):
    if i==0:
      d[keys_list[i]]=line_list[i]
    else:
      d[keys_list[i]]=int(line_list[i])
  l.append(d)
  line=f.readline()
f.close()  
print(l)  
    
  