def decorate(cls):
   def fun(*args):
      return cls(*args)
   return fun

@decorate
class B:
  def __init__(self,a,b):
      self.a=a
      self.b=b
  def __str__(self):
      return f"{self.a} and {self.b}"

if __name__=="__main__":
   b=B(2,3)
   print(b)