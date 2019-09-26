class Observable:
   def __init__(self):
      self.objects=[]

   def register(self,obj):
      self.objects.append(obj)

   def unregister(self,obj):
       if obj in self.objects:
           self.objects.remove(obj)

   def notify(self,message):
      for obj in self.objects:
          print(obj.update(message))

class Observer:
    def __init__(self,name):
       self.name=name
    def update(self,message):
       return f"{self.name} recieved {message}"

if __name__=="__main__":
   ob1=Observer("John")
   ob2=Observer("Jani")
   ob=Observable()
   ob.register(ob1)
   ob.register(ob2)
   ob.notify("Hello")

   
       