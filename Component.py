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
     def component_function(self):
         return f"{self.name}"

class Composite(Component):
     def __init__(self,name):
        Component.__init__(self,name)
        self.objects=[]
     def add_component(self,obj):
         self.objects.append(obj)
     def remove_component(self,obj):
         self.objects.remove(obj)
     def component_function(self):
         print(f"{self.name}")
         for obj in self.objects:
             obj.component_function()

if __name__=="__main__":
   comp=Composite("Submenu")
   ch1=Child("sub submenu1")
   ch2=Child("sub submenu2")
   comp.add_component(ch1)
   comp.add_component(ch2)
   comp1=Composite("MainMenu")
   comp1.add_component(comp)
   comp1.component_function()

  
     