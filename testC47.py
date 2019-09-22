from abc import ABC,abstractmethod

class Pet:
   @abstractmethod
   def speak(self):
      pass


class Cat(Pet):
   def __init__(self,name="Pussy"):
      self.name=name
   def speak(self):
      return "Mew Mew"
   def __str__(self):
      return f"{self.name}"
   def pet_food(self):
       return "Cat Food"
   def set_name(self,name):
      self.name=name


class Dog(Pet):
   def __init__(self,name="Doggy"):
      self.name=name
   def speak(self):
      return "Bow Bow"
   def __str__(self):
      return f"{self.name}"
   def pet_food(self):
       return "Dog food"
   def set_name(self,name):
      self.name=name


class Dog_factory:
    def __init__(self):
       self.pet=None
    def get_pet(self):
       self.pet=Dog()
       return self.pet
    
    

class Cat_factory:
    def __init__(self):
        self.pet=None
    def get_pet(self):
        self.pet=Cat()
        return self.pet
   
class Pet_factory:
   def __init__(self,pet_factory=None):
       self.petfact=pet_factory
   def set_pet(self):
       pet=self.petfact.get_pet()
       pet_food=pet.pet_food()
       pet_sound=pet.speak()
       print(f"{pet} is pets name")
       print(f"{pet_sound} is pets sound")
       print(f"{pet_food} is pets food")
       name=input("enter pet name")
       pet.set_name(name)
       print(f"{pet} is pet name")

       

if __name__=="__main__":
   factory=Cat_factory()
   m=Pet_factory(factory)
   m.set_pet()

   

       

