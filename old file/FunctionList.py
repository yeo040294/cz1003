from tkinter import *

def tick():
    import time
    time1 = ''
    time2 = time.strftime('%a, %d %b %y %H:%M:%S') # get the current local time from the PC
    if time2 != time1: # if time string has changed, update it
        time1 = time2
        clock.config(text=time2)

    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)

def StallList(index): #Returns all unique values in .csv (e.g. Stall List or Weekdays)
    import csv
    listof = set() #set() is a method to help identify unique values
    with open("Menu.csv") as file_pointer:
        csv_pointer = csv.reader(file_pointer)
        for row in csv_pointer:
            listof.add(row[index])
    return list(listof)

def getStallListByDay(day):
    import csv
    listof = set()
    with open("Menu.csv") as file_pointer:
        csv_pointer = csv.reader(file_pointer)
        for row in csv_pointer:
            if row[0] == day:
                listof.add(row[1])
    return list(listof)


def MenuTypeByHour(hour):
    from datetime import datetime
    time = int(hour)
    menutype = ["Breakfast", "Lunch & Dinner"]
    if time >= 9 and time < 12:
        return menutype[0]
    elif time >= 12 and time < 20:
        return menutype[1]
    else:
        return

def MenuType():
    from datetime import datetime
    time = int(datetime.now().strftime("%H"))
    menutype = ["Breakfast", "Lunch & Dinner"]
    if time > 9 and time < 12:
        return menutype[0]
    elif time >= 12 and time < 20:
        return menutype[1]
    else:
        return


def getMenu(menutype , day , stall):
    print('at getMenu')
    print(menutype)
    print(day)
    print(stall)
    import csv
    from datetime import datetime
    from collections import defaultdict
    with open("Menu.csv") as file_pointer:
        csv_pointer = csv.reader(file_pointer)
        for row in csv_pointer:
            print(row[0])
            print(row[1])
            if row[0] == day and row[1] == stall:
                if menutype == "Breakfast":
                    return row[2]
                elif menutype == "Lunch & Dinner":
                    return row[3]    
        

def Menu(menutype, day, stall): #Find breakfast or lunch menu based on day and stall name
    import csv
    from datetime import datetime
    from collections import defaultdict
    with open("Menu.csv") as file_pointer:
        csv_pointer = csv.reader(file_pointer)
        #menutype = MenuType()
        newdict = {}
        if menutype == "Breakfast":
            for each in csv_pointer:
                newdict.setdefault(each[0], {})[each[1]] = each[2]
        elif menutype == "Lunch & Dinner":
            for each in csv_pointer:
                newdict.setdefault(each[0], {})[each[1]] = each[3]
        else:
            return
        query = newdict[day][stall]
        return query

def DisplayMenu(window , menutype, day, stall): #To display all food and prices for a particular stall
    itemlist = getMenu(menutype, day, stall)
    print(itemlist)
    if itemlist == None:
        label = Label(window, text="Closed", font=("arial 10")).pack()
    else:
        itemlist = itemlist.split(", ")
        food = [i.split(" / ")[0] for i in itemlist]
        price = [float(i.split(" / ")[1]) for i in itemlist]
        count = 1
        for index, item in enumerate(food):
            display = str(count) + ". {:<10s}    ${:.2f}".format(item, price[index])
            label = Label(window, text=display, font=("arial 10")).pack()
            count += 1
    return label

