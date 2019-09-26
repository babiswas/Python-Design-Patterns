import time

#Producer
class Producer:
   def producer(self):
      print("Producer is working")
   def meet(self):
      print("Producer will meet now")

#Proxy
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
         time.sleep(3)

if __name__=="__main__":
   proxy=Proxy()
   proxy.produce()
   proxy.occupied="yes"
   proxy.produce()
