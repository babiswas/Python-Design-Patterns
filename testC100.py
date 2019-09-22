class Dog:
  """A simple dog class"""
  def __init__(self,name):
     self.name=name
  def speak(self):
     return f"{self.name} Woof"

class Cat:
   """A simple cat class"""
   def __init__(self,name):
       self.name=name
   def speak(self):
      return f"{self.name} mew"

def get_pet(pet="dog"):
   """This is factory method to create objects"""
   pets=dict(dog=Dog("dog"),cat=Cat("cat"))
   return pets[pet]

if __name__=="__main__":
   while True:
     enter_pet=input("Enter Pet")
     m=get_pet(enter_pet)
     print(m.speak())