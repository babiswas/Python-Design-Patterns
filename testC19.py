class A:
  def __new__(cls,*args):
    print("New method executed")
    return object.__new__(cls)

  def fun(self):
    print(f"{fun.__name__} executed")

  def __str__(self):
     return f"{self.a},{self.b},{self.c} executed"

  def __init__(self,*args):
    print("Init method executed")
    self.a=args[0]
    self.b=args[1]
    self.c=args[2]

if __name__=="__main__":
   a=A(1,2,3)
   print(a)
   
   