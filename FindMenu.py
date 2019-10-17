def BreakfastMenu(day,stall): #Find breakfast menu for stall on specified day
    import csv
    from datetime import datetime
    from collections import defaultdict
    with open("Menu.csv") as file_pointer:
        csv_pointer = csv.reader(file_pointer)
        newdict = {}
        for each in csv_pointer:
            newdict.setdefault(each[0], {})[each[1]] = each[2]
            if each[3] == "":
                del newdict[]

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