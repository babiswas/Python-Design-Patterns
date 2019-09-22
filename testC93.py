class A:
   def __init__(self,a):
      self.a=a
   def display_a(self):
      return f"{self.a} is value"


class B:
   def __init__(self,obj):
      self.obj=obj
   def __getattr__(self,attr):
      return getattr(self.obj,attr)


if __name__=="__main__":
   obj=A(2)
   b=B(obj)
   print(f"{b.a} is value")
   print(f"{b.display_a()}")