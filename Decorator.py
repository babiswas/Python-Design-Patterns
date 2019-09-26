from functools import wraps

def decorator(func):
   @wraps(func)
   def wrapper(*args):
      print("Wrapper executed")
      return func(*args)
   return wrapper

@decorator
def fun(*args):
  for i in args:
     print(i)

if __name__=="__main__":
   fun(1,2,3)


  
   