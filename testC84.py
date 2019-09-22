class A:
   values={}
   def __init__(self):
       self.__dict__=self.values

class B(A):

   def __init__(self,**args):
      A.__init__(self)
      self.values.update(args)

   def __str__(self):
      return f"{self.values}"

if __name__=="__main__":
   m=B(test="test1",mest="mest1",kest="kest1")
   print(m)
   n=B(lest="lest1")
   o=B(dest="dest2")
   p=B(jest="sest")
   for i in (m,n,o,p):
      print(i)