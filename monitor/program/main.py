"""
Code to start main menu of the application with tkinter GUI
Author: Andrey Fabián Picado Arias - Costa Rica participant to apply Genpact
Last modified: 05/24/2022 8:20 pm 
"""

from tkinter import *
import tkinter as tk

from director import Director

class Main:
    def __init__(self):
        WIDTH,LARGE=400,400 
        director = Director()
        tkwindow = Tk()
        widthwindow = tkwindow.winfo_screenwidth()
        largewindow = tkwindow.winfo_screenheight()
        POS_WINDOW_X = int((widthwindow/2) - (WIDTH/2))
        POS_WINDOW_Y = int((largewindow/2) - (LARGE/2))
        tkwindow.title("Folder Watcher")
        tkwindow.geometry("{}x{}+{}+{}".format(WIDTH,LARGE, POS_WINDOW_X, POS_WINDOW_Y))
        tkwindow.resizable(width=False, height=False)
        tkwindow.config(bg="gray")
        label1 = tk.Label(tkwindow, text="Welcome to file watcher\nand excel copy.",bg="gray", fg="light blue",
                          font=("Arial", 20, "italic"))
        label1.pack()
        label2 = tk.Label(tkwindow, text="By Andrey Picado Arias.",bg="gray", fg="white",
                          font=("Arial", 10, "italic"))
        label2.pack()
        label3 = tk.Label(tkwindow, bg="gray", fg="black", text = "\n\nPlease select a folder.\n",
                          font=("Arial", 15,))
        label3.pack()
        label4 = tk.Label(tkwindow, bg="gray", fg="black", text = "\n\nPlease select a folder.\n",
                          font=("Arial", 9))
        label4.pack()
        def getfolder():
            director.selectFolder()
            label3['text'] = "\n\nYour actual folder is:\n"
            label4['text'] = director.getfolder()
            
        btnselect = tk.Button(tkwindow,text="Choose folder to watch",bg="cyan",
                            width=20,height=3,
                            command=getfolder)
        btnstart = tk.Button(tkwindow,text="Start folder looking",bg="salmon",
                            width=20,height=3,
                            command=director.startlooking)
        btnselect.place(x=WIDTH//12,y=LARGE/1.3)

        btnstart.place(x=WIDTH//1.8,y=LARGE/1.3)

        tkwindow.mainloop()
        
Main()