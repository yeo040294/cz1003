from tkinter import *
import time


def amended (): 

    window = Tk()
    window.title("Set a Date")
    window.geometry("700x420")




    DATE=[ Date for Date in range(1,32)]
        
    MONTH = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ] #etc


    YEAR = [Year for Year in range (2019, 2031)]



    HOUR = [
    "07",
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21"
    ] #etc


    MIN = [ 
    "00",
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31",
    "32",
    "33",
    "34",
    "35",
    "36",
    "37",
    "38",
    "39",
    "40",
    "41",
    "42",
    "43",
    "44",
    "45",
    "46",
    "47",
    "48",
    "49",
    "50",
    "51",
    "52",
    "53",
    "54",
    "55",
    "56",
    "57",
    "58",
    "59"
    ]



    



    

    Label(window, text = "CHOOSE A DATE", font=("Times", 40)).pack()


    
    


    variable2 = StringVar(window)
    variable2.set(DATE[0])

    date = OptionMenu(window, variable2, *DATE)
    date.configure(font=(20))
    date.place(x=150, y = 200)

    variable = StringVar(window)
    variable.set(MONTH[0]) # default value

    month = OptionMenu(window, variable, *MONTH)
    month.configure(font=(20))
    month.place(x=200, y=200)

    variable3 = StringVar(window)
    variable3.set(YEAR[0])
    year = OptionMenu(window, variable3, *YEAR)
    year.configure(font=(20))
    year.place(x=270, y=200)


    variable4 = StringVar(window)
    variable4.set(HOUR[0])

    hour = OptionMenu(window, variable4, *HOUR)
    hour.configure(font=(20))
    hour.place(x=450, y = 200)

    Label(window, text = ":", font=("Times", 11)).place(x=945, y =300)

    variable5 = StringVar(window)
    variable5.set(MIN[0]) # default value

    min = OptionMenu(window, variable5, *MIN)
    min.configure(font=(20))
    min.place(x=510, y=200)





    def ok():
        print("Date is:" + variable2.get()+variable.get()+variable3.get())
        print("Time is:" + variable4.get()+variable5.get())


    button = Button(window, text="Next", font= 7, width = (15), command=ok)
    #button.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)
    button.place(x=100, y=300)


    button = Button(window, text="Back", font= 7, width = (15), command=window.destroy)
    button.place(x=400, y=300)

    #clock format
   
  
   

    
    


    mainloop()










