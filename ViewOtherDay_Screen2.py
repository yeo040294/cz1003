from tkinter import *
from datetime import datetime, time
import calendar
import StoreList_Screen3

user_input = ''
day = ''
dayValue = ''
monthValue = ''
yearValue = ''
hourValue = ''
minuteValue = ''

def screen():

    def monthTrace(*args):
        global monthValue
        monthValue = mnthvar.get()
        setUserInput()

    def dayTrace(*args):
        global dayValue
        dayValue = datevar.get()
        setUserInput()
    
    def yearTrace(*args):
        global yearValue
        yearValue = yrvar.get()
        setUserInput()

    def hourTrace(*args):
        global hourValue
        hourValue = hrvar.get()

    def minuteTrace(*args):
        global minuteValue
        minuteValue = minvar.get()

    def setUserInput():
        global monthValue
        global dayValue
        global yearValue
        global user_input
        user_input = dayValue + monthValue + yearValue

    window = Tk()
    window.title("Set a Date")
    window.geometry("700x420")

    DATE = [Date for Date in range(1,32)]
    MONTH = [Month[:3] for Month in calendar.month_name]
    YEAR = [Year for Year in range (2019, 2031)]
    HOUR = [Hour for Hour in range (9, 22)]
    MIN = ['00','05','10','15','20','25','30','35','40','45','50','55']

    Label(window, text = "Choose a Date", font = ("arial 30 bold italic")).pack()
    
    datevar = StringVar(window)
    datevar.set(DATE[0])
    datevar.trace("w" , dayTrace)

    date = OptionMenu(window, datevar, *DATE)
    date.configure(font=(20))
    date.place(x=150, y = 200)

    mnthvar = StringVar(window)
    mnthvar.set(MONTH[1]) # default value
    mnthvar.trace("w" , monthTrace)

    month = OptionMenu(window, mnthvar, *MONTH )
    month.configure(font=(20))
    month.place(x=200, y=200)
    
    yrvar = StringVar(window)
    yrvar.set(YEAR[0])
    yrvar.trace("w" , yearTrace)

    year = OptionMenu(window, yrvar, *YEAR)
    year.configure(font=(20))
    year.place(x=270, y=200)
 
    hrvar = StringVar(window)
    hrvar.set(HOUR[0])
    hrvar.trace("w" , hourTrace)

    hour = OptionMenu(window, hrvar, *HOUR)
    hour.configure(font=(20))
    hour.place(x=450, y = 200)

    Label(window, text = ":", font=("Times", 11)).place(x=945, y =300)

    minvar = StringVar(window)
    minvar.set(MIN[0]) # default value
    minvar.trace("w",minuteTrace)
    
    min = OptionMenu(window, minvar, *MIN)
    min.configure(font=(20))
    min.place(x=510, y=200)

    global monthValue
    global dayValue
    global yearValue
    global minuteValue
    global hourValue
    global user_input

    minuteValue = minvar.get()
    hourValue = hrvar.get()
    monthValue = mnthvar.get()
    dayValue = datevar.get()
    yearValue = yrvar.get()

    user_input = datevar.get() + " "+ mnthvar.get()+ " "+ yrvar.get()
    global day
    day = datetime.strptime(user_input, '%d %b %Y').strftime('%A')
    button = Button(window, text="Next", font= 7, width = (15), command=openScreen3)
    #button.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)
    button.place(x=100, y=300)

    button = Button(window, text="Back", font= 7, width = (15), command=window.destroy)
    button.place(x=400, y=300)

    #clock format

    mainloop()

def openScreen3():

    global user_input
    global day

    StoreList_Screen3.passUserInfo(day,user_input , minuteValue , hourValue)
    StoreList_Screen3.screen(False)
 

 



