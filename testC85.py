import copy

class Prototype:
    def __init__(self):
       self.objects={}

    def register(self,name,obj):
      self.objects[name]=obj

    def unregister(self,name):
      del self.objects[name]

    def clone(self,name,**kwargs):
       obj=copy.deepcopy(self.objects.get(name))
       obj.__dict__.update(kwargs)
       return obj

class Car:
    def __init__(self,name):
       self.name=name
    def __str__(self):
       return f"{self.name} is running"

if __name__=="__main__":
   prototype=Prototype()
   car=Car("Maruti")
   car1=Car("Merceedes")
   prototype.register("maruti",car)
   prototype.register("merceedes",car1)
   m=prototype.clone("maruti",wheel=4,door=5)
   print(m)
   m=prototype.clone("merceedes",wheel=4,door=5)
   print(m)
   
    
   
        