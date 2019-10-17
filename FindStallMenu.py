def StallList(): #Returns all stalls in North Spine Food Court
    import csv
    listofstalls = set() #set() is a method to help identify unique values
    with open("Menu.csv") as file_pointer:
        csv_pointer = csv.reader(file_pointer)
        for row in csv_pointer:
            listofstalls.add(row[1])
    return list(listofstalls)

def BreakfastMenu(day,stall): #Find breakfast menu for stall on specified day
    import csv
    from datetime import datetime
    from collections import defaultdict
    with open("Menu.csv") as file_pointer:
        csv_pointer = csv.reader(file_pointer)
        newdict = {}
        for each in csv_pointer:
            newdict.setdefault(each[0], {})[each[1]] = each[2]
        query = newdict[day][stall]
    return query

def LunchDinnerMenu(day,stall): #Find lunch and dinner menu for stall on specified day
    import csv
    from datetime import datetime
    from collections import defaultdict
    with open("Menu.csv") as file_pointer:
        csv_pointer = csv.reader(file_pointer)
        newdict = {}
        for each in csv_pointer:
            newdict.setdefault(each[0], {})[each[1]] = each[3]
        query = newdict[day][stall]
    return query