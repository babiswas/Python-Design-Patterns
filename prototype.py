class Prototype:
   def __init__(self):
      self.objects={}
   def register(self,name,obj):
       self.objects[name]=obj
   def unregister(self,name):
    if name in self.objects:
       del self.objects[name]
   def clone(self,name,**args):
      m=self.objects.get(name)
      m.__dict__.update(args)
      return m

class Car:
    def __init__(self,name):
       self.name=name
    def run_car(self):
       return f"{self.name} is running"


if __name__=="__main__":
   prototype=Prototype()
   car=Car("Merceedes")
   prototype.register("car1",car)
   n=prototype.clone("car1",wheels=2,mudguard=1)
   print(n.run_car())

   
      