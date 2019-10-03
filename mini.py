from tkinter import *
from datetime import datetime





window = Tk()
window.title("CZ1003 Mini Project")
window.geometry("500x400")

time = StringVar()
mainpage= StringVar()
Mainpage = Label( window, textvariable=mainpage, font = ("arial 15 bold italic"), relief=RAISED )
mainpage.set("Welcome to NTU NorthSpine Food Section")

logo = PhotoImage(file= "canteen.ppm")




currenttime = Label( window, textvariable=time, font = ("arial 10 bold italic"))
time.set(datetime.now().strftime("%a, %d %b %Y %H:%M:%S"))


buttontoday = Button(window, text="View Today Menu")
buttonanotherday = Button(window, text="View Other Day Menu")
Mainpage.pack()
currenttime.pack()


frame = Frame(window, width= 400,height = 300)
frame.pack_propagate(0)
frame.pack()

Label(frame, image = logo) .pack(fill=BOTH)   #logo
buttontoday.pack()
buttonanotherday.pack()
window.mainloop()