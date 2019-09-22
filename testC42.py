class A:
   _tes={}
   def __init__(self):
     self.__dict__=self._tes

class B(A):
   def __init__(self,**kwargs):
     A.__init__(self)
     self._tes.update(kwargs)
   def __str__(self):
     return str(self._tes)

x=B(bes="bello")
print(x)
y=B(nes="nello")
print(y)
z=B(bees="tello")
print(z)
