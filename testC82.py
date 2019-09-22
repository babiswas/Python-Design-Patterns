#Singleton using Borgs design pattern.

class A:
   value={}
   def __init__(self):
      self.__dict__=self.value

class B(A):
   def __init__(self,**kwargs):
      A.__init__(self)
      self.value.update(kwargs)
   def __str__(self):
      return f"{self.value}"

if __name__=="__main__":
   a=B(test="hello")
   print(a)
   b=B(best="kello")
   c=B(mest="mello")
   print(a)
   print(c)

      