#Import all relevant modules and packages
from FindStallMenu import *
from datetime import *
import csv
from tkinter import *
window = Tk()
import Screen3 as scr3
from functools import partial

 
#root Size
window.title("Choose Store to Query")
window.geometry("500x400")

#Formatting
time, subpage2 = StringVar(), StringVar()
Subpage2 = Label(window, textvariable=subpage2, font = ("arial 15 bold italic")).pack()
subpage2.set("Select a store from the following options")
currenttime = Label(window, textvariable=time, font = ("arial 10 bold italic")).pack()
time.set(datetime.now().strftime("%a, %d %b %Y %H:%M:%S"))

btn_list =[]
    
def openScreen3(stallName):
    scr3.create(stallName)

#Creating buttons
for i in StallList(1):
    if i == "":
        pass
    else:
        Button(window, text=i , command=partial(openScreen3,i)).pack(side="bottom", padx=10, pady=10)

window.mainloop()