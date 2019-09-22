class Cat:
   def __init__(self,name):
       self.name=name
   def speak(self):
      return f"{self.name} Mew Mew"
class Dog:
   def __init__(self,name):
      self.name=name
   def speak(self):
      return f"{self.name} Woof Woof"

def get_pet(pet="cat"):
   pets=dict(dog=Dog("Bow"),cat=Cat("pussy"))
   return pets[pet]

if __name__=="__main__":
  while True:
      enter_pet=input("Enter Dog:")
      m=get_pet(enter_pet)
      print(m.speak())