class learn():

  def __init__ (self, subject, id):
    self._subject = subject
    self._id = id

  def is_id():
    if self._subject = 'math':
      return True
    else:
      return False
      
user1 = learn(math, 2)
if user.is_id():
  print('very good!')

else:
  print("so bad!")
  
import time

while True:
    try:
        print('Hi')
        time.sleep(1)
    except:
        print('Bye')


class Employee:
   '所有员工的基类'
   empCount = 0
 
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount
 
   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary
