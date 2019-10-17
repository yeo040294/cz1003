from tkinter import *
import time
from itertools import chain


window = Tk()

time1 = ''
clock = Label(window, font=('times', 15, 'bold'))

def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%a, %d %b %y %H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)
tick()

window.title("CZ1003 Mini Project")
window.geometry("700x520")

mainpage= StringVar()
Mainpage = Label( window, textvariable=mainpage, font = ("arial 20 bold italic"))#, relief=RAISED 
mainpage.set("Welcome to NTU NorthSpine Food Section")

logo = PhotoImage(file= "rsz_1panda_face.ppm")



buttontoday = Button(window, text="View Today Menu",font = 8, width=(20) )
buttonanotherday = Button(window, text="View Other Day Menu", font = 8, width=(20))
Mainpage.pack()



frame = Frame(window, width= 400,height = 300)
frame.pack_propagate(0)
frame.pack()
frame.place(x= 10, y= 60)
Label(frame, image = logo) .pack(fill=BOTH)   #logo
clock.pack() 
clock.place(x= 280, y= 360)
buttontoday.pack()
buttontoday.place(x= 400, y= 120)
buttonanotherday.pack()
buttonanotherday.place(x= 400, y= 220)
window.mainloop()