from abc import ABC,abstractmethod

class Pet:
   @abstractmethod
   def speak(self):
      pass
   @abstractmethod
   def have_food(self):
      pass

class Dog(Pet):
   def __init__(self,name):
      self.name=name
   def speak(self):
       return f"{self.name} Bow Bow"
   def have_food(self):
       return f"Having Flesh"
   def set_name(self,name):
       self.name=name

class Cat(Pet):
   def __init__(self,name):
      self.name=name
   def speak(self):
      return f"{self.name} Mew Meww"
   def have_food(self):
      return f"Having Milk"
   def set_name(self,name):
      self.name=name

def get_objects(pet="cat"):
   pets=dict(dog=Dog("doggy"),cat=Cat("Pussy"))
   return pets[pet]

if __name__=="__main__":
   while True:
      try:
         enter_key=input("Enter the key")
         obj=get_objects(enter_key)
         print(obj.speak())
         print(obj.have_food())
         enter_name=input("enter name:")
         obj.set_name(enter_name)
         print(obj.speak())
      except Exception as e:
         print("Invalid key entered")
      