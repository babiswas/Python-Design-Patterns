import copy

class Prototype:
   def __init__(self):
       self.objects={}
   def register(self,name,obj):
     if name not in self.objects:
       self.objects[name]=obj
   def unregister(self,name):
     if name in self.objects:
        del self.objects[name]
   def clone(self,name,**kwargs):
      if name in self.objects:
         obj=copy.deepcopy(self.objects.get(name))
         obj.__dict__.update(kwargs)
         return obj

class Car:
   def __init__(self,name):
      self.name=name
   def __str__(self):
      return f"{self.name} is running"


if __name__=="__main__":
   car=Car("Merceedes")
   proto=Prototype()
   proto.register("car",car)
   obj=proto.clone("car",test="test1")
   print(obj)
   


