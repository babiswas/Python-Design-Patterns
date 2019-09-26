class A:
  def __init__(self,func):
      print("Init function executed")
      self.func=func
  def __call__(self,*args):
      print("Call function executed")
      return self.func(*args)

@A
def func(*args):
  for i in args:
      print(i)


if __name__=="__main__":
   func(2,3,4,5,6,7)
   