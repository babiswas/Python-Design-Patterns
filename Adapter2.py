class Korean:
   def __init__(self,name):
      self.name=name
   def speak_korean(self):
      return f"{self.name} speaks korean"

class British:
   def __init__(self,name):
      self.name=name
   def speak_english(self):
      return f"{self.name} speaks english"

class Adapter:
   def __init__(self,obj,**function):
       self.obj=obj
       self.__dict__.update(function)
   def __getattr__(self,attr):
      return getattr(self.obj,attr)

if __name__=="__main__":
  korean=Korean("korean")
  british=British("british")
  objects=[]
  objects.append(Adapter(korean,speak=korean.speak_korean))
  objects.append(Adapter(british,speak=british.speak_english))
  for obj in objects:
      print(obj.speak())
