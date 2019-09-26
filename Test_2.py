class House:
    def accept(self,visitor):
       visitor.visit(self)
    def work_on_hvac(self,hvac_specialist):
       print(self,"work on by",hvac_specialist)
    def work_on_electricity(self,electrician):
       print(self,"Work on by",electrician)
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

if __name__=="__main__":
   el=Electrician()
   hv=HvacSpecialist()
   home=House()
   home.accept(el)
   home.accept(hv)
   

