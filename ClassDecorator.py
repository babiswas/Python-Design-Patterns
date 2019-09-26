class A:
  def __init__(self,fun):
      self.func=fun

  def __call__(self,*args):
      print("call function is executed")
      return self.func(*args)

@A
def func(*args):
  for i in args:
     print(i)

if __name__=="__main__":
   func(1,2,3,4)
