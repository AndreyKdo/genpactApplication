"""
Code of the Monitor class. It obtains the files of the specified folder
Author: Andrey Fabián Picado Arias - Costa Rica participant to apply Genpact
Last modified: 05/24/2022 8:20 pm 
"""
from queue import Empty
from tokenize import String
from libraries import os
class Monitor:
    folder = ""
    files = [Empty]
    def ___init___(self):
        pass
    def clearfiles(self):
        self.files.clear()
    def setfolder(self, pfolder):
        self.folder = pfolder
    def getfolder(self):
        return self.folder
    def setfiles(self,pfiles):
        self.files = pfiles
    def appendfiles(self,pfile):
        self.files.append(pfile)
    def getfiles(self):
        return self.files
    def deletefilelisted(self,indice):
        self.files.pop(indice)
    def lookingfiles(self):
        with os.scandir(self.folder) as ficheros:
            contenido = [fichero for fichero in ficheros if fichero.is_file()]
        for file in contenido:
                self.appendfiles(file)
        