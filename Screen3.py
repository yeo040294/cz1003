#Import all relevant modules and packages
from FindStallMenu import *
from datetime import *
import csv
from tkinter import *


def create(stallName):
    window = Toplevel()
    #Window Size
    window.title("Store Query")
    window.geometry("500x400")
 
    #Formatting
    time, subpage2 = StringVar(), StringVar()
    Subpage2 = Label(window, textvariable=subpage2, font = ("arial 15 bold italic")).pack()
    subpage2.set("Store Information")
    currenttime = Label(window, textvariable=time, font = ("arial 10 bold italic")).pack()
    time.set(datetime.now().strftime("%a, %d %b %Y %H:%M:%S"))

    #Display
    today = StallList(0)[datetime.today().weekday()]
    DisplayMenu(window,"Lunch", today, stallName)

def show():
    window = Toplevel()
    window.mainloop()


