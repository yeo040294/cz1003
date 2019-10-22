from tkinter import *

def StallList(index): #Returns all unique values in .csv (e.g. Stall List or Weekdays)
    import csv
    listof = set() #set() is a method to help identify unique values
    with open("Menu.csv") as file_pointer:
        csv_pointer = csv.reader(file_pointer)
        for row in csv_pointer:
            listof.add(row[index])
    return list(listof)

def Menu(menutype, day, stall): #Find breakfast or lunch menu based on day and stall name
    import csv
    from datetime import datetime
    from collections import defaultdict
    with open("Menu.csv") as file_pointer:
        csv_pointer = csv.reader(file_pointer)
        newdict = {}
        if menutype == "Breakfast":
            for each in csv_pointer:
                newdict.setdefault(each[0], {})[each[1]] = each[2]
        else:
            for each in csv_pointer:
                newdict.setdefault(each[0], {})[each[1]] = each[3]
        query = newdict[day][stall]
        return query

def DisplayMenu(window , menutype, day, stall): #To display all food and prices for a particular stall
    itemlist = Menu(menutype, day, stall).split(", ")
    food = [i.split(" / ")[0] for i in itemlist]
    price = [float(i.split(" / ")[1]) for i in itemlist]
    count = 1
    for index, item in enumerate(food):
        display = str(count) + ". {:<10s}    ${:.2f}".format(item, price[index])
        label = Label(window, text=display, font=("arial 10")).pack()
        count += 1
    return label
