from tkinter import *


DATE = [
"1",
"2",
"3",
"4",
"5",
"6",
"7",
"8",
"9",
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
] #etc

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



YEAR = [
"2019",
"2020",
"2021",
"2022",
"2023",
"2024",
"2025",
"2026",
"2027",
"2028",
"2029",
"2030",
] #etc


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



master = Tk()


Label(master, text = "CHOOSE A DATE", font=("Times", 40)).pack()


variable2 = StringVar(master)
variable2.set(DATE[0])

date = OptionMenu(master, variable2, *DATE)
date.place(x=400, y = 300)

variable = StringVar(master)
variable.set(MONTH[0]) # default value

month = OptionMenu(master, variable, *MONTH)
month.place(x=437, y=300)

variable3 = StringVar(master)
variable3.set(YEAR[0])
year = OptionMenu(master, variable3, *YEAR)
year.place(x=487, y=300)


variable4 = StringVar(master)
variable4.set(HOUR[0])

hour = OptionMenu(master, variable4, *HOUR)
hour.place(x=900, y = 300)

Label(master, text = ":", font=("Times", 11)).place(x=945, y =300)

variable5 = StringVar(master)
variable5.set(MIN[0]) # default value

min = OptionMenu(master, variable5, *MIN)
min.place(x=955, y=300)




def ok():
    print("Date is:" + variable2.get()+variable.get()+variable3.get())
    print("Time is:" + variable4.get()+variable5.get())


button = Button(master, text="Next", command=ok)
button.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)

mainloop()









