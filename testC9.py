class A:
  name="hello"
  def __init__(self,a):
     self.a=a
  def __str__(self):
     return f"{self.a} is the value a"
  def fun(self):
     print(f"{self.a} is the value of object attribute")
  @classmethod
  def fun2(cls):
     print("Class method executed")

if __name__=="__main__":
   a=A(2)
   print(a)
   print(a.__dict__)
   A.fun(a)
   A.fun2()
