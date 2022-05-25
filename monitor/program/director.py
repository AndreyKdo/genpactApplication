"""
Code of the 'Orchestra director' class. It controls and validates the GUI commands
Author: Andrey Fabián Picado Arias - Costa Rica participant to apply Genpact
Last modified: 05/24/2022 8:20 pm 
"""

from libraries import *
from monitor import Monitor
from controller import Controller
from tkinter import filedialog
from tkinter import messagebox


class Director:
    MiMonitor = Monitor()
    miInspector = Controller()
    folder = ""
    
    def getfolder(self):
        if self.folder == "":
            return "No folder selected"
        else:
            return self.folder
            
    def validemptyfolder(self):
        if self.folder == "":
            return False
        elif len(os.listdir(self.folder)) == 0:
            return False
        else:
            return True
    def selectFolder(self):
        folderaux = filedialog.askdirectory()
        if (folderaux == ""):
            if self.miInspector.getfolder() == "":
                messagebox.showinfo(message="You choose cancel\nNo folder selected yet", title="Warning")
            else:
                messagebox.showinfo(message="You choose cancel\nThe current monitor folder is: "+ self.miInspector.getfolder(), title="Warning")
        else:
            self.folder = folderaux
            if self.validemptyfolder():                
                self.miInspector.setfolder(self.folder)
                self.miInspector.clearlists()
            else:
                messagebox.showerror(message="The selected folder is empty, select another please.", title="Empty folder")          
        
    def startlooking(self):
                
        self.folder = self.miInspector.getfolder()
        if self.validemptyfolder(): 
            confirmation = messagebox.askyesno(message="Are you sure to start folder looking?", title="Confirmation")
            if(confirmation):
                self.MiMonitor.clearfiles()
                try:
                    
                    self.MiMonitor.setfolder(self.miInspector.getfolder())
                    self.MiMonitor.lookingfiles()
                    monitorfiles = self.MiMonitor.getfiles()
            
                    self.miInspector.setfileslist(monitorfiles)
                    self.miInspector.organizefiles()               
                    messagebox.showinfo(message="You can find the results in:\n"+os.getcwd(),title="Looking successfully")
                except Exception as errmsg:
                    self.miInspector.clearlists()
                    serrmsg = "An error occurred while inspecting the folder. Be sure if all files are closed.\n"+str(errmsg)
                    messagebox.showerror(message=serrmsg,title="Inspector Error")
        else:
            messagebox.showerror(message="The selected folder is empty, select another please.", title="Empty folder")
        