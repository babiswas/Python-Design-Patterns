from abc import ABC,abstractmethod

class Component:
   @abstractmethod
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

class Composite:
   def __init__(self,*args,**kwargs):
      Component.__init__(self,*args,**kwargs)
      self.children=[]
      self.name=args[0]
   def append_child(self,child):
      self.children.append(child)
   def remove_child(self,child):
      self.children.remove(child)
   def component_function(self):
      print(f"{self.name}")
      for i in self.children:
          i.component_function()

if __name__=="__main__":
   sub1=Composite("submenu1")
   subl1=Child("sub_submenu_1")
   subl2=Child("sub_submenu_2")
   sub1.append_child(subl1)
   sub1.append_child(subl2)
   sub1.component_function()


   
