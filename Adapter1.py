class Korean:
   def __init__(self,name):
      self.name=name
   def speak_korean(self):
      return f"{self.name} speaks korean"

class British:
   def __init__(self,name):
       self.name=name
   def speak_british(self):
      return f"{self.name} speaks british"

class Adapter:
    def __init__(self,obj,**method):
        self.obj=obj
        self.__dict__.update(method)

    def __getattr__(self,attr):
        return get(self.obj,attr)

if __name__=="__main__":
   objects=[]
   korean=Korean()
   british=British()
   objects.append(Adapter(korean,speak=korean.speak_korean))
   objects.append(Adapter(british,speak=british.speak_british))
   for obj in objects:
       obj.speak()

   
      