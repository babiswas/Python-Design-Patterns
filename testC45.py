class Dog:
   def speak(self):
       return "Woof!"
   def __str__(self):
       return "Dog"

class DogFactory:
   def get_pet(self):
      return Dog()
   def get_food(self):
      return "Dog food"


class PetStore:
   def __init__(self,pet_factory=None):
      self.pet_factory=pet_factory
   def show_pet(self):
      pet=self.pet_factory.get_pet()
      pet_food=self.pet_factory.get_food()
      print(f"Our pet is {pet}")
      print(f"Our pet says {pet.speak()}")
      print(f"Its food is {pet_food}")

factory=DogFactory()
shop=PetStore(factory)
shop.show_pet()

