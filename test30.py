class DrawCircle1:
   def draw_circle(self,x,y,radius):
      print("API 1 is drawing circle")

class DrawCircle2:
   def draw_circle(self,x,y,radius):
      print("API 2 is drawing circle")

class Circle:
   def __init__(self,x,y,radius,object):
      self.x=x
      self.y=y
      self.radius=radius
      self.object=object
   def draw(self):
      self.object.draw_circle(self.x,self.y,self.radius)

if __name__=="__main__":
   c=Circle(2,3,4,DrawCircle1())
   c1=Circle(3,4,5,DrawCircle2())
   c.draw()
   c1.draw()

      