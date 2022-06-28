import json

import os

from Filesize import CheckSize

paths = os.path.dirname(os.path.abspath(__file__))

import os

import py7zr

import multivolumefile

from tempfile import TemporaryDirectory

def SplitaFiless(path :str): 

        with open(path, "rb") as file:
        
          data = file.read()

        part_size = 10000000

        filename = os.path.basename(path)

        foldername = path.split(".")[0]

        os.mkdir(foldername)

        with multivolumefile.open( foldername +"/"+ filename + ".7z","wb",volume=part_size) as vol:

            with py7zr.SevenZipFile(vol, "w") as archive:
                        
                archive.writestr(data, filename)

        listafiles = os.listdir(foldername)

        listafinal = list()

        for fin in listafiles:

            listafinal.append(foldername+"//"+fin)

        if(os.path.exists(path)):


                os.remove(path=path)

        return listafinal


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

        if(bytescopiados > 3000000):

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
