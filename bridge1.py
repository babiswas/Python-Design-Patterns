class DrawCircle1:
    def draw_circle(self,x,y,radius):
       return f"Circle API 1 executed"

class DrawCircle2:
    def draw_circle(self,x,y,radius):
        return f"Circle API 2 executed"

class Circle:
    def __init__(self,x,y,radius,object):
        self.x=x
        self.y=y
        self.radius=radius
        self.object=object

    def draw(self):
       print(self.object.draw_circle(self.x,self.y,self.radius))
    def percentage(self):
        self.radius*=2

if __name__=="__main__":
   circ=Circle(2,3,4,DrawCircle1())
   circ.draw()
   circ2=Circle(4,5,6,DrawCircle2())
   circ2.draw()

       