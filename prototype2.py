import copy

class Prototype:
   def __init__(self):
      self.objects={}
   def register(self,name,obj):
      self.objects[name]=obj
   def unregister(self,name):
      if name in self.objects:
        del self.objects[name]
   def clone(self,name,**kwargs):
      obj=copy.deepcopy(self.objects[name])
      obj.__dict__.update(kwargs)
      return obj

class Car:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f"{self.name} is running"

if __name__=="__main__":
   prototype=Prototype()
   car=Car("Matiz")
   prototype.register("car",car)
   m=prototype.clone("car",hest="best",mest="mest")
   print(m)
   