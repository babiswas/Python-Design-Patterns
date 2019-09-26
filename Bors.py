class Born:
  values={}
  def __init__(self):
     self.__dict__=self.values

class Singleton(Born):
   def __init__(self,**kwargs):
       Born.__init__(self)
       self.values.update(kwargs)
   def __str__(self):
      return f"{self.values}"

if __name__=="__main__":
   m=Singleton(name="Hello")
   print(m)
   n=Singleton(bame="Pello")
   print(n)
