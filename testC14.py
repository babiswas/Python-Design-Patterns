class A:
  def __init__(self,a):
      self.a=a
  def __str__(self):
     return f"{self.a} is the value"
  def fun(self):
     return f"{A.__name__} is executing {self.fun.__name__}"

class C:
  def __init__(self,c):
     self.c=c
  def fun(self):
     return f"{C.__name__} is executing {self.fun.__name__}"
  def __str__(self):
     return f"{self.c} is the value"

class B(A,C):
  def __init__(self,*args):
    A.__init__(self,args[0])
    C.__init__(self,args[1])
    self.d=args[2]

  def __str__(self):
     return f"{self.a},{self.c},{self.d} are the values"

  def fun(self):
     return f"{B.__name__} is executing {self.fun.__name__}"
     

if __name__=="__main__":
  l=[A(2),C(3),B(1,5,6)]
  for i in l:
    print(i)
    print(hasattr(i,'fun'))
    print(i.fun())


   
