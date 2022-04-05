from tkinter import *
from tkinter import ttk, messagebox
from functools import partial
from datetime import datetime
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


def createWindow():

    window = Tk()
    window.title("BarMaster POS")
    window.geometry("1200x480")

    return window


def changeClock(empid):
    login = empid.get()
    if BARSTORAGE["employees"][login]["onClock"] == 0:
        BARSTORAGE["employees"][login]["onClock"] = 1
        BARSTORAGE["employees"][login]["clockin"] = datetime.now()
    else:
        BARSTORAGE["employees"][login]["onClock"] = 0
        clockinTime = BARSTORAGE["employees"][login]["clockin"]
        difference = datetime.now() - clockinTime
        seconds = difference.total_seconds()
        differenceInHours = seconds / 3600
        BARSTORAGE["employees"][login]["hours"] += differenceInHours


def clockIn():
    clockinWindow = createWindow()
    loginIDLabel = Label(clockinWindow, text="Employee ID: ").grid(row=0, column=0)
    loginID = Entry(clockinWindow)
    loginID.grid(row=0, column=1)

    clockinButton = Button(
        clockinWindow,
        text="Clock In",
        command=(lambda: changeClock(loginID)),
    )
    clockinButton.grid(row=1, column=0)


def clockOut():
    clockoutWindow = createWindow()
    loginIDLabel = Label(clockoutWindow, text="Employee ID: ").grid(row=0, column=0)
    loginID = Entry(clockoutWindow)
    loginID.grid(row=0, column=1)

    clockoutButton = Button(
        clockoutWindow,
        text="Clock Out",
        command=(lambda: changeClock(loginID)),
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
    newEmployeeFirstName = efname.get()
    newEmployeeLastName = elname.get()
    newEmployeeEmail = eemail.get()
    newEmployeePhone = ephone.get()
    newEmployeeID = generateEmpId()

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

    print(BARSTORAGE["employees"])
    empWindow.destroy()
    generateEmployee()


def deleteEmployee(empid, empwindow):
    BARSTORAGE["employees"].pop(empid)
    empwindow.destroy()
    generateEmployee()


def generateEmployee():
    empWindow = createWindow()

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

        fname = Label(empWindow, text=employee["fname"]).grid(
            row=rowTracker, column=5, sticky="ew"
        )

        hours = Label(empWindow, text=employee["hours"]).grid(
            row=rowTracker, column=6, sticky="ew"
        )

        rowTracker += 1

    empWindow.mainloop()


if __name__ == "__main__":

    window = createWindow()

    clockIn = Button(window, text="Clock In", command=clockIn).grid(
        row=0, column=0, sticky="ew"
    )

    clockOut = Button(window, text="Clock Out", command=clockOut).grid(
        row=1, column=0, sticky="ew"
    )

    viewInventory = Button(
        window, text="View Inventory", command=displayInventory
    ).grid(row=2, column=0, sticky="ew")

    fillInventory = Button(window, text="Add to Inventory", command=addInventory).grid(
        row=3, column=0, sticky="ew"
    )

    viewSales = Button(window, text="View Sales", command=displaySales).grid(
        row=4, column=0, sticky="ew"
    )

    reorder = Button(window, text="Repeat Last Order", command=repeatOrder).grid(
        row=5, column=0, sticky="ew"
    )

    addEmployee = Button(window, text="Edit Employee", command=generateEmployee).grid(
        row=6, column=0, sticky="ew"
    )

    window.mainloop()
