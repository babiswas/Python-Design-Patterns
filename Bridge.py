class DrawingAPIOne:

    def draw_circle(self,x,y,radius):
        print(f"API 1 drawing circle {x} {y} {radius}")

class DrawingAPITwo:

    def draw_circle(self,x,y,radius):
        print(f"API 1 drawing circle {x} {y} {radius}")


class Circle:
    def __init__(self,x,y,radius,drawing_api):
       self.x=x
       self.y=y
       self.radius=radius
       self.drawing_api=drawing_api

    def draw(self):
       self.drawing_api.draw_circle(self.x,self.y,self.radius)    

    def scale(self,percent):
       self.radius=percent


if __name__=="__main__":
   circle1=Circle(1,2,3,DrawingAPIOne())
   circle1.draw()
   circle2=Circle(2,3,4,DrawingAPITwo())
   circle2.draw()



