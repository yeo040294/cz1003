#Import all relevant modules and packages
from FunctionList import *
from datetime import *
import csv
from tkinter import *

def create(stallName , dayOfWeek, hour , minute):
    window = Toplevel()
    #Window Size
    window.title("Store Query")
    window.geometry("700x420")
    
    menutype = MenuTypeByHour(hour)
    print(menutype)
    print(hour)
    print(minute)
    print(dayOfWeek)
    print(stallName)

    dateNow =  dayOfWeek + ' ' + hour + ':' + minute


    #Formatting
    time, subpage2 = StringVar(), StringVar()
    Subpage2 = Label(window, textvariable=subpage2, font = ("arial 15 bold italic")).pack()
    subpage2.set("Store Information")
    #currenttime = Label(window, textvariable=time, font = ("arial 10 bold italic")).pack()
    currenttime = Label(window, textvariable=dateNow, font = ("arial 10 bold italic")).pack()
    time.set(datetime.now().strftime("%a, %d %b %Y %H:%M:%S"))

    #Display
    today = StallList(0)[datetime.today().weekday()]
    DisplayMenu(window,menutype, dayOfWeek, stallName)

def show():
    window = Toplevel()
    window.mainloop()


