class A:
  __name="hello12"
  def __init__(self):
    self.__a=12
  def __str__(self):
     return f"{self.__a} is the value of a"
  def __fun(self):
     return f"{self.__a} is the value of a"

if __name__=="__main__":
   a=A()
   print(a)
   print(a._A__fun())
   print(A._A__name)
   print(a._A__a)
  