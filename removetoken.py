import os

from os import remove

def remove():
  
    paths = os.path.dirname(os.path.abspath(__file__))

    if(os.path.exists(paths+"//token")):

        if(os.path.isfile(paths+"//token//token.txt")):

          os.remove(paths+"//token//token.txt")

          print("removido")

    pass

