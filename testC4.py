class A:
   def __init__(self,*args):
      print(f"{A.__name__} class executed")
      self.a=args[0]
      self.b=args[1]
   def __str__(self):
      return f"{self.a} and {self.b}"

class B(A):
   def __init__(self,*args):
       super().__init__(*args)
       self.c=args[2]
       print(f"{B.__name__} executed")

   def __str__(self):
      return f"{self.a},{self.b} and {self.c}"
       


if __name__=="__main__":
   m=B(1,2,3)
   print(m.__dict__)
   print(m)
   a=A(1,2)
   print(a.__dict__)
   print(a)

