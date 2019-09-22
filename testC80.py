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
      return f"{self.name} bow bow"
   def have_food(self):
      return f"{self.name} have flesh"
   def __str__(self):
       return f"{self.name} is dog name"

class Cat(Pet):
   def __init__(self,name):
       self.name=name
   def speak(self):
      return f"{self.name} mew mew"
   def have_food(self):
      return f"{self.name} have milk"
   def __str__(self):
      return f"{self.name} is cat name"

class DogFactory:
   def get_pet(self):
      return Dog("doggy")

class CatFactory:
   def get_pet(self):
      return Cat("meww")

class Pet_factory:
   def __init__(self,pet_factory=None):
      self.pet_fact=pet_factory
   def pet_act(self):
      pet=self.pet_fact.get_pet()
      pet_speak=pet.speak()
      pet_food=pet.have_food()
      print(f"{pet} is the pet name")
      print(f"{pet_food} is pet food")
      print(f"{pet_speak} is pet speak")

dog_factory=DogFactory()
m=Pet_factory(dog_factory)
m.pet_act()

cat_factory=CatFactory()
m=Pet_factory(cat_factory)
m.pet_act()










