def decorator(cls):
   def wrapper(*args):
     print("Wrapper executed")
     return cls(*args)
   return wrapper

@decorator
class A:
   def __init__(self,name):
       self.name=name
   def __str__(self):
      return f"{self.name} is name"

if __name__=="__main__":
   a=A("hello")
   print(a)
      