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
       print(f"{self.name} Mew Mew")
   def having_food(self):
       print(f"{self.name} having milk")

class Dog(Pet):
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(f"{self.name} bow bow")
    def having_food(self):
        print(f"{self.name} having meat")

def get_pet(pet="cat"):
   pets=dict(cat=Cat("Meww"),dog=Dog("Bow Bow"))
   return pets[pet]

if __name__=="__main__":
   while True:
       try:
          key=input("Enter key")
          obj=get_pet(key)
          obj.speak()
          obj.having_food()
       except Exception as e:
          print("Invalid key entered")
  
       
