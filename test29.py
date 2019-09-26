from abc import ABC,abstractmethod

class Component:
   def __init__(self,name):
      self.name=name
   @abstractmethod
   def component_function(self):
        pass

class Child(Component):
   def __init__(self,name):
      Component.__init__(self,name)
      self.name=name
   def component_function(self):
      print(f"{self.name}")

class Composite(Component):
     def __init__(self,name):
        Component.__init__(self,name)
        self.objects=[]
     def register(self,obj):
         self.objects.append(obj)
     def unregister(self,obj):
         self.objects.remove(obj)
     def component_function(self):
        print(f"{self.name}")
        for obj in self.objects:
            obj.component_function()

if __name__=="__main__":
   comp1=Composite("submenu1")
   ch1=Child("ss menu1")
   ch2=Child("ss menu2")
   comp1.register(ch1)
   comp1.register(ch2)
   comp2=Composite("menu2")
   comp2.register(comp1)
   comp2.component_function()
   
   


        
