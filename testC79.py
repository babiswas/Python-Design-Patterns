#Factory Pattern
from abc import ABC,abstractmethod

class Pet:
   """Pet class"""

   @abstractmethod
   def speak(self):
       pass

   @abstractmethod
   def food(self):
      pass


class Cat:
   """Cat class"""

   def __init__(self,name="pussy"):
       self.name=name
   def speak(self):
       return f"{self.name} Mewww"
   def food(self):
       return f"drink milk"
   def print_doc(self):
       return f"{self.__doc__} is document"

class Dog:
   """Dog class"""

   def __init__(self,name="doggy"):
      self.name=name
   def speak(self):
      return f"{self.name} Bow Bow"
   def food(self):
      return f"Eat flesh"
   def print_doc(self):
       return f"{self.__doc__} is document"


class Cow:
   """Cow class"""

   def __init__(self,name="Coww"):
      self.name=name
   def speak(self):
      return f"{self.name} coww"
   def food(self):
      return f"Hambaa hambaa"
   def print_doc(self):
       return f"{self.__doc__} is document"



def get_pet(pet="cat"):
    pets=dict(cat=Cat(),dog=Dog(),cow=Cow())
    return pets[pet]


if __name__=="__main__":
   while True:
     try:
        key=input("Enter the key")
        print(get_pet(key).speak())
        print(get_pet(key).food())
     except Exception as e:
        print(f"Invalid key {key}")

      
      




