#This is an expensive object

import time

class Producer:
   def producer(self):
     return f"Producer is busy"
   def meet(self):
     return f"Producer can meet now"

class Proxy:
   def __init__(self):
       self.occupied="No"
       self.producer=None
   def produce(self):
       if occupied=="No":
         self.producer=Producer()
         time.sleep(2)
         self.producer.meet()
       else:
         print("Producer is easy")
         time.sleep(4)

if __name__=="__main__":
   p=Proxy()
   p.produce()
   p.occupied="yes"
   p.produce()

         
