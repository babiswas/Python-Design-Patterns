class A:
  def __init__(self,a):
      self.a=a
  def __str__(self):
     return f"{self.a} is value of a"
class B(A):
   def __init__(self,a,b):
       self.a=a
       self.b=b
   def __str__(self):
       return f"{self.a},{self.b} is value of a and b"

if __name__=="__main__":
   a=A(2)
   b=B(12,13)
   print(a)
   print(b)
