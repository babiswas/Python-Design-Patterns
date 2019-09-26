import time

class Producer:
   def producer(self):
      return f"{self.producer.__name__} executing"
   def meet(self):
      return f"{self.producer.__name__} can meet now"

class Proxy:
   def __init__(self):
      self.producer=None
      self.occupied="No"
   def produce(self):
      if self.occupied=="No":
         self.producer=Producer()
         time.sleep(2)
         self.producer.meet()
      else:
         print("Producer is busy")
         time.sleep(2)

if __name__=="__main__":
   prox=Proxy()
   prox.produce()
   prox.occupied="Yes"
   time.sleep(3)
   prox.produce()

   
         

