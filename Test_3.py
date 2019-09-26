class Bors:
   values={}
   def __init__(self):
      self.__dict__=self.values

class Singleton(Bors):
   def __init__(self,**kwargs):
      Bors.__init__(self)
      self.__dict__.update(kwargs)
   def __str__(self):
      return f"{self.__dict__}"

if __name__=="__main__":
   s1=Singleton(test="test1")
   print(s1)
   s2=Singleton(test1="test2")
   print(s1)
   print(s2)
   s3=Singleton(test3="test2")
   print(s1)
   print(s2)
   print(s3)


     