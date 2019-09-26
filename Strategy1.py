import types

class Strategy:
    def __init__(self,function=None):
        self.name="Default Strategy"
        if function:
          self.method=types.MethodType(function,self)
    def method(self):
       print("Hello")
       print(f"{self.name} is used")

def strategy_one(self):
    print("Bello")
    print(f"{self.name} is used to create method1")

def strategy_two(self):
    print("Mello")
    print(f"{self.name} is used to create method2")


if __name__=="__main__":
   st=Strategy(strategy_one)
   st.method()
   st=Strategy(strategy_two)
   st.name="Strategy Two"
   st.method()


        
       