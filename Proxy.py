import time

class Producer:
   def meet(self):
     print("Producer can meet now")

   def producer(self):
     print("Producer is busy")


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
  pro=Proxy()
  pro.produce()
  pro.occupied="yes"
  pro.produce()

  
    
        