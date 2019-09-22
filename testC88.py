class Borg:
   values={}
   def __init__(self):
     self.__dict__=self.values

class Single(Borg):
   def __init__(self,**kwargs):
       Borg.__init__(self)
       self.values.update(kwargs)
   def __str__(self):
       return f"{self.values}"

if __name__=="__main__":
   b=Single(test1="test1")
   print(b)
   c=Single(test2="test2")
   print(c)