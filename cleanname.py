import string
from typing import List

import threading

from string import printable

def CleanName(name:str):
    Listadecaracteres = list(name)  
    i = 0
    while i<5:
        for character in Listadecaracteres:
          if(character == ")"):
             Listadecaracteres.remove(character)
          if(character == "("):
             Listadecaracteres.remove(character)
          if(character == "/"):

              Listadecaracteres.remove(character)

          if(character == "-"):

              Listadecaracteres.remove(character)

          if(character == "="):

              Listadecaracteres.remove(character)

          if(character == "%"):

            Listadecaracteres.remove(character)
          if(character == "\n"):

            Listadecaracteres.remove(character)
          if(character == "!"):

            Listadecaracteres.remove(character)

          if(character == ":"):    

            Listadecaracteres.remove(character)

          if(character == "|"): 

               Listadecaracteres.remove(character)

          if(character == ">"): 

              Listadecaracteres.remove(character)

          if(character == "<"):

              Listadecaracteres.remove(character)
              
          if(character == "?"):

              Listadecaracteres.remove(character)

          if(character == " "):

            Listadecaracteres.remove(character)

          if(character == ","):
            
            Listadecaracteres.remove(character)

        i = i+1

    final = ""

    for fianl in Listadecaracteres:

        final+= fianl

    return str(final)

    pass
def ReduceName(name:str):
  Listadecaracteres = list(name)

  final = ""

  for er in range(20):

    final += Listadecaracteres[er]
    
  return str(final)
  pass
