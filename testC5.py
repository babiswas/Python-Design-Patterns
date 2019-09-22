class A:
  def __init__(self,*args):
     print(f"{A.__name__} executed")
     self.a=args[0]
     self.b=args[1]
  def __str__(self):
     return f"{self.a} and {self.b} executed"

class B(A):
  def __init__(self,*args):
      super().__init__(*args)
      self.c=args[2]
      print(f"{B.__name__} executed")
  def __str__(self):
     return f"{self.a},{self.b} and {self.c} are the values"

if __name__=="__main__":
   b=B(1,2,3)
   print(b)