class Director:
   def __init__(self,builder):
      self.builder=builder

   def construct_car(self):
       self.builder.get_car()
       self.builder.add_name()
       self.builder.add_model()
       self.builder.add_engine()

   def get_car(self):
      return self.builder.car

class Builder:
   def __init__(self):
     self.car=None
   def get_car(self):
     self.car=Car()
     

class Car_Builder(Builder):
   def add_name(self):
      self.car.name="Merceedes"
   def add_model(self):
      self.car.model="Brand New"
   def add_engine(self):
      self.car.engine="Engine added"
      

class Car:
   def __init__(self):
      self.name=''
      self.model=''
      self.engine=''
   def __str__(self):
      return f"{self.name}|{self.model}|{self.engine}"

if __name__=="__main__":
   builder=Car_Builder()
   dir=Director(builder)
   dir.construct_car()
   obj=dir.get_car()
   print(obj)
   
