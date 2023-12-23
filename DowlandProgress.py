from time import process_time
from Filesize import CheckSize
def DowlandProgress(bytescopiados,totalsize,mensaje,context,name,group):
   
    porcent = int(bytescopiados/totalsize*100)

    listaporcent =[1,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]

    mensajeacambiar = "Descargado...... "+name+" "+str(CheckSize(bytescopiados)) +" de " +str(CheckSize(totalsize)) +" "+str(porcent)+"%"
    try:

      if(mensaje.text.split(" ")[-1] != str(porcent)+"%"):    
           
       for e in listaporcent:

          if(porcent == e):

             mensaje.edit_text(mensajeacambiar)

             group.edit_text(mensajeacambiar)

             group.text = mensajeacambiar

             mensaje.text=mensajeacambiar
    except:

      print("error al cambiar el valor")

    pass
