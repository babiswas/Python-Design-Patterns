l=[[1,2,3],[4,5,6],[7,8,9],[10,11,1]]

def getkey(m):
   return m[2]


class A:
   def __init__(self,a,b):
       self.a=a
       self.b=b




if __name__=="__main__":
   k=sorted(l,key=getkey)
   m=[A(1,2),A(3,0),A(2,-1)]
   n=sorted(m,key=lambda obj:f"{obj.b} value")
   print(k)
   print(m)


