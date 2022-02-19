import json


from telegram.update import Update

from todus3.client import ToDusClient

from todus3.main import split_upload

import os 

from nubapi import NubApi

from telegram import ChatAction, bot, chat, message

def UploadFile(final,name,update,multiple :bool,nube :NubApi,context):
    
       #split_upload(clienteTodus,token,final,10000006,100)

        # if os.path.isfile(listo):
        #     with open(listo,'rb') as txtorigen:
        #         with open(paths+"//"+nombre+".txt",'wb')as desiton:
        #             shutil.copyfileobj(txtorigen,desiton)    
        # 
       filepath = "/app/"+name+".json" 

       respuesta = ""

       respuesta = nube.UploadFile(final,update=update)

       if(multiple==False):

              if(respuesta != "error"):

                 fichero = open(filepath,"w")

                 fichero.write(str(respuesta))  
     
                 fichero.close()

                 print("Archivo Copiado")
 
                 update.message.chat.send_action(action=ChatAction.UPLOAD_DOCUMENT,timeout = 5)
 
                 print("Se a enviado " + filepath)

                 update.message.chat.send_document(document = open(filepath,"r"))

                 #context.bot.send_message(chat_id='-647544571',text=)
                 
                 context.bot.send_document(chat_id='-1001791545677',document = open(filepath,"r"),caption="fue enviado por @"+str(update.message.chat.username))

                 if(os.path.exists(final)):

                     os.remove(final)

                 if(os.path.exists(filepath)):

                     os.remove(filepath)

                 print(os.listdir("/app/"))
                 
               
                 update.message.reply_text("✅Operacion Finalizada✅")
               
              else:
                     print(os.listdir("/app/"))

                     nubea = NubApi()

                     update.message.reply_text("😭Fallo la subida de el archivo " +name+ " y se subira de nuevo😭")
                     
                     UploadFile(final,name,update,False,nubea,context=context)



       else:
              if(respuesta != "error"):

                  if(os.path.exists(final)):
                         
                       print("Existe y se removera")

                       print(os.listdir("/app/"))

                       os.remove(final)
                  else:
                      print("ya el archivo no existe")   

                      print(os.listdir("/app/"))


                  return respuesta

              else:


                  update.message.reply_text("Fallo la subida de el archivo " +name)

                  if(os.path.exists(final)):
                         
                       print("Existe")

                       print(os.listdir("/app/"))

                  else:
                      print("No existe")   

                      print(os.listdir("/app/"))

                  return respuesta

       pass