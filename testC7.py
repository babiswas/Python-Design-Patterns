class A:
   def __init__(self,limit):
      self.limit=limit
   def __iter__(self):
      self.x=12
      return self
   def __next__(self):
      x=self.x
      if x>self.limit:
         raise StopIteration
      self.x=self.x+1
      return x


if __name__=="__main__":
    a=A(30)
    for i in a:
      print(i)
      