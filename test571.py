class Myclass:
   name="Hello"
   def __init__(self,a,b):
      self.a=a
      self.b=b
   def __str__(self):
      return f"{self.a} and {self.b}"

   #def __str__(self):
      #return f"{self.a}"

   @property
   def set_a(self):
      return self.a
   @property
   def set_b(self):
      return self.b
   @set_a.setter
   def set_a(self,a):
      self.a=a
   @set_b.setter
   def set_b(self,b):
      self.b=b
   def __add__(self,other):
       if isinstance(other,Myclass):
          return self.a+other.a
       elif isinstance(other,int):
          return self.a+other
       else:
          return self.a

def add_Myclass():
   m=Myclass(2,3)
   n=Myclass(3,4)
   print(m+n)
   print(m)

if __name__=="__main__":
  add_Myclass()
  print(dir(add_Myclass))
  