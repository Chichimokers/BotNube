from TareaFinalizable import StoppableThread
from todus3 import client

from todus3.client import ToDusClient

from UploadtoS3 import UploadFile

from ast import parse

import requests

from Filesize import CheckSize

import os

from cleanname import CleanName

paths = os.path.dirname(os.path.abspath(__file__))

sizeparts = 5000000

def MultipartTask(url: str,tarea:StoppableThread):

    _url = url

    r = requests.get(url,stream =True)

    #print("Puso a descargar un archivo grande @"+str(update.message.chat.username))

    #print("Token actual :"+ str(token))

    nombre = _url.split("/")[-1]

    nombre = CleanName(nombre)

    #update.message.reply_text("👍🏻Inciando la descarga👍🏻" + nombre)

    bytescopiados = 0
    
    file = open(paths+"\Dowland\main.part","wb")

    Actualfilename = str(paths+"\Dowland\main.part")

    partes = 0

    byterecividos =  bytearray

    for receptor in r.iter_content(4096*1024):
        for casilla in byterecividos:
            casilla = receptor
    
    for bytescop  in byterecividos.__iter__():

        if(bytescopiados < sizeparts):

         bytescopiados += len(bytescop)
         
         print("Se ha copiado " + str(CheckSize(bytescopiados)))

         file.write(bytescop)
         
        if(bytescopiados > sizeparts):

            partes = partes+1

            file.close()

            filenamebas = str(Actualfilename.split("/")[-1])

            #UploadFile(clienteTodus=cliete,token=token,final=Actualfilename,name=filenamebas,update=update)

            #update.message.reply_text("Se subio el archivo " + Actualfilename)
            
            archivoname = paths+"\Dowland\main"+str(partes)+".part"

            #update.message.reply_text("Se subira el archivo" + archivoname)
            
            Actualfilename = archivoname

            file = open(Actualfilename,"wb")

            bytescopiados = 0   

            #update.message.reply_text(str(partes)+" archivo finalizado correctamente")
    tarea.stop()
    pass
    

def strar():

    MultipartTask("http://100.102.44.6/asd.rar",er)

er = StoppableThread(target = strar)


er.start()