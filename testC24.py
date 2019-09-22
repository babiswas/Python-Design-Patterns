class A:
   def __init__(self,a):
      self.a=a
   def get_a(self):
     return f"{self.a} is value"

class Meta(type):
    def __new__(cls,classname,baseclass,attrs):
       attrs['func']=A.__dict__['get_a']
       return type.__new__(cls,classname,baseclass,attrs)
    def __init__(self,classname,baseclass,attrs):
        pass

class B(metaclass=Meta):
     def __init__(self,*args):
         self.a=args[0]
         self.b=args[1]

     def fun(self):
         return f"{self.a} and {self.b} are values"

if __name__=="__main__":
   b=B(1,2)
   print(b.fun())
   print(b.func())

   