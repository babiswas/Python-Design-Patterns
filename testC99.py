class House:
  def accept(self,visitor):
      visitor.visit(self)

  def work_on_hvac(self,hvac_spclst):
      print(self,"worked by",hvac_spclst)

  def work_on_electricity(self,electrcn):
     print(self,"Worked on by",electrcn)

  def __str__(self):
     return self.__class__.__name__


class Visitor:
   def __str__(self):
      return self.__class__.__name__



class HvacSpecialist(Visitor):
   def visit(self,house):
      house.work_on_hvac(self)


class Electrician(Visitor):
   def visit(self,house):
     house.work_on_electricity(self)


hv=HvacSpecialist()
e=Electrician()
home=House()
home.accept(hv)
home.accept(e)





