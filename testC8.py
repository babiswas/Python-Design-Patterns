class A:
  """Hello class"""

  name="hello"

  def __init__(self,a):
     self.a=a
  def __str__(self):
     return f"{self.a} is the value"
  def fun(self):
      return f"{self.fun.__name__} called"
  @classmethod
  def fun1(self):
     print("Class method called")

if __name__=="__main__":
   a=A(2)
   print(a)
   print(a.fun())
   A.fun1()
   print(A.name)
   print(a.__doc__)
   print(a.__dict__)
   print(dir(a))
   print("New way")
   print(A.fun(a))
   A.fun1()
   