#Import all relevant modules and packages
from FunctionList import *
from datetime import *
import csv
from tkinter import *
import StoreMenu_Screen4
from functools import partial

day = ''
user_input = ''
dayOfWeek =''
minute = ''
hour = ''

def passUserInfo(v1, v2 ,min,hr):
    global day
    global user_input
    global dayOfWeek
    global minute
    global hour
    minute = min
    hour = hr
    day = v1
    user_input = v2
    dayOfWeek = datetime.strptime(user_input, '%b%d%Y').strftime('%A')

def screen(currentDay):

    global day
    global user_input
    global dayOfWeek
    global minute
    global hour

    window = Tk()
    window.title("Choose Store to Query")
    window.geometry("700x420")

    if currentDay:
        print('currentday is true')
        timeNow = datetime.now().strftime("%b%d%Y")
        dayOfWeek = datetime.strptime(timeNow , '%b%d%Y').strftime('%A')
        hour = datetime.now().strftime("%H")
        minute = datetime.now().strftime("%M")
        dateNow = dayOfWeek + ' ' + hour + ':' + minute

    else:
        dateNow = user_input + ' , ' + dayOfWeek + ' ' + hour + ':' + minute

    #Formatting
    time, subpage2 = StringVar(), StringVar()
    Subpage2 = Label(window, text= "Select a store from the following options" , font = ("arial 15 bold italic")).pack()
    #currenttime = Label(window, text = datetime.now().strftime("%a, %d %b %Y %H:%M:%S"), font = ("arial 10 bold italic")).pack()
    currenttime = Label(window, text = dateNow, font = ("arial 10 bold italic")).pack()


    btn_list =[]
    
        
    def openScreen3(stallName):
        StoreMenu_Screen4.create(stallName , dayOfWeek , hour , minute)

    #Creating buttons
    for i in getStallListByDay(dayOfWeek):
        print(i)
        if i == "":
            pass
        else:
            Button(window, text=i , command =partial(openScreen3,i)).pack(side="bottom", padx=10, pady=10)
        

    window.mainloop()
