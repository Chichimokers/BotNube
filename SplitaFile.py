import json

import os

from Filesize import CheckSize

paths = os.path.dirname(os.path.abspath(__file__))

def SplitaFile(paht :str):

    cantidaddepartes = 0

    f = open(paht,'rb')

    data = f.read(1024*1024)

    bytescopiados = 0 

    fichero  = open(str(paht+str("."+str(cantidaddepartes)))+".part",'wb')

    lista = list()
    
    lista.insert(0,str(paht+str("."+str(cantidaddepartes)))+".part")

    while(len(data) != 0):

        fichero.write(data)

        bytescopiados = bytescopiados + len(data)

        print("Se han copiado " + CheckSize(bytescopiados))

        data = f.read(1024*1024)

        if(bytescopiados > 50000000):

            print("Cambiando de archivo")

            fichero.close()
            
            cantidaddepartes = cantidaddepartes+1

            bytescopiados = 0

            fichero  = open(str(paht+str("."+str(cantidaddepartes)))+".part",'wb')

            lista.insert(cantidaddepartes,str(paht+str("."+str(cantidaddepartes)))+".part")
            
    data = 0

    bytescopiados = 0

    fichero = 0

    if(os.path.exists(paht)):
        
        print("Se borro el archivo que se dividio")

        os.remove(paht)

    else:

        print("Ya no existe el archivo que se dividio")

    return lista
    

    pass
