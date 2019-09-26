from abc import ABC,abstractmethod

class Component:
   def __init__(self,*args,**kwargs):
      pass

   @abstractmethod
   def component_function(self):
       pass

class Child(Component):
   def __init__(self,*args,**kwargs):
      Component.__init__(self,*args,**kwargs)
      self.name=args[0]

   def component_function(self):
       print(f"{self.name}")

class Composite(Component):
   def __init__(self,*args,**kwargs):
      Component.__init__(self,*args,**kwargs)
      self.name=args[0]
      self.objects=[]

   def add_objects(self,obj):
      self.objects.append(obj)

   def remove_objects(self,obj):
      self.objects.remove(obj)
      
   def component_function(self):
      print(f"{self.name}")
      for obj in self.objects:
         obj.component_function()

if __name__=="__main__":
   sub1=Composite("Sub comp")
   ch1=Child("sub sub1")
   ch2=Child("sub sub2")
   sub1.add_objects(ch1)
   sub1.add_objects(ch2)
   top=Composite("Comp")
   top.add_objects(sub1)
   top.component_function()

   
   
   
   
   


   
       
   