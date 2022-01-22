from pytube import YouTube

from cleanname import CleanName

import yt_dlp

from YTLOGGER import YTLOGGER

def DowlandVid(link,update):


    print("Descargando video de youtube " +str(link))

    update.message.reply_text("Descargando video de youtube " +str(link))


    
    try:
      dowlandesr = yt_dlp.YoutubeDL({"logger" : YTLOGGER() })

      titulo = dowlandesr.extract_info(link)

      print(titulo['title'])

      name = titulo['title']
      
      finalname = dowlandesr.prepare_filename(titulo)

      print(finalname)

      print("Descarga finalizada")

      update.message.reply_text("Descarga finalizada")

      

      
      return "app/"+finalname,100

    except:

        print("No se pudo descargar "+name+" por razones puedes que el video no sea descargable o no te deje acceder a Youtube")

    

def DowlandVide(link,update):

    yt = YouTube(str(link))

    print("Descargando video de youtube " +str(link))

    update.message.reply_text("Descargando video de youtube " +str(link))
  
    video = yt.streams.get_by_resolution("720p")

    print(yt.title)

    name = CleanName(yt.title)

    print(name)
    
    try:

      video.download("/app/",str(name+".mp4"))
      
      print("Descarga finalizada")

      update.message.reply_text("Descarga finalizada")
    
      return "/app/"+str(name+".mp4"),video.filesize

    except:

        print("No se pudo descargar "+name+" por razones puedes que el video no sea descargable o no te deje acceder a Youtube")



    pass