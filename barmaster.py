from tkinter import *
from tkinter import ttk, messagebox
from functools import partial
from datetime import datetime
from PIL import ImageTk, Image
import random


BARSTORAGE = {
    "ingredients": {
        "vodka": 125,
        "bourbon": 125,
        "bitters": 125,
        "tequila": 125,
        "cointreau": 125,
        "limejuice": 125,
        "cranberryjuice": 125,
        "gin": 125,
        "campari": 125,
        "vermouth": 125,
        "gingerbeer": 125,
        "rum": 125,
        "whiskey": 125,
        "simplesyrup": 125,
        "lemonjuice": 125,
    },
    "employees": {},
}

"""
Create Window Function: create_window()
    This function is responsible for the generation of the tkinter "Window" object, which is returned by this function
"""


def createWindow(width, height):

    window = Tk()
    window.title("BarMaster POS")
    window.geometry(str(width) + "x" + str(height))

    return window


def changeClock(empid, window):
    login = empid.get()
    if BARSTORAGE["employees"][login]["onClock"] == 0:
        BARSTORAGE["employees"][login]["onClock"] = 1
        BARSTORAGE["employees"][login]["clockin"] = datetime.now()
        window.destroy()
        clockinWindow = createWindow(100, 100)
        clockinSuccess = Label(clockinWindow, text="Successful clockin").grid(
            row=0, column=0
        )
    else:
        BARSTORAGE["employees"][login]["onClock"] = 0
        clockinTime = BARSTORAGE["employees"][login]["clockin"]
        difference = datetime.now() - clockinTime
        seconds = difference.total_seconds()
        differenceInHours = seconds / 3600
        BARSTORAGE["employees"][login]["hours"] += differenceInHours
        window.destroy()
        clockoutWindow = createWindow(400, 100)
        clockoutSuccess = Label(
            clockoutWindow,
            text=f"Successful clockout, hours worked: {differenceInHours}",
        ).grid(row=0, column=0)


def clockIn():
    clockinWindow = createWindow(100, 100)
    loginIDLabel = Label(clockinWindow, text="Employee ID: ").grid(row=0, column=0)
    loginID = Entry(clockinWindow)
    loginID.grid(row=0, column=1)

    clockinButton = Button(
        clockinWindow,
        text="Clock In",
        command=(lambda: changeClock(loginID, clockinWindow)),
    )
    clockinButton.grid(row=1, column=0)


def clockOut():
    clockoutWindow = createWindow(100, 100)
    loginIDLabel = Label(clockoutWindow, text="Employee ID: ").grid(row=0, column=0)
    loginID = Entry(clockoutWindow)
    loginID.grid(row=0, column=1)

    clockoutButton = Button(
        clockoutWindow,
        text="Clock Out",
        command=(lambda: changeClock(loginID, clockoutWindow)),
    )
    clockoutButton.grid(row=1, column=0)


def displayInventory():
    return 1


def addInventory():
    return 1


def displaySales():
    return 1


def repeatOrder():
    return 1


"""
Phone Formatting Function: phoneFormat()
    - This function is responsible for checking to see if the phone number entered by the user is in the proper format
    - This function takes in a string "p", and checks to make sure there are correct "-" characters in the correct positions for a phone number
        - if in good format, returns True
"""


def phoneFormat(p):
    # format: ### - ### - ####
    if len(p.get()) == 12 and p.get()[3] == "-" and p.get()[7] == "-":
        return True
    else:
        return False


"""
Filter Bad Characters Function: catchBadChar()
    - This function is responsible for the detection of forbidden characters in the entries made by the user
    - This function takes in a string, and compares each character of that string, against each forbidden character, and if there
       is no match, it moves on to the next character in the passed string.
"""


def catchBadChar(testString):
    symbols = {
        "~",
        ":",
        "'",
        "+",
        "[",
        "\\",
        "@",
        "^",
        "{",
        "%",
        "(",
        '"',
        "*",
        "|",
        ",",
        "&",
        "<",
        "`",
        "}",
        ".",
        "_",
        "=",
        "]",
        "!",
        ">",
        ";",
        "?",
        "#",
        "$",
        ")",
        "/",
    }
    flag = True

    for character in testString:
        for badChar in symbols:
            if character == badChar:
                flag = False

    return flag


"""
Employee ID Generation Function: generate_empid()
    This function is responsible for the generation of the employee's random and individual ID number
        - The ID is returned as a string object
"""


def generateEmpId():
    empid = ""

    for i in range(0, 4):
        if random.random() < 0.5:
            char = chr(random.randint(48, 57))
        else:
            char = chr(random.randint(65, 90))

        empid += char

    return empid


def commitEmployee(efname, elname, eemail, ephone, empWindow):
    add_flag = 1
    newEmployeeFirstName = efname.get()
    newEmployeeLastName = elname.get()
    newEmployeeEmail = eemail.get()
    newEmployeePhone = ephone.get()
    newEmployeeID = generateEmpId()

    if efname.get() == "":
        Label(empWindow, text="Empty Field").grid(row=0, column=2)
        add_flag = 0
    else:
        if catchBadChar(efname.get()):
            add_flag = 1
        else:
            Label(empWindow, text="Forbidden Character Detected").grid(row=0, column=2)

    if elname.get() == "":
        Label(empWindow, text="Empty Field").grid(row=1, column=2)
        add_flag = 0
    else:
        if catchBadChar(elname.get()):
            add_flag = 1
        else:
            Label(empWindow, text="Forbidden Character Detected").grid(row=1, column=2)

    if ephone.get() == "":
        Label(empWindow, text="Empty Field").grid(row=3, column=2)
        add_flag = 0
    else:
        if phoneFormat(ephone) == 0:
            Label(empWindow, text="Invalid Phone Number").grid(row=3, column=2)
            add_flag = 0
        elif catchBadChar(ephone.get()) == 0:
            add_flag = 0
        else:
            Label(empWindow, text="Forbidden Character Detected").grid(row=3, column=2)
    if add_flag:
        BARSTORAGE["employees"][newEmployeeID] = {
            "empid": newEmployeeID,
            "fname": newEmployeeFirstName,
            "lname": newEmployeeLastName,
            "email": newEmployeeEmail,
            "phone": newEmployeePhone,
            "hours": 0.0,
            "onClock": 0,
            "clockin": datetime.now(),
        }

    else:
        return 0
    empWindow.destroy()
    generateEmployee()
    print(BARSTORAGE["employees"])


def deleteEmployee(empid, empwindow):
    BARSTORAGE["employees"].pop(empid)
    empwindow.destroy()
    generateEmployee()


def generateEmployee():
    empWindow = createWindow(800, 600)

    fnameLabel = Label(empWindow, text="First Name:").grid(row=0, column=0)
    lnameLabel = Label(empWindow, text="Last Name:").grid(row=1, column=0)
    emailaddrLabel = Label(empWindow, text="Email Address:").grid(row=2, column=0)
    phonenumberLabel = Label(empWindow, text="Phone Number:").grid(row=3, column=0)

    fname1 = Entry(empWindow)
    fname1.grid(row=0, column=1)

    lname1 = Entry(empWindow)
    lname1.grid(row=1, column=1)

    emailaddr1 = Entry(empWindow)
    emailaddr1.grid(row=2, column=1)

    phonenumber1 = Entry(empWindow)
    phonenumber1.grid(row=3, column=1)

    addNewEmp = Button(
        empWindow,
        text="Add Employee",
        command=(
            lambda: commitEmployee(fname1, lname1, emailaddr1, phonenumber1, empWindow)
        ),
    )
    addNewEmp.grid(row=4, column=0)

    header1 = Label(empWindow, text="EmployeeID").grid(row=5, column=1, sticky="ew")
    header2 = Label(empWindow, text="First Name").grid(row=5, column=2, sticky="ew")
    header3 = Label(empWindow, text="Last Name").grid(row=5, column=3, sticky="ew")
    header4 = Label(empWindow, text="Email Address").grid(row=5, column=4, sticky="ew")
    header5 = Label(empWindow, text="Phone Number").grid(row=5, column=5, sticky="ew")
    header6 = Label(empWindow, text="Hours").grid(row=5, column=6, sticky="ew")

    employees = BARSTORAGE["employees"]

    rowTracker = 6

    for employeeID in employees:
        employee = employees[employeeID]

        deleteButton = Button(
            empWindow,
            text="Delete",
            command=(lambda: deleteEmployee(employee["empid"], empWindow)),
        )
        deleteButton.grid(row=rowTracker, column=0)

        id = Label(empWindow, text=employee["empid"]).grid(
            row=rowTracker, column=1, sticky="ew"
        )

        fname = Label(empWindow, text=employee["fname"]).grid(
            row=rowTracker, column=2, sticky="ew"
        )

        lname = Label(empWindow, text=employee["lname"]).grid(
            row=rowTracker, column=3, sticky="ew"
        )

        email = Label(empWindow, text=employee["email"]).grid(
            row=rowTracker, column=4, sticky="ew"
        )

        ephone = Label(empWindow, text=employee["phone"]).grid(
            row=rowTracker, column=5, sticky="ew"
        )

        hours = Label(empWindow, text=employee["hours"]).grid(
            row=rowTracker, column=6, sticky="ew"
        )

        rowTracker += 1

    empWindow.mainloop()


ORDER = {
    "ingredients": {
        "vodka": 0,
        "bourbon": 0,
        "bitters": 0,
        "tequila": 0,
        "cointreau": 0,
        "limejuice": 0,
        "cranberryjuice": 0,
        "gin": 0,
        "campari": 0,
        "vermouth": 0,
        "gingerbeer": 0,
        "rum": 0,
        "whiskey": 0,
        "simplesyrup": 0,
        "lemonjuice": 0,
    },
    "server": "",
}


def addToOrder(drinkName):
    if drinkName == "OldFashioned":
        ORDER["ingredients"]["bourbon"] += 2
        ORDER["ingredients"]["bitters"] += 1

    elif drinkName == "Margarita":
        ORDER["ingredients"]["tequila"] += 2
        ORDER["ingredients"]["cointreau"] += 1
        ORDER["ingredients"]["limejuice"] += 1

    elif drinkName == "Cosmopolitan":
        ORDER["ingredients"]["vodka"] += 2
        ORDER["ingredients"]["cointreau"] += 1
        ORDER["ingredients"]["limejuice"] += 1
        ORDER["ingredients"]["cranberryjuice"] += 1

    elif drinkName == "Negroni":
        ORDER["ingredients"]["gin"] += 1
        ORDER["ingredients"]["campari"] += 1
        ORDER["ingredients"]["vermouth"] += 1

    elif drinkName == "MoscowMule":
        ORDER["ingredients"]["vodka"] += 2
        ORDER["ingredients"]["gingerbeer"] += 5
        ORDER["ingredients"]["limejuice"] += 1

    elif drinkName == "Martini":
        ORDER["ingredients"]["gin"] += 3
        ORDER["ingredients"]["vermouth"] += 1

    elif drinkName == "Mojito":
        ORDER["ingredients"]["rum"] += 2
        ORDER["ingredients"]["limejuice"] += 1
        ORDER["ingredients"]["simplesyrup"] += 2

    elif drinkName == "WhiskeySour":
        ORDER["ingredients"]["whiskey"] += 2
        ORDER["ingredients"]["lemonjuice"] += 1

    elif drinkName == "Manhattan":
        ORDER["ingredients"]["whiskey"] += 2
        ORDER["ingredients"]["vermouth"] += 1
        ORDER["ingredients"]["bitters"] += 1

    elif drinkName == "Daiquiri":
        ORDER["ingredients"]["rum"] += 2
        ORDER["ingredients"]["simplesyrup"] += 2
        ORDER["ingredients"]["limejuice"] += 2

    print(ORDER)


if __name__ == "__main__":

    window = createWindow(1200, 1000)

    # Creating PhotoImage objects from the drink images
    cosImg = PhotoImage(file="drinkphotos/coffee.png")
    daqIm = PhotoImage(file="drinkphotos/coffee.png")
    manIm = PhotoImage(file="drinkphotos/coffee.png")
    margIm = PhotoImage(file="drinkphotos/coffee.png")
    martIm = PhotoImage(file="drinkphotos/coffee.png")
    mojIm = PhotoImage(file="drinkphotos/coffee.png")
    mosIm = PhotoImage(file="drinkphotos/coffee.png")
    negIm = PhotoImage(file="drinkphotos/coffee.png")
    olfIm = PhotoImage(file="drinkphotos/coffee.png")
    wsrIm = PhotoImage(file="drinkphotos/coffee.png")

    # Resizing the PhotoImage objects
    cosIm = cosImg.subsample(5, 5)
    daquiIm = daqIm.subsample(5, 5)
    manhatIm = manIm.subsample(5, 5)
    margaIm = margIm.subsample(5, 5)
    martiIm = martIm.subsample(5, 5)
    mojiIm = mojIm.subsample(5, 5)
    moscoIm = mosIm.subsample(5, 5)
    negroniIm = negIm.subsample(5, 5)
    oldfIm = olfIm.subsample(5, 5)
    whiskIm = wsrIm.subsample(5, 5)

    # Drink buttons row 1
    cosmoButton = Button(
        window,
        image=cosIm,
        compound=TOP,
        text="Cosmopolitan",
        command=(lambda: addToOrder("Cosmopolitan")),
    ).grid(row=0, column=1, sticky="ew")

    daqButton = Button(
        window,
        text="Daquiri",
        image=daquiIm,
        compound=TOP,
        command=(lambda: addToOrder("Daiquiri")),
    ).grid(row=0, column=2, sticky="ew")
    manButton = Button(
        window,
        text="Manhattan",
        image=manhatIm,
        compound=TOP,
        command=(lambda: addToOrder("Manhattan")),
    ).grid(row=0, column=3, sticky="ew")

    margButton = Button(
        window,
        text="Margarita",
        image=margaIm,
        compound=TOP,
        command=(lambda: addToOrder("Margarita")),
    ).grid(row=0, column=4, sticky="ew")

    # Drink buttons row 2
    martButton = Button(
        window,
        image=martiIm,
        compound=TOP,
        text="Martini",
        command=(lambda: addToOrder("Martini")),
    ).grid(row=1, column=1, sticky="ew")

    mojButton = Button(
        window,
        text="Mojito",
        image=daquiIm,
        compound=TOP,
        command=(lambda: addToOrder("Mojito")),
    ).grid(row=1, column=2, sticky="ew")

    negroniButton = Button(
        window,
        text="Negroni",
        image=negroniIm,
        compound=TOP,
        command=(lambda: addToOrder("Negroni")),
    ).grid(row=1, column=3, sticky="ew")

    moscButton = Button(
        window,
        text="Moscow Mule",
        image=moscoIm,
        compound=TOP,
        command=(lambda: addToOrder("MoscowMule")),
    ).grid(row=1, column=4, sticky="ew")

    # Drink buttons row 3
    mojButton = Button(
        window,
        text="Mojito",
        image=oldfIm,
        compound=TOP,
        command=(lambda: addToOrder("Mojito")),
    ).grid(row=2, column=1, sticky="ew")

    negroniButton = Button(
        window,
        text="Negroni",
        image=whiskIm,
        compound=TOP,
        command=(lambda: addToOrder("Negroni")),
    ).grid(row=2, column=2, sticky="ew")

    # Clock in Button
    clockIn = Button(window, text="Clock In", command=clockIn).grid(
        row=0, column=0, sticky="ew"
    )

    # Clock out Button
    clockOut = Button(window, text="Clock Out", command=clockOut).grid(
        row=1, column=0, sticky="ew"
    )

    # Display Inventory Button
    viewInventory = Button(
        window, text="View Inventory", command=displayInventory
    ).grid(row=2, column=0, sticky="ew")

    # Add to Inventory Button
    fillInventory = Button(window, text="Add to Inventory", command=addInventory).grid(
        row=3, column=0, sticky="ew"
    )

    # View Sales Button
    viewSales = Button(window, text="View Sales", command=displaySales).grid(
        row=4, column=0, sticky="ew"
    )

    # Reorder Button
    reorder = Button(window, text="Repeat Last Order", command=repeatOrder).grid(
        row=5, column=0, sticky="ew"
    )

    # Edit Employee List Button
    addEmployee = Button(window, text="Edit Employee", command=generateEmployee).grid(
        row=6, column=0, sticky="ew"
    )

    window.mainloop()
