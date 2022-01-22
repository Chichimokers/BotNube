from posixpath import basename

from typing import List

import multivolumefile

import py7zr  # type: ignore

import os
import shutil
from tempfile import TemporaryDirectory

paths = os.path.dirname(os.path.abspath(__file__))

def SpliaFileInZip(path):

    with TemporaryDirectory() as tempdir:

       print("Diviendo el Archivo ")

       finalname = os.path.basename(path)

       nombrefinal = tempdir + "//"+finalname


       with multivolumefile.open(str(nombrefinal+'.7z'), mode='wb', volume=50000000) as target_archive:

          with py7zr.SevenZipFile(target_archive, 'w') as archive:

              archive.writeall(path, 'target')
              
       print("termino de dividir")

       partes = os.listdir(tempdir)

       finallist = list()

       directoryactually = list()

       for e in partes:

        finallist.append(str(tempdir+"//"+e))

       for r in finallist:

           nombrebas = os.path.basename(r)

           shutil.move(r,str(paths+"//"+nombrebas))
         
           print("Se movio hacia " + paths +"//"+nombrebas)

           directoryactually.append(paths+"//"+nombrebas)

           datos = 0

       os.remove(path)
        
       return directoryactually