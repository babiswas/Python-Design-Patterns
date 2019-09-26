from abc import ABC,abstractmethod

class Pet:
   @abstractmethod
   def speak(self):
     pass
   @abstractmethod
   def having_food(self):
     pass


class Cat(Pet):
   def __init__(self,name):
       self.name=name
   def speak(self):
     return f"{self.name} mew"
   def having_food(self):
     return f"{self.name} having food"
   def __str__(self):
       return f"{self.name}"

class Dog(Pet):
   def __init__(self,name):
      self.name=name
   def speak(self):
      return f"{self.name} Bow"
   def having_food(self):
      return f"{self.name} having food"
   def __str__(self):
       return f"{self.name}"



class CatFactory:
   def get_pet(self):
      return  Cat("Mew")

class DogFactory:
   def get_pet(self):
      return Dog("dog")


class PetFactory:
   def __init__(self,petfactory=None):
       self.petfactory=petfactory
   def get_pet_now(self):
       pet=self.petfactory.get_pet()
       print(pet)
       speak=pet.speak()
       food=pet.having_food()
       print(speak)
       print(food)

if __name__=="__main__":
   fact=DogFactory()
   m=PetFactory(fact)
   m.get_pet_now()