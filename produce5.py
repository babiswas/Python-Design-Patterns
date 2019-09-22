import time

class Producer:
   def producer(self):
     return print(f"producer is busy")
   def meet(self):
     return print(f"producer can meet now")


class Proxy:
   def __init__(self):
       self.occupied="No"
       self.producer=None
   def produce(self):
       if self.occupied=="No":
          self.producer=Producer()
          time.sleep(2)
          self.producer.meet()
       else:
          print("Producer is busy")
          time.sleep(2)

if __name__=="__main__":
   p=Proxy()
   p.produce()
   p.occupied="yes"
   p.produce()

   


