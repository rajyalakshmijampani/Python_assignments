class Student:
  def __init__(self,roll_no,name,total):
    self.roll_no=roll_no
    self.name=name
    self.total=total
  def display(self):
    print(self.roll_no,self.name,self.total)
  def result(self):
    if self.total>120:
      print("Result of",self.name, "is Pass")
    else:
      print("Result of",self.name, "is Fail")

s0=Student(0,'Bhuvan',500)
s1=Student(1,'Hari',100)
s0.result()
s1.result()