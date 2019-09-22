#Implementation dependent
class DrawingAPIOne:
    def draw_circle(self,x,y,radius):
        print(f"API 1 for drawing circle {x},{y} with radius {radius}")

#Implementation dependent
class DrawingAPITwo:
    def draw_circle(self,x,y,radius):
        print(f"API 2 for drawing circle {x},{y} with radius {radius}")


#Implementation Indipendent class
class Circle:
    def __init__(self,x,y,radius,drawing_api):
        self.x=x
        self.y=y
        self.radius=radius
        self.draw_api=drawing_api

    def draw(self):
       self.draw_api.draw_circle(self.x,self.y,self.radius)

    def scale(self,percent):
        self.radius*=percent


if __name__=="__main__":
   circle=Circle(1,2,3,DrawingAPIOne())
   circle.draw()
   circle=Circle(1,2,3,DrawingAPITwo())
   circle.draw()


       