

from asyncore import file_wrapper
from genericpath import isfile
import json

from logging import error

import os
from unicodedata import name

from telegram.ext.conversationhandler import ConversationHandler
from telegram.update import Update

from DowlandFromYoutube import DowlandVide
from Filesize import CheckSize
from SplitaFile import SplitaFile
from RandomNumber import getRandomName
import time
from UploadtoS3 import UploadFile

from TareaFinalizable import StoppableThread

from telegram import ChatAction, chat

import urllib

import requests

import bs4
from cleanname import CleanName

from dowlandFileMultipart import MultipartTask
from NexCloudClient import NexCloudClient
from dowlandFile import dowland

from nubapi import NubApi
from zipfilespliter import SpliaFileInZip

global taskslist 

taskslist = list()

paths = os.path.dirname(os.path.abspath(__file__))

finalsize =400 * 1000000

def NUBUPLOAD(update,context):
  def start():
    namefile = dowland(update.message.text,update,None)
    afg = update.message.reply_text("Logueandose")

    a = NexCloudClient("ernesto.perez","*Y@g@miL96","https://nube.uo.edu.cu/")

    a.login()

    afg.edit_text("subiendo")


    def progresfinc(filename,bytes_read,len,speed,a):

      print(filename +" "+str(bytes)+" "+str(bytes_read)+" "+str(len)+" "+str(speed) )

      pass

    asd = a.upload_file(file="/app/"+namefile,path="/"+namefile,progressfunc=progresfinc)

    afg.edit_text("Se subio")
   

    name = namefile

    file = open("/app/"+name+".txt","w")
    for a in asd:
      if(a =="url"):
        file.write(str(asd[a]))

 
    file.close()
  
    update.message.chat.send_document(document = open("/app/"+name+".txt","r"))

  PrincipalThread = StoppableThread(target=start)

  PrincipalThread.start()

  return ConversationHandler.END


  pass
def ProcesartxtdeYoutube(update,context):
     context.bot.send_message(chat_id='-1001791545677',text=str("@"+update.message.chat.username) + " ha usado YoutubeTxt") 
     
     ID =getRandomName()

     update.message.reply_text("El ID de esta tarea es : "+str(ID)) 

     def start():

      nube = NubApi()

      errorlist = list()

      print("Añadio un txt para descargar de youtube  @"+str(update.message.chat.username))

      print (update)
    
      f = open(paths+"//"+"lista.txt","wb")
        
      context.bot.get_file(update.message.document).download(out =f)

      f.close()
    
      finalpaht = str(paths+"//"+"lista.txt")

      archivo = open(finalpaht,"r")

      enlaces = archivo.readlines()

      archivo.close()

      if(os.path.isfile("/app/ListadeVideos.json")): 
          
        os.remove("/app/ListadeVideos.json")

      else:

        print("No existe")

      archivoaenviar = open("/app/ListadeVideos.json","a")

      def RetryError(files,names,update,multi,nube):

        fichero= ""

        nube =NubApi()

        fichero = UploadFile(files,names,update,True,nube,context=context)


        if(fichero == "error"):

          RetryError(files,names,update,True,nube)

        else:

          archivoaenviar.write(str(fichero)+"\n")

        pass

      for er in enlaces:

          nube = NubApi()

          finalpa,size = DowlandVide(er,update=update)

          name = er.split('/')[-1]

          if(size > finalsize):

            update.message.reply_text("El video es largo se dividira en varias partes")
            
            update.message.reply_text("Tiene una size de :" + str(CheckSize(size)))

            partes =  SplitaFile(finalpa)

            for files in partes:

              names = files.split('/')[-1]

              fichero = UploadFile(files,names,update,True,nube,context=context)
              
              if(fichero == "error"):

                RetryError(files,names,update,True,nube)

              else:

               archivoaenviar.write(str(fichero)+"\n")

          else:

              final = UploadFile(finalpa,name,update,True,nube,context=context)

              if(final == "error"):

                RetryError(finalpa,name,update,True,nube)

              else:

                 archivoaenviar.write(str(final)+"\n")
             
         
      archivoaenviar.close()

      update.message.chat.send_action(action=ChatAction.UPLOAD_DOCUMENT,timeout = 5)

      print("Descarga del los videos del txt completada")

      update.message.chat.send_document(document = open("/app/ListadeVideos.json","r"))

      context.bot.send_document(chat_id='-1001791545677',document = open("/app/ListadeVideos.json","r"),caption="fue enviado por @"+str(update.message.chat.username))

      update.message.reply_text("Descarga de los videos del txt completada")

      PrincipalThread.stop()   

      


     PrincipalThread = StoppableThread(target=start)

     PrincipalThread.name = ID

     taskslist.append(PrincipalThread)

     PrincipalThread.start()
     
     return ConversationHandler.END


     
def DescargarVideodeYoutube(update,context):
     context.bot.send_message(chat_id='-1001791545677',text=str("@"+update.message.chat.username) + " ha usado /youtube con este enlace "+ str(update.message.text))   
     ID =getRandomName()

     update.message.reply_text("El ID de esta tarea es : "+str(ID)) 
     def start():

      nube = NubApi()

      errorlist = list()

      print("Esta descargando de Youtube @"+str(update.message.chat.username))

      finalpaht,tama = DowlandVide(update.message.text,update)

      name = finalpaht.split('/')[-1]

      if(tama > finalsize):
          
        update.message.reply_text("El video es largo se dividira en varias partes")

        update.message.reply_text("Tiene una size de :" +str( CheckSize(tama)))

        fichero = open(finalpaht+".json","a")

        flista = SplitaFile(finalpaht)

        def RetryError():

          nube = NubApi()

          respuesta =   respuesta = UploadFile(er,name,update,True,nube,context=context)

          if(respuesta == "error"):

            RetryError()

          else:

            print(respuesta)

            fichero.write(str(respuesta)+"\n")
            
          pass

        for er in flista:

            name =  er.split('/')[-1]

            respuesta = UploadFile(er,name,update,True,nube,context=context)


            if(respuesta == "error"):

              #errorlist.insert(len(errorlist),er)

              RetryError()

            else:
          
              print(respuesta)

              fichero.write(str(respuesta)+"\n")
  
        """ def PackageError():

           for er in errorlist:
       
            basedenombre = er.split("/")[-1]
       
            returnado = UploadFile(final=er,name=basedenombre,update=update,multiple=True)

            if(returnado != "error"):

             errorlist.remove(er)

             fichero.write(returnado+"\n")

            if(len(errorlist) != 0):

             PackageError()"""

      

              
        fichero.close()

        update.message.chat.send_action(action=ChatAction.UPLOAD_DOCUMENT,timeout = 5)

        update.message.chat.send_document(document = open(finalpaht+".json","r"))

        context.bot.send_document(chat_id='-1001791545677',document = open(finalpaht+".json","r"),caption="fue enviado por @"+str(update.message.chat.username))

        Tarea.stop()

      else:

         update.message.reply_text("Subiendo a la Nube")

         UploadFile(finalpaht,name,update,False,nube,context=context)

      Tarea.stop()

      

     Tarea = StoppableThread(target = start)

     Tarea.name = ID

     taskslist.append(Tarea)
    
     Tarea.start()

     return ConversationHandler.END
def CancelarTarea(update,context):

    for tarea in taskslist:

        if(str(tarea.name) == str(update.message.text)):

          tarea.stop()

          print("Se detuvo Correctamente")

          update.message.reply_text("👍Se detuvo Correctamente👍")

    return ConversationHandler.END


    pass
def DowlandFromTxt(update,context):

    context.bot.send_message(chat_id='-1001791545677',text=str("@"+update.message.chat.username) + " ha usado DowlandTxt")
    ID =getRandomName()

    update.message.reply_text("El ID de esta tarea es : "+str(ID)) 
    def start():


      print("Añadio un txt para descargar archvos @"+str(update.message.chat.username))

      print (update)
    
      f = open(paths+"//"+"DescargaFromTXTFILE.txt","wb")
        
      context.bot.get_file(update.message.document).download(out =f)

      f.close()
    
      finalpaht = str(paths+"//"+"DescargaFromTXTFILE.txt")

      archivo = open(finalpaht,"r")

      enlaces = archivo.readlines()

      archivo.close()

      if(os.path.isfile("/app/"+update.message.chat.username+"ListadeDescargas.json")): 
          
        os.remove("/app/"+update.message.chat.username+"ListadeDescargas.json")

      else:

        print("No existe")

      archivoaenviar = open("/app/"+update.message.chat.username+"ListadeDescargas.json","a")


      def RetryError(files,names,update,multi,nube):

        fichero= ""

        nube = NubApi()
        
        fichero = UploadFile(files,names,update,True,nube,context=context)


        if(fichero == "error"):

          RetryError(files,names,update,True,nube)

        else:

          archivoaenviar.write(str(fichero)+"\n")

        pass

      print("El txt descargara "+str(len(enlaces)) + " ficheros")
      
      update.message.reply_text("El txt descargara "+str(len(enlaces)) + " ficheros")

      cantidadcopiados =  0

      for enlace in enlaces:
        
        archivoaenviar = open("/app/"+update.message.chat.username+"ListadeDescargas.json","a")

        cantidadcopiados = cantidadcopiados+1

        nube = NubApi()

        enlacess = ""

        cookies= ""

        clean_url = enlace
       
        print(clean_url)

        r = requests.get(clean_url,stream =True)

        saber  = clean_url.split("/")

        if(saber[2] == "www.mediafire.com"):

          era = bs4.BeautifulSoup(r.content,"html.parser")

          clean_url = era.find('a',{'id':'downloadButton'})['href']

          cookies = r.cookies

          r = requests.get(clean_url,stream =True,cookies=cookies)
        
        if(r.headers.get("Content-Length") == None):

          print("Puso a descargar un archivo  @"+str(update.message.chat.username))

          print(update)
     
          #print("Token actual :"+ str(_tokenfinal))

          update.message.reply_text("👍🏻Inciando la descarga👍🏻")

          update.message.reply_text("No tiene content-Lenght")

          #print('Descargando '+ str(update.message.text))

          #Downland file from internet

          nombre = dowland(clean_url,update,cookies=cookies)

          update.message.reply_text("✅Finalizo la descarga de "+nombre+" ✅")

          update.message.reply_text("📡Subiendo a S3 el archivo "+nombre+"📡")

          finalpaht = paths+"//"+str(nombre)
 
          #Upload File

          enlacess = UploadFile(finalpaht,nombre,update,True,nube=nube,context=context)

          if(enlacess != "error"):
   
             archivoaenviar.write(str(enlacess) + "\n")
 
          else:

             RetryError(finalpaht,nombre,update,True,nube=nube)

        else:

           tamano  = 0

           try:

              tamano  =  int(r.headers.get("Content-Length")) 

           except:

             print("Error")

           if(tamano > finalsize):

             update.message.reply_text("El archivo que va a copiar es grande va a demorar mas de lo normal")
 
             update.message.reply_text("Tiene una size de :" +str( CheckSize(tamano)))
             grandesenalces =  MultipartTask(clean_url,update,None,cookies,nube,True,context=context)

             for en in grandesenalces:
               print(en)
               if(en != None):
                 archivoaenviar.write(str(en)+"\n")

  
           else:
 
              print("Puso a descargar un archivo  @"+str(update.message.chat.username))

              update.message.reply_text("👍🏻Inciando la descarga👍🏻")

              #print('Descargando '+ str(update.message.text))

              #Downland file from internet
 
              nombre = dowland(clean_url,update,cookies=cookies)

              update.message.reply_text("✅Finalizo la descarga de "+nombre+" ✅")
 
              update.message.reply_text("📡Subiendo a S3 el archivo "+nombre+"📡")

              finalpaht = paths+"//"+str(nombre)

              #Upload File

              enlacess  = UploadFile(finalpaht,nombre,update,True,nube=nube,context=context)
  
              if(enlacess != "error"):

                 archivoaenviar.write(str(enlacess) +"\n")

              else:
        
                 RetryError(finalpaht,nombre,update,True,nube)

        """ if(cantidadcopiados == len(enlaces)/2):

          update.message.chat.send_document(document = open("/app/"+update.message.chat.username+"ListadeDescargas.json","r"))"""
        if(open("/app/"+update.message.chat.username+"ListadeDescargas.json","r").read() != None):
              
         archivoaenviar.close()

         update.message.chat.send_document(document = open("/app/"+update.message.chat.username+"ListadeDescargas.json","r"))
        
        update.message.reply_text("Se han copiado "+str(cantidadcopiados)+"de "+str(len(enlaces)) +" Ficheros")

        print("Se han copiado "+str(cantidadcopiados)+"de "+str(len(enlaces)) +" Ficheros")
        
      archivoaenviar.close()

      update.message.chat.send_action(action=ChatAction.UPLOAD_DOCUMENT,timeout = 5)

      print("Descarga de los archivos del txt completada")

      update.message.chat.send_document(document = open("/app/"+update.message.chat.username+"ListadeDescargas.json","r"))

      context.bot.send_document(chat_id='-1001791545677',document = open("/app/"+update.message.chat.username+"ListadeDescargas.json","r"),caption="fue enviado por @"+str(update.message.chat.username))

      update.message.reply_text("Descarga de los archivos del txt completada")

      PrincipalThread.stop()   

      


    PrincipalThread = StoppableThread(target=start)

    PrincipalThread.name = ID

    taskslist.append(PrincipalThread)

    PrincipalThread.start()

    return ConversationHandler.END

    pass

     
def DisallowUser(update,context):

   print("Removio un usuario de la lista @"+str(update.message.chat.username))

   admincontroller = open("/app/whitelist.txt","r")

   userlis = admincontroller.readlines()

   admincontroller.close()

   for r in userlis:

     userlis[userlis.index(r)] = CleanName(r)

   for e in userlis:

     if(e ==update.message.text) :

       update.message.reply_text("Se elimino a @"+update.message.text)

       userlis.remove(e)

   admincontrollers = open("/app/whitelist.txt","w")

   for s in userlis :

       admincontrollers.write(str(s)+"\n")

   admincontrollers = open("/app/whitelist.txt","r")

   userliss = admincontrollers.readlines()

   admincontrollers.close()

   update.message.reply_text("Los usuarios permitidos ahora son")

   for r in userliss:

      update.message.reply_text("@"+r)
  
   update.message.reply_text("Finalizao")

   return ConversationHandler.END

   pass

def Agregarusuario(update,context):
  
    print("Añadio otro usuario a la lista @"+str(update.message.chat.username))

    admincontroller = open("/app/whitelist.txt","a")

    admincontroller.write("\n"+update.message.text)

    admincontroller.close()

    fileadmin = open("/app/whitelist.txt","r")

    Listaadmin = fileadmin.readlines()

    update.message.reply_text("Los usuarios perimitidos ahora son :")

    for userin in Listaadmin:

        update.message.reply_text("@"+userin)

    fileadmin.close()

    update.message.reply_text("Finalizao")


    pass



def ProcesarDescargadeunFichero(update,context):
   mensajegrupo = context.bot.send_message(chat_id='-1001791545677',text=str("@"+update.message.chat.username) + " ha usa /dowland con el enlace "+str(update.message.text))
   ID =getRandomName()

   update.message.reply_text("El ID de esta tarea es : "+str(ID)) 
   def start():
      
     clean_url = update.message.text

     r = requests.get(clean_url,stream=True)

     verificacion = r.headers.get("Content-Length")
     
     cookies= ""

    
    #Eso es por si el server de de Mega o Mediafire

    #https://www.mediafire.com/file/1z86p0316keehjf/11x04.mkv/file
    
     saber  = clean_url.split("/")

     if(saber[2] == "www.mediafire.com"):
       
       era = bs4.BeautifulSoup(r.content,"html.parser")

       clean_url = era.find('a',{'id':'downloadButton'})['href']

       cookies = r.cookies

       r = requests.get(clean_url,cookies=cookies,stream=True)
     
     nube = NubApi()

     if(verificacion == None):

         print("Puso a descargar un archivo  @"+str(update.message.chat.username))

         print(update)
     
         #print("Token actual :"+ str(_tokenfinal))

         update.message.reply_text("👍🏻Inciando la descarga👍🏻")

         #print('Descargando '+ str(update.message.text))

         #Downland file from internet

         nombre = dowland(clean_url,update,cookies=cookies)

         finalpaht = paths+"//"+str(nombre)

         try:
           tamano = r.headers.get("Content-Length")
         except:
           print("Error el contentleght es none")

         if(tamano == None):
           
           tamano = 1
        
         if(tamano > finalsize):

           update.message.reply_text("El archivo que va a copiar es grande va a demorar mas de lo normal")
           update.message.reply_text("Tiene una size de :" +str(CheckSize(tamano)))
           MultipartTask(clean_url,update,tarea=tareas,cookies=cookies,nube=nube,Fromtxt=False,context=context)

         else:

           update.message.reply_text("✅Finalizo la descarga de "+nombre+" ✅")

           update.message.reply_text("📡Subiendo a S3 el archivo "+nombre+"📡")

           #Upload File

           UploadFile(finalpaht,nombre,update,False,nube=nube,context=context)
 
           tareas.stop()

     else:

         tamano  = 0

         try:
          tamano  =  int(r.headers.get("Content-Length")) 
         except: 
           print("Error")


         if(tamano > finalsize):

           update.message.reply_text("El archivo que va a copiar es grande va a demorar mas de lo normal")
           
           update.message.reply_text("Tiene una size de :" + str(CheckSize(tamano)))

           MultipartTask(clean_url,update,tarea=tareas,cookies=cookies,nube=nube,Fromtxt=False,context=context)

         else:
 
           print("Puso a descargar un archivo  @"+str(update.message.chat.username))

           update.message.reply_text("👍🏻Inciando la descarga👍🏻")

           #print('Descargando '+ str(update.message.text))

           #Downland file from internet
           nombre = dowland(clean_url,update,cookies=cookies)

           update.message.reply_text("✅Finalizo la descarga de "+nombre+" ✅")

           update.message.reply_text("📡Subiendo a S3 el archivo "+nombre+"📡")

           finalpaht = paths+"//"+str(nombre)
 
           #Upload File

           UploadFile(finalpaht,nombre,update,False,nube=nube,context=context)

           tareas.stop()

     

   tareas = StoppableThread(target = start)

   tareas.name= ID

   taskslist.append(tareas)

   tareas.start()

   return ConversationHandler.END

