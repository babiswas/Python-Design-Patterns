class A:
   def __init__(self,a,b):
      self.a=a
      self.b=b
   def __str__(self):
      return f"{self.a} and {self.b}"
   def __call__(self):
      setattr(self,'c',12)

if __name__=="__main__":
   a=A(21,32)
   print(a.__dict__)
   print(a)
   a()
   print(a.__dict__)