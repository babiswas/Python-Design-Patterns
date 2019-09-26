class Director:
   def __init__(self,builder):
      self.builder=builder

   def construct_obj(self):
      self.builder.get_object()
      self.builder.add_part1()
      self.builder.add_part2()
      self.builder.add_part3()

   def show_obj(self):
       return f"{self.builder.obj}"

class Builder:
   def __init__(self):
      self.obj=''
   def get_object(self):
      self.obj=Obj()

class Obj_builder(Builder):
   def add_part1(self):
      self.obj.part1="part1"
   def add_part2(self):
      self.obj.part2="part2"
   def add_part3(self):
      self.obj.part3="part3"
     
    
class Obj:
   def __init__(self):
      self.part1=''
      self.part2=''
      self.part3=''
   def __str__(self):
      return f"{self.part1}|{self.part2}|{self.part3}"

if __name__=="__main__":
   builder=Obj_builder()
   dir=Director(builder)
   dir.construct_obj()
   print(dir.show_obj())

