class Observable:
   def __init__(self):
       self.observer=[]
   def register(self,obj):
      if obj not in self.observer:
        self.observer.append(obj)
   def unregister(self,obj):
      if obj in self.observer:
        self.observer.remove(obj)
   def notify(self,message):
      for o in self.observer:
          o.update(message)

class Observer:
   def __init__(self,name):
       self.name=name
   def update(self,message):
      print(f"{self.name} recieved {message}")

if __name__=="__main__":
   o1=Observer("John")
   o2=Observer("Jani")
   c1=Observable()
   c1.register(o1)
   c1.register(o2)
   c1.notify("Hello")