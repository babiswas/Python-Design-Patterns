from abc import ABC,abstractmethod

class Pet:
   @abstractmethod
   def speak(self):
      pass
   @abstractmethod
   def have_food(self):
      pass

class Dog(Pet):
    def __init__(self,name="Dog"):
        self.name=name

    def speak(self):
       return f"{self.name} bow bow"
  
    def __str__(self):
       return f"{self.name}"

    def have_food(self):
       return f"{self.name} eat flesh"

    def set_name(self):
       self.name=name


class Cat(Pet):
   def __init__(self,name="Cat"):
      self.name=name
   def speak(self):
      return f"{self.name} mew mew"
   def have_food(self):
      return f"{self.name} have milk"
   def set_name(self,name):
       self.name=name
   def __str__(self):
      return f"{self.name}"

class Dog_factory:
    def get_pet(self):
        return Dog("Dog")
    

class Cat_factory:
    def get_pet(self):
       return Cat("Cat")


class Pet_factory:
    def __init__(self,pet_factory=None):
        self.pet_factory=pet_factory

    def get_your_pet(self):
       pet=self.pet_factory.get_pet()
       pet_name=f"{pet} is pet name"
       print(pet.speak())
       print(pet.have_food())
       pet.set_name("Holly Maclain")
       print(pet_name)

if __name__=="__main__":
   cat_factory=Cat_factory()
   factory=Pet_factory(cat_factory)
   factory.get_your_pet()
   








   