import os

import os.path

from todus3 import client

from todus3.main import register

from os import remove


paths = os.path.dirname(os.path.abspath(__file__))

def NewToken(token):
      
    if(os.path.isfile(paths+"//token//token.txt")):  

          os.remove(paths+"//token//token.txt")

          filewrite =  open(str(paths+"//token//token.txt"),"w")

          filewrite.write(token)

          filewrite.close()
         
          return token

    pass