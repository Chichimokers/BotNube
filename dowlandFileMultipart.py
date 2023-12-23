
from genericpath import isfile

import threading

from nubapi import NubApi

from typing import List

import time

from nubapi import NubApi

from bs4.builder import TreeBuilderRegistry

from TareaFinalizable import StoppableThread


from UploadtoS3 import UploadFile

from ast import parse
from DowlandProgress import DowlandProgress

import requests

from Filesize import CheckSize
import time
import os
from SplitaFile import SplitaFile
from cleanname import CleanName

from telegram import ChatAction

from zipfilespliter import SpliaFileInZip
from datetime import datetime
def Contextito(context):

    global contexto

    contexto = context


    pass

paths = os.path.dirname(os.path.abspath(__file__))

def MultipartTask(url: str,update,tarea,cookies,nube :NubApi,Fromtxt :bool,context):

    #Primero se descarga el archiv y luego lo partimos en varias partes de a 50mb
    _url = url

    r = requests.get(url,stream =True,cookies=cookies)

    print("Puso a descargar un archivo grande @"+str(update.message.chat.username))

    nombre = ""
    
    #Desde aqui vemos cual es el nombre del archivo recurriendo a la respuesta de la peticion
    
    if(r.headers.get("Content-Disposition") != None):

        nombre = r.headers.get("Content-Disposition")

        if(nombre.__contains__(";")):

            print(nombre)

            nombre = nombre.split(";")[1]

            if(nombre.__contains__('"')):

                nombre = nombre.split('"')[1]

                print(nombre)

            else:

                nombre = nombre.split('=')[1]

                print(nombre)


    else:

        nombre = _url.split("/")[-1]

    nombre = CleanName(nombre)

    update.message.reply_text("👍🏻Inciando la descarga👍🏻" + nombre)

    hola =  update.message.chat.send_message("Descarga Inciada")
    
    bytescopiados = 0

    listaficheros = list()

    print(os.listdir("/app/"))

    #aqui vemos si el archivo existe y si esta compelto para si no volverlo a descargar

    if(os.path.exists(paths+"/"+nombre)):

        f = open(paths+"/"+nombre,'rb')

        data =f.read()

        f.close()

        if(len(data) == len(r.content)):

          print("ya el archivo existe se procedera subir ")

          listaficheros =  SplitaFile(paths+"/"+nombre)
          
          data = 0

        else:       

         update.message.reply_text("El existe pero no tiene la misma logitud se descargara de nuevo ")

         print("El existe pero no tiene la misma logitud se descargara de nuevo ")

         file = open(paths+"/"+nombre,"wb")

         ##grupouploading = context.bot.send_message(chat_id='-1001791545677',text=str("Se esta descargando "+str(nombre) +" Downloading 0%"))
         
         for bytescop  in r.iter_content(chunk_size=4096*1024):

          if bytescop:
          
           bytescopiados += len(bytescop)
        
           print("Se ha copiado " + str(CheckSize(bytescopiados)))

           file.write(bytescop)

           now = datetime.now()


           DowlandProgress(bytescopiados=bytescopiados,totalsize=int(r.headers.get("Content-Length")),group=grupouploading,mensaje=hola,context=contexto,name=nombre)

           print(nombre)

          file.close()

          hola.edit_text("Descarga Completada")
          
          listaficheros =  SplitaFile(paths+"/"+nombre)
   
    else:

     print("El archivo no existe se procedera a descargar ")

     file = open(paths+"/"+nombre,"wb")
     ##grupouploading = context.bot.send_message(chat_id='-1001791545677',text=str("Se esta descargando "+str(nombre) +" Downloading 0%"))
     
     for bytescop  in r.iter_content(chunk_size=4096*1024):

        if bytescop:
          
          bytescopiados += len(bytescop)
        
          print("Se ha copiado " + str(CheckSize(bytescopiados)))

          file.write(bytescop)
        

          DowlandProgress(bytescopiados=bytescopiados,totalsize=int(r.headers.get("Content-Length")),group=grupouploading,mensaje=hola,context=contexto,name=nombre)

          print(nombre)

     file.close()

     hola.edit_text("Se completo la descarga:)")

     listaficheros =  SplitaFile(paths+"/"+nombre)

    update.message.reply_text(str("Se ha dividido en " +str(len(listaficheros)) + " ficheros .part"))

    #al terminar de hacer la separacion en archivos de a 50 mb proseguimos a subirloa la nube
    print("Se procedera a subir los archivos")
    
    enlacesdearchivscopiados = ""

    print(os.listdir("/app/"))

    if(Fromtxt == False):

      if(os.path.exists("/app/"+nombre+".json")): 

        os.remove("/app/"+nombre+".json")
        
      else:
        print("Ya existe")

      fichero = open("/app/"+nombre+".json","a")

    else:

      enlacesdearchivscopiados = list()
    

    def RetryEror(final,name,update,multiple,nube):

        nube = NubApi()

        asd = UploadFile(final=file,name=filenamebase,update=update,multiple=True,nube=nube,context=context)

        if(asd == "error"):


            RetryEror(final,name,update,multiple,nube)

        else:

            if(Fromtxt == False):

                if(asd != None):    
                 fichero.write(str(asd) +"\n")
            else:

                enlacesdearchivscopiados.insert(len(enlacesdearchivscopiados),asd)
        pass

    for file in listaficheros:

        filenamebase = str(file.split("/")[-1])

        asd = UploadFile(final=file,name=filenamebase,update=update,multiple=True,nube=nube,context=context)

        if(asd == "error"):

            RetryEror(file,filenamebase,update,True,nube)
            
        print("###########A Escribir en el json###########")

        print(asd)

        if(Fromtxt == False):

          if(asd != "error"):

              if(asd != None):

                  fichero.write(str(asd) +"\n")

        else:

            if(asd != "error"):

             enlacesdearchivscopiados.insert(len(enlacesdearchivscopiados),asd)

    #corremos PackageError para ver si existio algun error en la subida de los archivos

    if(Fromtxt == False):
        
        fichero.close()

        update.message.chat.send_action(action=ChatAction.UPLOAD_DOCUMENT,timeout = 5)

        update.message.chat.send_document(document = open("/app/"+nombre+".json","r"))
        
        context.bot.send_document(chat_id='-1001791545677',document = open("/app/"+nombre+".json","r"),caption="fue enviado por @"+str(update.message.chat.username))

       

    print(os.listdir("/app/"))
    
    if(Fromtxt != True):

        if(tarea != None):    

            tarea.stop()
    else:
        
        return enlacesdearchivscopiados
  

    pass
