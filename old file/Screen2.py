#Import all relevant modules and packages
from FindStallMenu import *
from datetime import *
import csv
from tkinter import *

import Screen3 as scr3
from functools import partial

def screen():

    window = Tk()
    #root Size
    window.title("Choose Store to Query")
    window.geometry("500x400")

    #Formatting
    time, subpage2 = StringVar(), StringVar()
    Subpage2 = Label(window, text= "Select a store from the following options" , font = ("arial 15 bold italic")).pack()
    
    currenttime = Label(window, text = datetime.now().strftime("%a, %d %b %Y %H:%M:%S"), font = ("arial 10 bold italic")).pack()
    

    btn_list =[]

    count = 0
        
    def openScreen3(stallName):
        scr3.create(stallName)

    #Creating buttons
    for i in StallList(1):
        print(i)
        if i == "":
            pass
        else:
            Button(window, text=i , command =partial(openScreen3,i)).pack(side="bottom", padx=10, pady=10)
        

    window.mainloop()
