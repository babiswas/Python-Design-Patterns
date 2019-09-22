from abc import ABC,abstractmethod

class B(ABC):
   @abstractmethod
   def fun(self):
      pass
   @abstractmethod
   def fun1(self):
      pass

class C(B):
  def fun(self):
     print(f"{self.fun.__name__} executing")
  def fun1(self):
     print(f"{self.fun1.__name__} executing")

if __name__=="__main__":
  c=C()
  c.fun()
  c.fun1()
