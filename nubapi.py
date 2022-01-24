
from os import path

import bs4

from bs4.element import ProcessingInstruction

import requests

import parser 
import time
import sre_parse 
from urllib import parse
from requests_toolbelt import MultipartEncoder ,MultipartEncoderMonitor

from requests.sessions import Session

import os
from datetime import datetime
from telegram import update
from telegram.message import Message

from Filesize import CheckSize

import json

paths = os.path.dirname(os.path.abspath(__file__))

lastporcent = "%"
def Contexto(context):

    global contexto

    contexto = context


    pass

class NubApi():

    def __init__(self) -> None:

        self.Session = requests.Session()

        self.Session.headers.update({"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"})

        self.Moodle = "https://cursos.uo.edu.cu/"

        self.urls = self.Moodle+"login/index.php"

        self.token = ""

        self.Autor = "Alguien Escondido"

        self.username = 'something'

        self.password = 'Systemcrashed404*'
        
        self.InitialNegotiation()

        self.Login()

        pass

    def GetDashBoard(self):

        respuesta = requests.get(self.Moodle+"/my",cookies=self.Session.cookies)

        print(respuesta.text)

        print(respuesta.url)

    def InitialNegotiation(self):

        try:
          respuesta = self.Session.get(url=self.urls)
  
          contenido  = respuesta.content

          er = bs4.BeautifulSoup(contenido,'html.parser')

          tokelonginer = er.find('input',{'name':'logintoken'})['value']

          self.token = tokelonginer
      
          #   print("##########Headers de la sesion ##########")

          #   print(self.Session.headers)

          #     print("##########Response headers de la sesion ##########")
        
          #  print(respuesta.headers)

          print("###########<<<<<<<<<Cookie de Initial>>>>>>>>>>>>>>>#############")

          print(respuesta.url)
        
          for a in self.Session.cookies:
 
            print(a)
        except:
         print("Error al obtener logintken")
         self.InitialNegotiation()

        pass

    def Login(self):

        try:

          # print("##########DATOS##########")

          data = {'anchor':'','logintoken': self.token, 'username': self.username, 'password': self.password}
          #data = {'anchor':'', 'username': self.username, 'password': self.password}

          # data = {'username': 'titi', 'password': 'titicloud123'}

          #  print(data)

          #   print(self.token)

          self.Session.headers.update({"Content-Type":"application/x-www-form-urlencoded"})

          respuesta = self.Session.post(url=self.urls,data=data)

          #print("##########Headers de la sesion ##########") 

          print(self.Session.headers)

          # print("##########Response headers de la sesion ##########")

          # print(respuesta.headers)

          # print("###########<<<<<<<<<Cookie de Login>>>>>>>>>>>>>>>#############")

          print(respuesta.url)

          print(respuesta)

          print(respuesta.links)

           #  for a in self.Session.cookies:

        except:
            
           print("Ha ocurrido un Error al loguearse en la nube")

           self.Login()

        pass
   
    def DowlandFile(self,url):

        clean_url = parse.unquote(url)

        bytescopiados = 0

        completename  = clean_url.split("/")[-1]

        respuesta = self.Session.get(clean_url)

        print("Downloading.....")

        f = open(paths+"\\Dowland\\"+completename,"wb")

        for bytesacopiar in respuesta.iter_content(chunk_size=4096*1024):

            if bytesacopiar:

                bytescopiados += len(bytesacopiar)

                f.write(bytesacopiar)
                
                print("Se han copiado "+CheckSize(bytescopiados))

        f.close()

    def UploadFile(self,pathfile :str,update):

          name = pathfile.split("/")[-1]

          #with  as file:
        
            #data = file.read()
         #name = pathfile.split("\\")[-1]

 
          longitud = open(pathfile,'rb') 

          datos = longitud.read()

          size = len(datos)

          tamanofinal =str(CheckSize(len(datos)))

          print("El size del archivo es "+ str(tamanofinal))

          datos = 0

          longitud.close()

          iles = {"repo_upload_file": open(pathfile,'rb')}

          try:

            contenido  = self.Session.get(self.Moodle+"user/files.php")
 
            er = bs4.BeautifulSoup(contenido.text,'html.parser')

            sesky = er.find('input',{'name':'sesskey'})['value']

            print(sesky)

          except:
              
              print("No se pudo obtener la sesskey")
              
              return "error"

          if(er != None):

            ctssxid = er.find('object',{'type':'text/html'})['data']

          else:

              update.message.reply_text("No se pudo Obtener el data para sacar ctxid y itemid")
        
              return "error"

          if(ctssxid !=None):

           spliteado = ctssxid.split('&')

           itemid = spliteado[2].split('=')[1]

           ctxid = spliteado[7].split('=')[1]

           print(ctxid ,itemid)

          else:

              print("Como no se pudo obtener el data para item y ctx no se sacaran")

              return "error"


          
          print("Subiendo "+pathfile)
        

          if(update != None):
            
            update.message.reply_text("Se esta subiendo el archivo "+ str(name))

          update.message.reply_text("La longitud del arhcivo es :"+str(tamanofinal))

          mensajeuno = update.message.reply_text("Uploading 0%")
  
          grupouploading = contexto.bot.send_message(chat_id='-1001791545677',text=str("Se esta subiendo "+str(name) +" Uploading 0%")) 

          def upload_callback(monitor):
              
            s = "Se ha subido " + CheckSize(int(monitor.bytes_read)) + " de "+ tamanofinal
          
            now = datetime.now()

            if(int(monitor.bytes_read) != 0 ):
             
              porcent = int(monitor.bytes_read/size*100)

              
              cambio = str("Uploading "+str(CheckSize(monitor.bytes_read))+" de "+str(CheckSize(size))+" "+str(porcent)+"%") 
 
              grupocambio = "Se esta subiendo "+str(name) +" Uploading "+str(CheckSize(monitor.bytes_read))+" de "+str(CheckSize(size))+" "+str(porcent)+"%"

              print(s)


              if(mensajeuno.text.split(" ")[-1] != str(str(porcent)+"%")):
 
                   lista = [1,10,15,20,30,35,40,50,60,70,80,90,100]

                   for e in lista:

                     if(e == int(porcent)):

                         print("Se cambio")
                         
                         lastporcent = str(porcent)

                         grupouploading.text = grupocambio

                         grupouploading.edit_text(grupocambio)

                         mensajeuno.text = cambio
                         
                         mensajeuno.edit_text(cambio)


               
              else :
                 print("no se cambio")

              
        

              pass

          values = {'sesskey': sesky,'repo_id':'4','author':self.Autor,'savepath':'/','title':name,'itemid':itemid,'ctx_id':ctxid,"repo_upload_file": (name,open(pathfile,'rb'))}
       
          e = MultipartEncoder(fields=values)

          m = MultipartEncoderMonitor(e, upload_callback)
          headers = {"Content-Type": m.content_type}

          respuesta = ""

          respuesta = requests.post(self.Moodle+"/repository/repository_ajax.php?action=upload",cookies=self.Session.cookies,data=m,headers=headers)
         #print("###########<<<<<<<<<Cookie de Upload>>>>>>>>>>>>>>>#############")
        
         #for a in self.Session.cookies:

         #    print(a)
 

          print("###########Request URL#############")

          print(respuesta.request.url)

         #print("###########Request Headers#############")

         #print(respuesta.request.headers)

        # print("######Codigo de Respuesta########")

         #print(respuesta.status_code)  
 
         #print(respuesta.headers)

          print("###########Request Content#############")

          print(respuesta.text)
          try:

             er = json.loads(respuesta.text)
          
          except:

              update.message.reply_text("❌❌Error al leer el Json❌❌")

              print("❌❌Error fatal al leer el json❌❌")
              grupouploading.delete()
              mensajeuno.delete()
              time.sleep(2)

              return "error"
            
          try: 
            
             if(er["error"]):

                 print("❌❌!!!!!!!!!!!!!!Error fatal al subir arhcivo!!!!!!!!!!!!!❌❌")
                
                 update.message.reply_text("❌❌Error fatal al subir❌❌")

                 grupouploading.delete()

                 mensajeuno.delete()

                 time.sleep(2)
  
                 return "error"

          except:

             update.message.reply_text("✅ Se subio correctamente el fichero " + name+"✅")

             grupouploading.delete()

             mensajeuno.delete()

             if(os.path.exists(pathfile)):

                 print("Existe")

                 os.remove(pathfile)
            

             else:

                 print("ya el arhcivo fue borrado")
                 
             time.sleep(2)

             return respuesta.text


          pass
