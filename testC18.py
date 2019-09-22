class Person:
   def __init__(self,id,name):
       self.id=id
       self.name=name
   def is_employee(self):
     return False
   def getname(self):
     return "{self.name} is the name executed by {Person.__name__}"
class Employee(Person):
   def __init__(self,id,name,profile):
       super().__init__(id,name)
       self.profile=profile
   def is_employee(self):
      return True
   def getname(self):
      return f"{self.name},{self.id},{self.profile} is person details executed by {Employee.__name__}"

if __name__=="__main__":
   l=[Person(21,"Hello"),Employee(32,"Tello","Engineeer"),Employee(32,"Tello","Engineeer"),Person(21,"Hello")]
   for i in l:
     print(i.is_employee())
     print(i.getname())