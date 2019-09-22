class Handler:
    def __init__(self,successor):
        self.successor=successor

    def handle(self,request):
         handled=self._handle(request)
         if not handled:
             self.successor.handle(request)

    def _handle(self,request):
       raise NotImplementedError("Not implemented")


class ConcreteHandler(Handler):
    def _handle(self,request):
       if 0<request<=10:
          print(f"Request {request} handled in handler1")
          return True

class DefaultHandler(Handler):
    def _handle(self,request):
      print(f"End of chain ,no handler for {request}")
      return True

class Client:
   def __init__(self):
      self.handler=ConcreteHandler(DefaultHandler(None))

   def delegate(self,request):
     for request in requests:
        self.handler.handle(request)


if __name__=="__main__":
   c=Client()
   requests=[2,5,30]
   c.delegate(requests)


