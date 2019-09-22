class Myclass:
   def __init__(self,a):
      self.a=a
   def __str__(self):
      return f"{self.a} is value"
   def __add__(self,other):
       if isinstance(other,Myclass):
         return self.a+other.a
   def __radd__(self,other):
      print("reverse addition executing")
      return other+self.a

if __name__=="__main__":
   a=Myclass(2)
   print(6+a)
   print(a)
   print(a+11)
   b=Myclass(12)
   print(a+b)

