#Dynamically changing the behaviour of an object.
#Types module support dynamic creation of new types.

import types

class Strategy:
   def __init__(self,function=None):
      self.name="Default Strategy"
      if function:
         self.execute=types.MethodType(function,self)

   def execute(self):
      print("Hello")
      print(f"{self.name} is used")


def strategy_one(self):
    print("Bello")
    print(f"{self.name} is used to create method1")

def strategy_two(self):
    print("Mello")
    print(f"{self.name} is used to create method2")

s0=Strategy()
s0.execute()
s1=Strategy(strategy_one)
s1.name="Strategy One"
s1.execute()
s2=Strategy(strategy_two)
s2.name="Strategy Two"
s2.execute()


