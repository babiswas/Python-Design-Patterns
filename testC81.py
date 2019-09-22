class Borg:
   value={}
   def __init__(self):
      self.__dict__=self.value

class Singleton(Borg):
    def __init__(self,**kwargs):
       Borg.__init__(self)
       self.value.update(kwargs)

    def __str__(self):
       return str(self.value)

if __name__=="__main__":
   x=Singleton(hello="Bello")
   print(x)
   x=Singleton(fello="Fello")
   print(x)
   