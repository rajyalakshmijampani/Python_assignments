class Person():
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def display(self):
    print(self.name,self.age)

class Student(Person): #Inheritence
  def __init__(self,name,age,marks):
    super().__init__(name,age)
    self.marks=marks
  def display(self):
    super().display()
    print(self.marks)
    
class Employee(Person): #Inheritence
  def __init__(self,name,age,salary):
    super().__init__(name,age)
    self.salary=salary
  def display(self): #Method overriding
    print(self.name,self.age,self.salary)

s0=Student('Ram',25,500)
s1=Employee('Siva',45,30000)
s0.display()
s1.display()