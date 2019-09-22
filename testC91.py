class Dummy:
   def fun(self,*args):
      for i in args:
         print(i)

   def fun1(self):
     print(f"{self.fun1.__name__} is function name")

   def __getattribute__(self,attr):
       print(attr)
       return "Hello"


if __name__=="__main__":
   d=Dummy()
   print(d.fun)
   print(d.fun1)
       