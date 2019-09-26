import copy

class Prototype:
   def __init__(self):
      self.objects={}
   def register(self,name,obj):
       if name not in self.objects:
          self.objects[name]=obj
   def unregister(self,name):
       if name not in self.objects:
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
   proto=Prototype()
   car1=Car("Merceedes")
   car2=Car("Matiz")
   proto.register("car1",car1)
   proto.register("car2",car2)
   obj=proto.clone("car2",test1="test2",test3="test3")
   print(obj)
   obj2=proto.clone("car1",test4="test4")
   print(obj2)
   print(obj2.__dict__)
   
          
      
        