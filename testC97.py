import types

class Strategy:
   def __init__(self,function=None):
      self.name="Default Strategy"
      if function:
         self.execute=types.MethodType(function,self)
   def execute(self):
      print("Hello")
      print(f"{self.name} is used")


def strat_one(self):
    print("Bello")
    print(f"{strat_one.__name__} is used to create method {self.name}")

def strat_two(self):
   print("Mello")
   print(f"{strat_two.__name__} is to create method {self.name}")

if __name__=="__main__":
  s0=Strategy()
  s0.execute()
  s1=Strategy(strat_one)
  s1.execute()
  s2=Strategy(strat_two)
  s2.execute()



