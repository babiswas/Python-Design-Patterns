import types

def stra_1(self):
    print(f"{self.name} executing {stra_1.__name__}")

def stra_2(self):
    print(f"{self.name} executing {stra_2.__name__}")

class Strategy:
    def __init__(self,function=None):
        self.name="Default Strategy"
        if function:
           self.func=types.MethodType(function,self)

    def func(self):
        print(f"{self.name} running {self.func.__name__}")

if __name__=="__main__":
   st=Strategy()
   st.func()
   st=Strategy(stra_2)
   st.name="hello"
   st.func()
   bt=Strategy(stra_1)
   bt.name="bello"
   bt.func()

