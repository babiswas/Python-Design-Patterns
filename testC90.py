class A:
  def display(self):
     return f"Displayed"

class Mymeta(type):
    def __new__(metaclass,classname,baseclass,attr):
        attr['hello']=A.__dict__['display']
        return type.__new__(metaclass,classname,baseclass,attr)
    def __init__(self,classname,baseclass,attr):
        pass

class C(metaclass=Mymeta):
    def __init__(self):
        self.a=2
    def get_a(self):
      return self.a

if __name__=="__main__":
   a=C()
   print(a.hello())