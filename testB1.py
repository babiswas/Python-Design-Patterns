class A:
  def __init__(self,a):
    self.a=a
  def __call__(self):
    def fun(a):
      print(f"{a} is value")
    setattr(self,'hello',fun)

if __name__=="__main__":
  a=A(3)
  a()
  a.hello(2)
