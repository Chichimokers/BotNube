
from cleanname import CleanName, ReduceName

from urllib.request import urlopen

from urllib.request import urlretrieve

from os.path import basename

import threading

import requests
import time
import os
from DowlandProgress import DowlandProgress
import cgi

import sys

from os import system

from telegram import message

from telegram.chat import Chat

from telegram.message import Message

from telegram.update import Update

from Filesize import CheckSize

from urllib import parse
from datetime import datetime
def Contexton(context):

    global contexto

    contexto = context


    pass
paths = os.path.dirname(os.path.abspath(__file__))

def dowland(url,update,cookies):

      _url = str(url)

      clean_url = parse.unquote(_url)

      headers = {
         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0"
      }

      r = requests.get(clean_url,stream =True,headers=headers,cookies=cookies)
      
      print('Descargando ' + url)
      
      completename = ""

      if(r.headers.get("Content-Disposition") != None):

         completename = r.headers.get("Content-Disposition")

         print(completename)
         if(completename.__contains__(";")):

          completename = completename.split(";")[1]

          if(completename.__contains__('"')):

           completename = completename.split('"')[1]

          else:
             completename = completename.split('=')[1]


         print(completename)
         
        
      else:

       completename  = _url.split("/")[-1]

      bytescopiados = 0

      totasize = 0

      if(r.headers.get('Content-Length') == None):

         f =  open(str(paths+"/"+completename), 'wb')  
       
         update.message.chat.send_message(completename)

         hola =  update.message.chat.send_message("Descarga Inciada")

         print(hola)
         
         copaidos = 0

         grupouploading = contexto.bot.send_message(chat_id='-1001791545677',text=str("Se esta descargando "+str(completename) +" Downloading 0%"))

         for bytescop in r.iter_content(chunk_size=4096*1024):

            if bytescop:

               copaidos += len(bytescop)

               f.write(bytescop)


               print("Descargando " + str(CheckSize(copaidos)))

               print(completename)
       

               DowlandProgress(bytescopiados=copaidos,totalsize=int(r.headers.get("Content-Length")),group=grupouploading,mensaje=hola,context=contexto,name=completename)

               sys.stdout.flush()    
         hola.edit_text("Descarga Completada :)")        

         return completename

      
   
      totasize = int(r.headers.get('Content-Length'))

      f =  open(str(paths+"/"+completename), 'wb')  
      
      update.message.chat.send_message(completename)

      hola =  update.message.chat.send_message("Descarga Inciada")
      grupouploading = contexto.bot.send_message(chat_id='-1001791545677',text=str("Se esta descargando "+str(completename) +" Downloading 0%"))

      print(hola)
      for bytescop in r.iter_content(chunk_size=4096*1024):

        if bytescop:

            bytescopiados += len(bytescop)

            f.write(bytescop)

            print(completename)
     
            print("Descargando....."+str(CheckSize(bytescopiados))+" Total "+ str(CheckSize(totasize)))    



            DowlandProgress(bytescopiados=bytescopiados,totalsize=int(r.headers.get("Content-Length")),group=grupouploading,mensaje=hola,context=contexto,name=completename)

            sys.stdout.flush()

      hola.edit_text("Se completo la descarga:)")

      return completename


