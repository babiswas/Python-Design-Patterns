class British:
   def __init__(self,name):
       self.name=name
   def speak_english(self):
      return "English"

class Korean:
   def __init__(self,name):
       self.name=name
   def speak_korean(self):
        return "Korean"

class Adapter:
   def __init__(self,object,**adapted_method):
        self.object=object
        self.__dict__.update(adapted_method)
   def __getattr__(self,attr):
       return getattr(self.object,attr)

if __name__=="__main__":
   objects=[]
   korean=Korean("Korean")
   british=British("British")
   objects.append(Adapter(korean,speak=korean.speak_korean))
   objects.append(Adapter(british,speak=british.speak_english))
   for obj in objects:
       print(f"{obj.name} says {obj.speak()}")

   

