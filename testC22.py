class A:
   """Hello World"""
   def __init__(self):
      self.a=2
      self.b=3
   def fun(self):
      return f"{self.fun.__name__} name of function"

if __name__=="__main__":
   print(f"{A.__name__}")
   print(A.__dict__)