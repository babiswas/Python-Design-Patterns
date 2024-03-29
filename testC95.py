class Component:
   def __init__(self,*args,**kwargs):
       pass
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
       self.children=[]

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
   subc1=Child("comp submenu1")
   subc2=Child("comp submenu2")
   sub1.append_child(subc1)
   sub1.append_child(subc2)
   top=Composite("top menu")
   sub2=Child("submenu2")
   top.append_child(sub1)
   top.append_child(sub2)
   top.component_function()

#top menu
#sub menu1
#
   

  