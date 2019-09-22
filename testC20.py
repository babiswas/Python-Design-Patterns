class A(Exception):
   def __init__(self,name):
     self.name=name
     print("Init method executed")
   def __str__(self):
     return f"{self.name} Exception occoured {A.__name__}"

if __name__=="__main__":
   try:
     raise A("Throw")
   except Exception as e:
     print(e)