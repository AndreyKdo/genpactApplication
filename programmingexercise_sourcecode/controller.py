"""
Code of the critic functions Control class. It evaluates the files and moves them to Processed or not applying folders. 
    Copy data from the excel workbooks to the masterBook.xlsx
Author: Andrey Fabián Picado Arias - Costa Rica participant to apply Genpact
Last modified: 05/24/2022 8:20 pm 
"""

from ast import If
from queue import Empty
import shutil
from tokenize import String
from libraries import *
from pathlib import Path
import re

class Controller:
    folder = ""
    pathprocessed = os.getcwd()+"/Processed"
    pathnotapply = os.getcwd()+"/Not_applicable"
    pathmasterbook = os.getcwd()+"\masterBook.xlsx"
    toprocessfiles = [Empty]
    notapplyfiles = [Empty]
    fileslist = [Empty]
    def __init__(self):
        self.verifymasterbook()
        self.masterbook = openpyxl.load_workbook(self.pathmasterbook)
    def verifymasterbook(self):
        fileName = self.pathmasterbook
        fileObj = Path(fileName)
        if fileObj.is_file() == False:
            wb = openpyxl.Workbook()
            wb.save(self.pathmasterbook)
        else:
            pass    
    def setfileslist(self, fileslist):
        self.fileslist = fileslist
        
    def setmaster(self, masterbook):
        self.masterbook = masterbook
    def setfolder(self, folder):
        if folder[-1] != "/":
            folder = folder + "/"
        self.folder = folder
    def getfolder(self):
        return self.folder
               
    
    def gettoprocessfiles(self):
        return self.toprocessfiles
    def getnotapplyfiles(self):
        return self.notapplyfiles    
            
    def deletetoprocessfiles(self,indice):
        self.toprocessfiles.pop(indice)
    def deletenotapplyfiles(self,indice):
        self.notapplyfiles.pop(indice)
    def clearlists(self):
        self.notapplyfiles.clear()
        self.toprocessfiles.clear()
        self.fileslist.clear()
    def validpaths(self):
        isExist1 = os.path.exists(self.pathprocessed)
        if not isExist1:
            os.makedirs(self.pathprocessed)
            
        isExist2 = os.path.exists(self.pathnotapply)
        if not isExist2:
            os.makedirs(self.pathnotapply)
    
    def movetoProcessed(self,file):    
        #"Moving to Processed"
        shutil.move(self.folder+file.name,self.pathprocessed)
        
    def movetoNotapply(self,file): 
        #"Moving to Not apply")
        shutil.move(self.folder+file.name,self.pathnotapply)

        
    def copytomaster(self,archivoexcel):        
        booktocopy = openpyxl.load_workbook(self.folder+'\\'+archivoexcel.name)
                
        for sheet in booktocopy.sheetnames:
            self.masterbook.create_sheet(sheet+"-"+str(datetime.today().strftime('%Y-%m-%d %H-%M-%S')))
            destinationsheet = self.masterbook[self.masterbook.sheetnames[-1]] 
            originsheet = booktocopy[sheet]
            maxr = originsheet.max_row
            maxc = originsheet.max_column
            for r in range (1, maxr + 1):
                for c in range (1, maxc + 1):
                    destinationsheet.cell(row=r,column=c).value = originsheet.cell(row=r,column=c).value
            self.masterbook.save(self.pathmasterbook)  
    
    def validfilesareclosed(self,folder):
        for file in self.fileslist:
            if self.validexcell(file):
                sauxfile = folder+file.name        
                os.rename(folder+file.name,folder+"temp")
                os.rename(folder+"temp",sauxfile)  
                    
    
    def validexcell(self,file):
        if file.is_file() and re.search(".*\.xls.?$",file.name):
            return True
        else:
            return False    
    def organizefiles(self):
        self.validpaths()
        for file in self.fileslist:            
            if self.validexcell(file):
                self.toprocessfiles.append(file)
                self.copytomaster(file)
                self.movetoProcessed(file)
            else:
                self.notapplyfiles.append(file)
                self.movetoNotapply(file)
        
        
         