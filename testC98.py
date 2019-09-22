class Observable:
   def __init__(self):
      self.observers=[]
   def attach(self,obj):
      if obj not in self.observers:
          self.observers.append(obj)
   def dettach(self,obj):
       if obj in self.observers:
           self.observers.remove(obj)
   def notify(self,message):
      for i in self.observers:
         i.update(message)

class Observer:
    def __init__(self,name):
         self.name=name
    def update(self,message):
        print(f"{self.name} recieved {message}")

if __name__=="__main__":
   o1=Observer("Jenny")
   o2=Observer("Jennifer")
   o=Observable()
   o.attach(o1)
   o.attach(o2)
   o.notify("hello ")



