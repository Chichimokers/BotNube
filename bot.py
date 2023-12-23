
from cgitb import text
from datetime import time
import urllib
from FuncionesBot import Ped
import telegram
from telegram.bot import Bot

from TareaFinalizable import StoppableThread

import threading

from typing import ContextManager, List, Text

from telegram import update

from FuncionesBot import CancelarTarea

from telegram.files.document import Document

import os



from urllib import parse

from telegram.ext import CommandHandler,Updater , MessageHandler

from telegram.ext.conversationhandler import ConversationHandler

from telegram.ext.filters import Filters, MessageFilter

from telegram import ChatAction, chat, message

from telegram.update import Update
from dowlandFile import Contexton
from dowlandFileMultipart import Contextito

import shutil


import requests

import time
from FuncionesBot import NUBUPLOAD

import re 

import bs4

from os.path import basename

from ChekAllows import EstasPermitiado , AreAdmin

from FuncionesBot import DisallowUser ,ProcesartxtdeYoutube,DescargarVideodeYoutube,Agregarusuario,ProcesarDescargadeunFichero,DowlandFromTxt

from nubapi import Contexto

Entrada_de_la_Descaraga = 0 

ChangeToken = 1

BanUSEr=988
nubdowland = 5000
Dowlandtxt = 100

Dowland_Trance = 5

youtubetxt = 6

allowuser = 3

paths = os.path.dirname(os.path.abspath(__file__))

def ProcessYutubetxt(update,context):
 

 ProcesartxtdeYoutube(update=update,context=context)

 return ConversationHandler.END

 pass

def ProccesYoutubeDowland(update,context):

    DescargarVideodeYoutube(update=update,context=context)

    return ConversationHandler.END

    pass
def Test(update,conext):

    r = requests.get("https://eva.uo.edu.cu")

    print(r.content)

    

def Dowland(update,context):

    #Downland entry point

    print("/dowland  fue utilizado por @"+str(update.message.chat.username))

    if(EstasPermitiado(update=update)):


     update.message.reply_text("Envie el enlace")

     return Entrada_de_la_Descaraga

    else :

        update.message.reply_text("No estas autorizado para utilizar este bot")
  
    pass

def start(update,context):
    #init Handler

    print("/start fue utilizado por @"+str(update.message.chat.username))

    print(update)

    print(context)

    if(EstasPermitiado(update=update)):

        update.message.reply_text("Utilize /dowland y luego instrodusca un url valido")

    else:

        update.message.reply_text("No estas autorizado para usar este bot")


    pass
    #Downland action
    
def ChangeTokens(update,context):

    print("/token fue utilizado por @"+str(update.message.chat.username))

    if(EstasPermitiado(update=update)):

      update.message.reply_text("Introdusca el nuevo token")

      return ChangeToken

    else:

      update.message.reply_text("No estas autorizado para usar este bot")

    pass

def processtoken(update,token):

    print("Cambio el token @"+str(update.message.chat.username))

    _tokenfinal = update.message.text

    return ConversationHandler.END

    pass

#Dowland youtube videos from txt list
def Youtubetxt(update,context):
    
    print("/youtubetxt fue utilizado por @"+str(update.message.chat.username))

    if(EstasPermitiado(update=update)):

      update.message.reply_text("Envie un txt con los enlaces")

      return youtubetxt

    else:

         update.message.reply_text("No estas autorizado para usar este bot")
       
    pass

def AllowUser(update,conext):

    print("/allow fue utilizado por @"+str(update.message.chat.username))

    if(AreAdmin(update)):

        update.message.reply_text("Que usuarios quieres permitir")

        return allowuser

    else:

        update.message.reply_text("No eres admin")

    pass
def banUser(update,context):

    if(AreAdmin(update)):

        update.message.reply_text("que usuario quieres banear")

        return BanUSEr
    else:

        update.message.reply_text("No eres admin")

    pass


def BanearUsuario(update,context):

    DisallowUser(update=update,context=context)

 
    return ConversationHandler.END

    pass

def AddUser(update,context):

    Agregarusuario(update=update,context=context)
   
    return ConversationHandler.END
    
    pass

def downloadTxt(update,conext):

    print("/dowlandtxt fue utilizado por  @"+str(update.message.chat.username))

    if(EstasPermitiado(update=update)):

     update.message.reply_text("Envie el archivo con los enlaces")

     return Dowlandtxt

    else:

     update.message.reply_text("No estas autorizado para usar este bot")

    pass
def TestNube(context):

    def start():
        
      while True:

       urls = "https://aulavirtual.sld.cu/login/index.php"
 
       try:
         respuesta = requests.get(url=urls)
 
         contenido  = respuesta.content
         #print(contenido)
       

         #er = bs4.BeautifulSoup(contenido,'html.parser')
 
         #tokelonginer = er.find('input',{'name':'logintoken'})['value']

         #context.bot.send_message(chat_id='-1001791545677',text="✅La Nube esta  ready✅")
         print("Puede acceder a la nube correctamente ")
       except:
        print("Error al loguerase en la nube ")
            #context.bot.send_message(chat_id='-1001791545677',text="🛑La Nube esta  fallando🛑 ")

       time.sleep(1800)
      
    PrincipalThread = StoppableThread(target=start)

    PrincipalThread.start()
    

CancelTrace = 56
def Cancelartareas(update,context):

    print("/cancel fue utilizado por  @"+str(update.message.chat.username))

    if(EstasPermitiado(update=update)):

     update.message.reply_text("Envie el ID de su descarga")

     return CancelTrace

    else:

     update.message.reply_text("No estas autorizado para usar este bot")
    pass
def DowlandYoutubeVideo(update,context):
#Youtube dowland entry point
    
    print("/youtube fue utilizado por  @"+str(update.message.chat.username))
    
    if(EstasPermitiado(update=update)):

     update.message.reply_text("Envie el enlace del video de youtube")

     return Dowland_Trance

    else:

     update.message.reply_text("No estas autorizado para usar este bot")

    pass
def nubdowlanda(update,context):

    NUBUPLOAD(update=update,context=context)
   
    return ConversationHandler.END
    
    pass

def nubdowlandsin(update,context):

    print("/nubdowland fue utilizado por  @"+str(update.message.chat.username))
    
    if(EstasPermitiado(update=update)):

     update.message.reply_text("Envie el enlace")

     return nubdowland

    else:

     update.message.reply_text("No estas autorizado para usar este bot")

    pass
dowlandpentry = 9000
def dowlandp(update,context):
    print("/dowlandp  fue utilizado por @"+str(update.message.chat.username))

    if(EstasPermitiado(update=update)):


     update.message.reply_text("Envie el enlace")

     return dowlandpentry

    else :

        update.message.reply_text("No estas autorizado para utilizar este bot")
  
    pass
    pass
def main():
        
      
        token = "5127350516:AAEYj2U1diLTU0lAh2csg_rtqSCTHXYJiFc"
      


        update = Updater(token=token,use_context=True)

        despachador =  update.dispatcher
        

        despachador.add_handler(CommandHandler('start',start))
        
        despachador.add_handler(ConversationHandler(

        entry_points=
        [
    
            CommandHandler('dowland',Dowland),
            CommandHandler('token',ChangeTokens),
            CommandHandler('youtube',DowlandYoutubeVideo),
            CommandHandler('youtubetxt',Youtubetxt),
            CommandHandler('allow',AllowUser),
            CommandHandler('Dowlandtxt',downloadTxt),
            CommandHandler('cancel',Cancelartareas),
            CommandHandler('Test',Test),
            CommandHandler('ban',banUser),
            CommandHandler('nubdowland',nubdowlandsin),
            CommandHandler('downlandp',dowlandp)
        ],
        states=
        {
            dowlandpentry: [MessageHandler(Filters.text,Ped)],
            ChangeToken: [MessageHandler(Filters.text,processtoken)],
            Entrada_de_la_Descaraga: [MessageHandler(Filters.text,proccesrequest)],
            Dowland_Trance :[MessageHandler(Filters.text,ProccesYoutubeDowland)],
            youtubetxt:[MessageHandler(Filters.document,ProcessYutubetxt)],
            allowuser:[MessageHandler(Filters.text,AddUser)],
            Dowlandtxt:[MessageHandler(Filters.document,DowlandFromTxt)],
            CancelTrace:[MessageHandler(Filters.text,CancelarTarea)],
            BanUSEr:[MessageHandler(Filters.text,BanearUsuario)],
            nubdowland:[MessageHandler(Filters.text,nubdowlanda)]
        },
        
        fallbacks=[]

    ))
        
        
        print("Listo para descargar")

        TestNube(despachador)
        Contexto(despachador)
        Contextito(despachador)
        Contexton(despachador)
        update.start_polling()
      
        update.idle() 
     
        pass  
        
def proccesrequest(update,context):

    ProcesarDescargadeunFichero(update=update,context=context)
    
    return ConversationHandler.END

if __name__ == "__main__":
      main()