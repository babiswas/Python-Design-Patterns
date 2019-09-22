class A:
   def __init__(self,*args):
       self.a=args[0]
   def fun(self):
      print(f"{self.fun.__name__} is executed by {A.__name__}")
   def __str__(self):
      return f"{self.a} is the value"

class B(A):
   def __init__(self,*args):
      super().__init__(*args)
      self.b=args[1]
   def fun(self):
      print(f"{B.__name__} is executing {self.fun.__name__}")
   def __str__(self):
      return f"{self.a},{self.b} are the values"


if __name__=="__main__":
   a=A(12)
   print(a)
   a.fun()
   b=B(12,13)
   print(b)
   b.fun()
   print(isinstance(b,B))
   print("Is a isnatnce of A")
   print(isinstance(a,A))
   print("Is B subclass of A")
   print(issubclass(B,A))


  
      
      
