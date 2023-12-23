from genericpath import isfile
import threading

from certifi import contents
from nubapi import NubApi
from typing import List
import time
from bs4.builder import TreeBuilderRegistry

from TareaFinalizable import StoppableThread

from UploadtoS3 import UploadFile

from ast import parse

import requests

from Filesize import CheckSize

import os

from cleanname import CleanName

from telegram import ChatAction

paths = os.path.dirname(os.path.abspath(__file__))

def MultipartTask(url: str,update,tarea:StoppableThread,cookies):

    _url = url

    r = requests.get(url,stream =True,cookies=cookies)

    Listadearchivos = [str]

    print("Puso a descargar un archivo grande @"+str(update.message.chat.username))

    nombre = ""

    if(r.headers.get("Content-Disposition") != None):

        nombre = r.headers.get("Content-Disposition")
        
        print(nombre)

        nombre = nombre.split(";")[1]

        print(nombre)


        nombre = nombre.split('"')[1]

    else:

        nombre = _url.split("/")[-1]

    nombre = CleanName(nombre)

    update.message.reply_text("👍🏻Inciando la descarga👍🏻" + nombre)

    bytescopiados = 0

    partes = 0

    if(partes == 0):

            nombredelaparte=paths+"/"+nombre+".part"
            
    else:

            nombredelaparte = paths+"/"+nombre+str(partes)+".part"
            
    file = open(nombredelaparte,"wb")

    sizeparts = 50000000

    Listadearchivos = list()

    Listadearchivos.insert(0,nombredelaparte)

    for bytescop  in r.iter_content(chunk_size=4096*1024):

        if(bytescopiados < sizeparts):
          
          bytescopiados += len(bytescop)
        
          print("Se ha copiado " + str(CheckSize(bytescopiados)))

          file.write(bytescop)
         
        if(bytescopiados > sizeparts):

            partes = partes+1

            file.close()

            filenamebas = str(nombredelaparte.split("/")[-1])

            update.message.reply_text("Se guardo el archivo " + nombredelaparte)
            
            archivoname = paths+"/"+nombre+str(partes)+".part"

            Listadearchivos.insert(partes,archivoname)

            update.message.reply_text("Se Guardara" + archivoname)
            
            nombredelaparte = archivoname

            file = open(nombredelaparte,"wb")

            bytescopiados = 0  

            time.sleep(1)
             


    if(os.path.exists(+nombre+".json")): 

        os.remove(+nombre+".json")
        
    else:
        print("Ya existe")
     

    fichero = open(+nombre+".json","a")

    errorlist = list()

    for file in Listadearchivos:

        filenamebase = str(file.split("/")[-1])

        asd = UploadFile(final=file,name=filenamebase,update=update,multiple=True,context=context)

        if(asd == "error"):

            errorlist.insert(len(errorlist),file)

        print("###########A Escribir en el json###########")

        print(asd)
        
        if(asd != "error"):

            fichero.write(str(asd) +"\n")

    update.message.reply_text("Revisando paquetes que dieron errores")

    print("#####Review Package Errors#########")
    
    def PackageError():

     for er in errorlist:
       
       basedenombre = er.split("/")[-1]
       
       returnado = UploadFile(final=er,name=basedenombre,update=update,multiple=True,context=context)

       if(returnado != "error"):

        errorlist.remove(er)

        fichero.write(str(returnado)+"\n")

     if(len(errorlist) != 0):

         PackageError()

    PackageError()

    fichero.close()
    
    update.message.chat.send_action(action=ChatAction.UPLOAD_DOCUMENT,timeout = 5)

    update.message.chat.send_document(document = open("/app/"+nombre+".json","r"))

    tarea.stop()

    pass