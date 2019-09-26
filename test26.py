def function(cls):
   print(f"{function.__name__} is executing")
   def wrapper(*args):
     print(f"{wrapper.__name__} executed")
     return cls(*args)
   return wrapper


@function
class B:
  def __init__(self,name):
      self.name=name
  def func(self):
     return f"{self.func.__name__} executed"

if __name__=="__main__":
   print("Main Bloc")
   b=B("hello")
   print(b.func())
