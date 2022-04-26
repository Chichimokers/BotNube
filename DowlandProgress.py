from time import process_time
from Filesize import CheckSize
def DowlandProgress(bytescopiados,totalsize,mensaje,context,name,group):
   
    porcent = int(bytescopiados/totalsize*100)

    listaporcent =[1,20,30,60,90,100]

    mensajeacambiar = "Descargado...... "+name+" "+str(CheckSize(bytescopiados)) +" de " +str(CheckSize(totalsize)) +" "+str(porcent)+"%"

    if(mensaje.text.split(" ")[-1] != str(porcent)+"%"):       
      for e in listaporcent:

          if(porcent == e):

             mensaje.edit_text(mensajeacambiar)

             group.edit_text(mensajeacambiar)

             group.text = mensajeacambiar

             mensaje.text=mensajeacambiar

    pass
