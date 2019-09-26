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
      self.name=name
   def speak(self):
     return f"{self.name} Mew"
   def have_food(self):
     return f"{self.name} having Milk"
   def __str__(self):
      return f"{self.name} drinking milk"

class Dog(Pet):
   def __init__(self,name):
      self.name=name
   def speak(self):
     return f"{self.name} bow"
   def have_food(self):
     return f"{self.name} have meat"
   def __str__(self):
      return f"{self.name} eat meat"

class DogFactory:
   def get_pet(self):
      return Dog("doggy")

class CatFactory:
   def get_pet(self):
     return Cat("Mew")

class PetFactory:
   def __init__(self,pet_fact=None):
      self.pet_fact=pet_fact
   def get_pets(self):
      if self.pet_fact:
         pet=self.pet_fact.get_pet()
         print(pet)
         print(pet.speak())
         print(pet.have_food())

if __name__=="__main__":
  dog=DogFactory()
  petf=PetFactory(dog)
  petf.get_pets()

           