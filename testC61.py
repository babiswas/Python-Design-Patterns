class Director:
   def __init__(self,builder):
      self.builder=builder

   def construct_a(self):
     self.builder.create_a()
     self.builder.add_name()
     self.builder.add_tire()
     self.builder.add_engine()
     

   def get_a(self):
      return self.builder.a

class Builder:
   def __init__(self):
      self.a=''
   def create_a(self):
      self.a=Car()
   

class Obj_builder(Builder):
   def add_name(self):
      self.a.name="Merceedes"
   def add_tire(self):
      self.a.tires="Ralco"
   def add_engine(self):
      self.a.engine="Engine Added"
    

class Car:
  def __init__(self):
     self.name=''
     self.tires=''
     self.engine=''

  def __str__(self):
     return f"{self.name}|{self.tires}|{self.engine}"

if __name__=="__main__":
   builder=Obj_builder()
   d=Director(builder)
   d.construct_a()
   m=d.get_a()
   print(m)
