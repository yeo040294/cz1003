from tkinter import *
import tkinter as tk
import time
from itertools import chain, cycle


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





class App(tk.Tk):
    '''Tk window/label adjusts to size of image'''
    def __init__(self, image_files, x, y, delay):
        # the root will be self
        tk.Tk.__init__(self)
        # set x, y position only
        self.geometry('+{}+{}'.format(x, y))
        self.delay = delay
        # allows repeat cycling through the pictures
        # store as (img_object, img_name) tuple
        self.pictures = cycle((tk.PhotoImage(file=image), image)
                              for image in image_files)
        self.picture_display = tk.Label(self)
        self.picture_display.pack()
    def show_slides(self):
        '''cycle through the images and show them'''
        # next works with Python26 or higher
        img_object, img_name = next(self.pictures)
        self.picture_display.config(image=img_object)
        # shows the image filename, but could be expanded
        # to show an associated description of the image
        self.title(img_name)
        self.after(self.delay, self.show_slides)
    def run(self):
        self.mainloop()







window.title("CZ1003 Mini Project")
window.geometry("700x520")

mainpage= StringVar()
Mainpage = Label( window, textvariable=mainpage, font = ("arial 20 bold italic"))#, relief=RAISED 
mainpage.set("Welcome to NTU NorthSpine Food Section")

logo = PhotoImage(file= "rsz_1panda_face.ppm")



buttontoday = Button(window, text="View Today Menu",font = 8, width=(20) )
buttonanotherday = Button(window, text="View Other Day Menu", font = 8, width=(20))
Mainpage.pack()





delay = 3500
# get a series of gif images you have in the working folder
# or use full path, or set directory to where the images are
image_files = [
'rsz_1panda_face.ppm',
'canteen.ppm',
'panda_face.ppm'
]
# upper left corner coordinates of app window
x = 100
y = 50
app = App(image_files, x, y, delay)
app.show_slides()
app.run()




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