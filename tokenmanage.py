import os

import os.path

from todus3 import client

from todus3.main import register


paths = os.path.dirname(os.path.abspath(__file__))
def searchToken(clienteTodus : client.ToDusClient,telefono):

    if(os.path.isfile(paths+"//token//token.txt")):   

          fileread = open(str(paths+"//token//token.txt"),"r")

          tokenread = fileread.read()

          fileread.close()

          return tokenread
    else:
        password = register(clienteTodus, telefono)

        _token = clienteTodus.login(telefono, password)

        if(os.path.exists(paths+"//token")):

            print("")

        else:
            os.mkdir(paths+"//token")

        filwrite = open(paths+"//token//token.txt","w")

        filwrite.write(_token)

        filwrite.close()  
        
        return  _token
    pass