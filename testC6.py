class A:
   def __init__(self,start,limit):
      self.start=start
      self.limit=limit
      self.x=0
   def __iter__(self):
      self.x=self.start
      return self
   def __next__(self):
     x=self.x
     if x>self.limit:
         raise StopIteration
     self.x=self.x+1
     return x

if __name__=="__main__":
   a=A(0,10)
   print(a.__next__())
   print(a.__next__())
   print(a.__next__())
   print(a.__next__())
   print(a.__next__())
   print(a.__next__())
   print(a.__next__())
   print(a.__next__())
   print(a.__next__())
   print(a.__next__())
   print(a.__next__())
   print(a.__next__())
   print(a.__next__())
   print(a.__next__())
   print(a.__next__())
   print(a.__next__())
