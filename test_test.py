from abc import ABC,abstractmethod

class Component:
   @abstractmethod
   def component_function(self):
        pass


class Child(Component):
   def __init__(self,name):
      Component.__init__(self,name)
      self.name=name

   def component_function(self):
       return f"{self.name}"

class Composite(Component):
    def __init__(self,name):
       Component.__init__(self,name)
       self.name=name
       self.objects=[]
    def add_component(self,obj):
       self.objects.append(obj)
    def remove_component(self,obj):
       self.objects.remove(obj)
    def component_function(self):
       print(f"{self.name}")
       for obj in self.objects:
           obj.speak()


if __name__=="__main__":
   sub1=Composite("Sub menu")
   ch1=Child("sub sub menu1")
   ch2=Child("sub sub menu2")
   sub1.add_component(ch1)
   sub1.add_component(ch2)
   top=Composite("Menu")
   top.add_component(sub1)
   top.component_function()
       