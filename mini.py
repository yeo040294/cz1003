from tkinter import *
import time

window = Tk()

time1 = ''
clock = Label(window, font=('times', 20, 'bold'), bg= 'green')
clock.pack(fill=BOTH, expand=1)
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
window.geometry("500x430")

mainpage= StringVar()
Mainpage = Label( window, textvariable=mainpage, font = ("arial 15 bold italic"), relief=RAISED )
mainpage.set("Welcome to NTU NorthSpine Food Section")

logo = PhotoImage(file= "canteen.ppm")







buttontoday = Button(window, text="View Today Menu")
buttonanotherday = Button(window, text="View Other Day Menu")
Mainpage.pack()



frame = Frame(window, width= 400,height = 300)
frame.pack_propagate(0)
frame.pack()

Label(frame, image = logo) .pack(fill=BOTH)   #logo
buttontoday.pack()
buttonanotherday.pack()
window.mainloop()