class A:
  def __new__(cls,*args):
     print("New method executed")
     return object.__new__(cls)
  def __init__(self,a):
      print("init method executed")
      self.a=a
  def __str__(self):
      return f"{self.a} is value"

if __name__=="__main__":
   a=A(2)
   print(a)
     