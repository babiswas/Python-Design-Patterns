import copy

class Prototype:
   def __init__(self):
     self.objects={}
   def register_object(self,name,obj):
     self.objects[name]=obj
   def unregister_object(self,name):
     del self.objects[name]
   def clone(self,name,**args):
     obj=copy.deepcopy(self.objects[name])
     obj.__dict__.update(args)
     return obj

class Car:
   def __init__(self):
      self.name="Skylark"
      self.color="Red"
      self.options="Ex"
   def __str__(self):
      return f"{self.name},{self.color},{self.options}"

c=Car()
prototype=Prototype()
prototype.register_object('skylark',c)
c1=prototype.clone('skylark')
print(c1)
