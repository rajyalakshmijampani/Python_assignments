import random
class Student:
    count = 0
    def __init__(self, name, roll, maths, physics, chemistry):
        Student.count += 1
        self.roll = roll
        self.name = name
        self.maths = maths
        self.physics = physics
        self.chemistry = chemistry

class Group:
    def __init__(self):
        self.members = [ ]

    def add(self, student):
        self.members.append(student)

    def print_members(self):
        for student in self.members:
            print(student.name)

    def remove(self, roll):
      found = False
      for student in self.members:
          if student.roll == roll:
              found = True
              break
      if found:
          self.members.remove(student)
      else:
          print('Student not found')

    def pick_leader(self):
      potential = [ ]
      for student in self.members:
          avg = (student.maths +
                 student.physics +
                 student.chemistry) // 3
          if avg >= 80:
              potential.append(student)
      print([x.name for x in potential])      
      if len(potential) > 0:
          index = random.randint(0, len(potential) - 1)
          self.leader = potential[index].name
      else:
          self.leader = None 
        
Student.count = 0
f = open('Week10/scores.csv', 'r')
f.readline()	# ignore the header
students = [ ]
for line in f:
    roll, name, maths, physics, chemistry = line.strip().split(',')
    roll, maths, physics, chemistry = int(roll), int(maths), int(physics), int(chemistry)
    students.append(Student(name, roll, maths, physics, chemistry))
f.close()
print(Student.count)

study_group = Group()
study_group.add(Student('Lathika', 1, 100, 90, 80))
study_group.add(Student('Keerthana', 2, 80, 70, 60))
study_group.add(Student('Sourabh', 3, 100, 50, 60))
#study_group.print_members()
#print(Group.members)
print("******")
#study_group.remove(5)
#study_group.print_members()
print("********")

study_group = Group()
study_group.add(Student('Lathika', 1, 80, 80, 80))
study_group.add(Student('Keerthana', 2, 80, 70, 60))
study_group.add(Student('Sourabh', 3, 75, 85, 80))
study_group.add(Student('Nikhil', 4, 100, 79, 59))
study_group.pick_leader()
print(study_group.leader)