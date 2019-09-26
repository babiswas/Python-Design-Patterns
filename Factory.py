from abc import ABC,abstractmethod

class Pet:
   @abstractmethod
   def speak(self):
      pass
   @abstractmethod
   def have_food(self):
       pass

class Cat(Pet):
   def __init__(self,name):
      self.__name__=name
   def speak(self):
       return f"{self.__name__} Mew Mew"

   def have_food(self):
      return f"{self.__name__} having milk"

class Dog(Pet):
   def __init__(self,name):
      self.__name__=name
   def speak(self):
      return f"{self.__name__} Bow Bow"
   def have_food(self):
      return f"{self.__name__} having Flesh"

def get_object(pet="cat"):
   pets=dict(cat=Cat("mew"),dog=Dog("doggy"))
   return pets[pet]

if __name__=="__main__":
   while True:
     try:
        key=input("Enter the key:")
        obj=get_object(key)
        print(obj.speak())
        print(obj.have_food())
     except Exception as e:
        print(f"Invalid key {key} entered")
        


      
   

