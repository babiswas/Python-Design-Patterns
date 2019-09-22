from abc import ABC,abstractmethod

class Pet:
   @abstractmethod
   def speak(self):
      pass

class Dog:
   def __init__(self,name="Doggy"):
      self.name=name
   def speak(self):
      return "BowBow"
   def pet_food(self):
      return "Dogs food"
   def __str__(self):
      return f"{self.name}"

class Cat:
   def __init__(self,name="Mewwww"):
       self.name=name
   def speak(self):
       return f"Mew Mew"
   def pet_food(self):
       return "Cat's Milk"
   def __str__(self):
      return f"{self.name}"


class DogFactory:
   def get_pet(self):
     return Dog()

class CatFactory:
  def get_pet(self):
     return Cat()

class Pet_Factory:
    def __init__(self,pet_factory=None):
        self.pet=pet_factory
    def show_pet(self):
        pet=self.pet.get_pet()
        pet_food=pet.pet_food()
        pet_speak=pet.speak()
        print(f"{pet} is pet name")
        print(f"{pet_food} is pets food")
        print(f"{pet_speak} is pet sound")

dog_factory=DogFactory()
cat_factory=CatFactory()
shop=Pet_Factory(dog_factory)
shp=Pet_Factory(cat_factory)
shop.show_pet()
shp.show_pet()

  


