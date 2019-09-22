import glob
import os

m=glob.glob('.\\*.py')
for i in m:
   os.system('python'+' '+i)

   
