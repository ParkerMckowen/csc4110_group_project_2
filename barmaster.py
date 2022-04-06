from tkinter import *
from tkinter import ttk, messagebox
from functools import partial
from datetime import datetime
from PIL import ImageTk, Image
from collections import Counter
import pickle
import random

# Global variable for the storage of necessary bar details
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
    "sales": [],
}

# Global variable for the storage of an order
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
    "drinks": [],
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


"""
Swap the clock value function: changeClock():

Resposible for changing the "is clocked in" value
    - if 0, then change to 1 and add a new timestamp for the clock in
    - if 1, then change to 0 and add the difference between now and clockin timestamp
      to the employee's hours worked
"""


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


"""
Clocking in button function: clockIn()

This is the function that is triggered when the clock in button is pressed
    - Allows employee to enter their id, then press the clock in button
    - pops up a success window upon a successful clockin
    - calls the changeClock() function to do the actual clock changing
"""


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


"""
Clocking out button function: clockIn()

This is the function that is triggered when the clock in button is pressed
    - Allows employee to enter their id, then press the clock out button
    - pops up a success window upon a successful clockout
    - calls the changeClock() function to do the actual clock changing
"""


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


"""
Inventory Display: displayInventory()

This function is triggered when the "display inventory" button is pressed
    - displays all current values of the inventory
    - allows a user to add to the inventory
    - calls the addInventory() function with the item and amount to do the actual adding
"""


def displayInventory():
    inventoryWindow = createWindow(500, 500)
    counter = 0

    amountLabel = Label(inventoryWindow, text="Amount to add").grid(row=0, column=3)
    amountAdded = Entry(inventoryWindow)
    amountAdded.grid(row=1, column=3)

    for ingredient in BARSTORAGE["ingredients"]:
        ingredientLabel = Label(inventoryWindow, text=ingredient).grid(
            row=counter, column=0
        )

        ingredientQuantity = Label(
            inventoryWindow, text=f"{BARSTORAGE['ingredients'][ingredient]} oz"
        ).grid(row=counter, column=1)

        counter += 1

    # Add to inventory buttons
    fillInventory = Button(
        inventoryWindow,
        text="Add to Stock",
        command=(lambda: addInventory("vodka", amountAdded, inventoryWindow)),
    ).grid(row=0, column=2, sticky="ew")

    fillInventory = Button(
        inventoryWindow,
        text="Add to Stock",
        command=(lambda: addInventory("bourbon", amountAdded, inventoryWindow)),
    ).grid(row=1, column=2, sticky="ew")

    fillInventory = Button(
        inventoryWindow,
        text="Add to Stock",
        command=(lambda: addInventory("bitters", amountAdded, inventoryWindow)),
    ).grid(row=2, column=2, sticky="ew")

    fillInventory = Button(
        inventoryWindow,
        text="Add to Stock",
        command=(lambda: addInventory("tequila", amountAdded, inventoryWindow)),
    ).grid(row=3, column=2, sticky="ew")

    fillInventory = Button(
        inventoryWindow,
        text="Add to Stock",
        command=(lambda: addInventory("cointreau", amountAdded, inventoryWindow)),
    ).grid(row=4, column=2, sticky="ew")

    fillInventory = Button(
        inventoryWindow,
        text="Add to Stock",
        command=(lambda: addInventory("limejuice", amountAdded, inventoryWindow)),
    ).grid(row=5, column=2, sticky="ew")

    fillInventory = Button(
        inventoryWindow,
        text="Add to Stock",
        command=(lambda: addInventory("cranberryjuice", amountAdded, inventoryWindow)),
    ).grid(row=6, column=2, sticky="ew")

    fillInventory = Button(
        inventoryWindow,
        text="Add to Stock",
        command=(lambda: addInventory("gin", amountAdded, inventoryWindow)),
    ).grid(row=7, column=2, sticky="ew")

    fillInventory = Button(
        inventoryWindow,
        text="Add to Stock",
        command=(lambda: addInventory("campari", amountAdded, inventoryWindow)),
    ).grid(row=8, column=2, sticky="ew")

    fillInventory = Button(
        inventoryWindow,
        text="Add to Stock",
        command=(lambda: addInventory("vermouth", amountAdded, inventoryWindow)),
    ).grid(row=9, column=2, sticky="ew")

    fillInventory = Button(
        inventoryWindow,
        text="Add to Stock",
        command=(lambda: addInventory("gingerbeer", amountAdded, inventoryWindow)),
    ).grid(row=10, column=2, sticky="ew")

    fillInventory = Button(
        inventoryWindow,
        text="Add to Stock",
        command=(lambda: addInventory("rum", amountAdded, inventoryWindow)),
    ).grid(row=11, column=2, sticky="ew")

    fillInventory = Button(
        inventoryWindow,
        text="Add to Stock",
        command=(lambda: addInventory("whiskey", amountAdded, inventoryWindow)),
    ).grid(row=12, column=2, sticky="ew")

    fillInventory = Button(
        inventoryWindow,
        text="Add to Stock",
        command=(lambda: addInventory("simplesyrup", amountAdded, inventoryWindow)),
    ).grid(row=13, column=2, sticky="ew")

    fillInventory = Button(
        inventoryWindow,
        text="Add to Stock",
        command=(lambda: addInventory("lemonjuice", amountAdded, inventoryWindow)),
    ).grid(row=14, column=2, sticky="ew")


"""
Add to inventory button: addInventory()

This function is called by the "add to inventory" button in the inventory display
    - adds the called for amount to the BARSTORAGE inventory

"""


def addInventory(ingredient, amountToAdd, invWindow):
    amount = int(amountToAdd.get())
    print(amount)
    BARSTORAGE["ingredients"][ingredient] += amount

    displayInventory()


"""
Sales Display: displaySales()

This function is called when the "display sales" button is pressed
    - displays all the sales history of the bar
    - shows the employee who sold it, the id of the sale, and what was sold
"""


def displaySales():
    salesWindow = createWindow(400, 400)
    rowCounter = 0
    for sale in BARSTORAGE["sales"]:
        # saleLabel = Label(salesWindow, text=f"{sale} {BARSTORAGE['sales'][sale]}").grid(
        #     row=rowCounter, column=0
        # )

        saleLabel = Label(salesWindow, text=f"{sale}").grid(row=rowCounter, column=0)
        rowCounter += 1


"""
Closing the Program Handler: on_closing()
    - This function is responsible for handling the closing of the program, and it saves the employees added automatically prior to closing
    - This function calls the saveFile() function to accomplish the saving of the information
"""


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        saveFile()
        window.destroy()


"""
Open Pickle File Function: openFile()
    - This function is responsible for opening the pickle file which stores all of the past added employees
    - If no file exists, or the file is empty, one is created, and the storage variable is initialized as empty
    - If the file exists, and contains employees, then those employees are added to the storage variable while the program is running
"""


def openFile(storage):
    try:
        with open("barData.pickle", "rb") as barData:
            data = pickle.load(barData)
            for field in data:
                storage[field] = data[field]

    except EOFError:
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
            "sales": {},
        }

    except FileNotFoundError:
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
            "sales": {},
        }
        with open("barData.pickle", "wb") as employees:
            pickle.dump(BARSTORAGE, employees)


"""
Save to Pickle File Function: saveFile()
    - This function is responsible for saving what is in the storage variable, into the pickle file
    - This function overwrites what is in the pickle file, which is why the open funtion loads the current information in the file
       into the storage variable prior to the addition of new employees, it actually happens on opening
"""


def saveFile():
    with open("barData.pickle", "wb") as employees:
        pickle.dump(BARSTORAGE, employees)


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


"""
Saving New Employee Function: commitEmployee()

This function takes in the new employee details
    - checks the details to make sure they are valid (special char, blank, etc)
    - adds the new employee to the BARSTORAGE employees field if valid
"""


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


"""
Employee Deletion: deleteEmployee()

This function is triggered when the delete button next to the employee on the edit page is pressed
    - deletes the employee from the BARSTORAGE
"""


def deleteEmployee(empid, empwindow):
    BARSTORAGE["employees"].pop(empid)
    empwindow.destroy()
    generateEmployee()


"""
Employee Edit Portal Function: generateEmployee()

This function is triggered when the "edit employees" button is pressed
    - creates the window/portal for employee editing

"""


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


"""
Repeat Last Order Function: repeatOrder()

This function takes the last order placed, and adds it to the sales history again
    - adds new sale id for the sale
    - requires a valid employee id to repeat just like the initial sale
"""


def repeatOrder(idCheck):
    add_flag = 1

    lastval = len(BARSTORAGE["sales"]) - 1
    saleid = generateEmpId()
    empid = BARSTORAGE["sales"][lastval]["employee"]
    drinks = BARSTORAGE["sales"][lastval]["drinks"]

    if idCheck.get() == "":
        Label(window, text="Empty Field").grid(row=7, column=4)
        add_flag = 0
    elif idCheck.get() not in BARSTORAGE["employees"].keys():
        add_flag = 0
        Label(window, text="Not an employee!").grid(row=7, column=4)
    else:
        if catchBadChar(idCheck.get()):
            add_flag = 1
        else:
            Label(window, text="Forbidden Character Detected").grid(row=7, column=4)
            add_flag = 0

    if add_flag:

        BARSTORAGE["sales"].append(
            {"saleID": saleid, "employee": empid, "drinks": drinks}
        )


"""
Clear ORDER on Submission: clearOrder()

This function is responsible for clearing out the global ORDER variable when the order is placed
    - gets it ready for the next order
"""


def clearOrder(window):
    for ingredient in ORDER["ingredients"]:
        ORDER["ingredients"][ingredient] = 0

    ORDER["server"] = ""
    ORDER["drinks"] = []

    updateOrderDisplay(window)


"""
Order Submission: placeOrder()

This function is what actually adds the order to the BARSTORAGE
    - requires a valid employee id to submit
"""


def placeOrder(window, empid):
    add_flag = 1

    for ingredient in ORDER["ingredients"]:
        pour = ORDER["ingredients"][ingredient]
        BARSTORAGE["ingredients"][ingredient] -= pour

    saleid = generateEmpId()

    if empid.get() == "":
        Label(window, text="Empty Field").grid(row=7, column=4)
        add_flag = 0
    elif empid.get() not in BARSTORAGE["employees"].keys():
        add_flag = 0
        Label(window, text="Not an employee!").grid(row=7, column=4)
    else:
        if catchBadChar(empid.get()):
            add_flag = 1
        else:
            Label(window, text="Forbidden Character Detected").grid(row=7, column=4)
            add_flag = 0

    if add_flag:
        BARSTORAGE["sales"].append(
            {"saleID": saleid, "employee": empid.get(), "drinks": ORDER["drinks"]}
        )

        LASTORDER = ORDER
        print(BARSTORAGE["sales"])
        clearOrder(window)


"""
Current Order Display: updateOrderDisplay()

This function prints out the contents of the current order along with their values to the main page
"""


def updateOrderDisplay(window):
    order = ORDER
    rowCounter = 5
    drinkCounts = Counter(order["drinks"])
    for drink in drinkCounts:
        drinkLabel = Label(window, text=f"{drink}").grid(row=rowCounter, column=1)
        drinkCount = Label(window, text=f"{drinkCounts[drink]}").grid(
            row=rowCounter, column=2
        )
        rowCounter += 1


"""
Add a drink to order: addToOrder()

This function adds the drink, and its ingredients to the current ORDER
"""


def addToOrder(drinkName, window):
    if drinkName == "OldFashioned":
        ORDER["ingredients"]["bourbon"] += 2
        ORDER["ingredients"]["bitters"] += 1
        ORDER["drinks"].append(drinkName)
        updateOrderDisplay(window)

    elif drinkName == "Margarita":
        ORDER["ingredients"]["tequila"] += 2
        ORDER["ingredients"]["cointreau"] += 1
        ORDER["ingredients"]["limejuice"] += 1
        ORDER["drinks"].append(drinkName)
        updateOrderDisplay(window)

    elif drinkName == "Cosmopolitan":
        ORDER["ingredients"]["vodka"] += 2
        ORDER["ingredients"]["cointreau"] += 1
        ORDER["ingredients"]["limejuice"] += 1
        ORDER["ingredients"]["cranberryjuice"] += 1
        ORDER["drinks"].append(drinkName)
        updateOrderDisplay(window)

    elif drinkName == "Negroni":
        ORDER["ingredients"]["gin"] += 1
        ORDER["ingredients"]["campari"] += 1
        ORDER["ingredients"]["vermouth"] += 1
        ORDER["drinks"].append(drinkName)
        updateOrderDisplay(window)

    elif drinkName == "MoscowMule":
        ORDER["ingredients"]["vodka"] += 2
        ORDER["ingredients"]["gingerbeer"] += 5
        ORDER["ingredients"]["limejuice"] += 1
        ORDER["drinks"].append(drinkName)
        updateOrderDisplay(window)

    elif drinkName == "Martini":
        ORDER["ingredients"]["gin"] += 3
        ORDER["ingredients"]["vermouth"] += 1
        ORDER["drinks"].append(drinkName)
        updateOrderDisplay(window)

    elif drinkName == "Mojito":
        ORDER["ingredients"]["rum"] += 2
        ORDER["ingredients"]["limejuice"] += 1
        ORDER["ingredients"]["simplesyrup"] += 2
        ORDER["drinks"].append(drinkName)
        updateOrderDisplay(window)

    elif drinkName == "WhiskeySour":
        ORDER["ingredients"]["whiskey"] += 2
        ORDER["ingredients"]["lemonjuice"] += 1
        ORDER["drinks"].append(drinkName)
        updateOrderDisplay(window)

    elif drinkName == "Manhattan":
        ORDER["ingredients"]["whiskey"] += 2
        ORDER["ingredients"]["vermouth"] += 1
        ORDER["ingredients"]["bitters"] += 1
        ORDER["drinks"].append(drinkName)
        updateOrderDisplay(window)

    elif drinkName == "Daiquiri":
        ORDER["ingredients"]["rum"] += 2
        ORDER["ingredients"]["simplesyrup"] += 2
        ORDER["ingredients"]["limejuice"] += 2
        ORDER["drinks"].append(drinkName)
        updateOrderDisplay(window)

    print(ORDER)


if __name__ == "__main__":

    window = createWindow(1300, 1100)
    openFile(BARSTORAGE)

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
        command=(lambda: addToOrder("Cosmopolitan", window)),
    ).grid(row=0, column=0, sticky="ew")

    daqButton = Button(
        window,
        text="Daquiri",
        image=daquiIm,
        compound=TOP,
        command=(lambda: addToOrder("Daiquiri", window)),
    ).grid(row=0, column=1, sticky="ew")

    manButton = Button(
        window,
        text="Manhattan",
        image=manhatIm,
        compound=TOP,
        command=(lambda: addToOrder("Manhattan", window)),
    ).grid(row=0, column=2, sticky="ew")

    margButton = Button(
        window,
        text="Margarita",
        image=margaIm,
        compound=TOP,
        command=(lambda: addToOrder("Margarita", window)),
    ).grid(row=0, column=3, sticky="ew")

    # Drink buttons row 2
    martButton = Button(
        window,
        image=martiIm,
        compound=TOP,
        text="Martini",
        command=(lambda: addToOrder("Martini", window)),
    ).grid(row=1, column=0, sticky="ew")

    mojButton = Button(
        window,
        text="Mojito",
        image=daquiIm,
        compound=TOP,
        command=(lambda: addToOrder("Mojito", window)),
    ).grid(row=1, column=1, sticky="ew")

    negroniButton = Button(
        window,
        text="Negroni",
        image=negroniIm,
        compound=TOP,
        command=(lambda: addToOrder("Negroni", window)),
    ).grid(row=1, column=2, sticky="ew")

    moscButton = Button(
        window,
        text="Moscow Mule",
        image=moscoIm,
        compound=TOP,
        command=(lambda: addToOrder("MoscowMule", window)),
    ).grid(row=1, column=3, sticky="ew")

    # Drink buttons row 3
    oldfButton = Button(
        window,
        text="Old Fashioned",
        image=oldfIm,
        compound=TOP,
        command=(lambda: addToOrder("OldFashioned", window)),
    ).grid(row=2, column=0, sticky="ew")

    wsrButton = Button(
        window,
        text="Whiskey Sour",
        image=whiskIm,
        compound=TOP,
        command=(lambda: addToOrder("WhiskeySour", window)),
    ).grid(row=2, column=1, sticky="ew")

    # Clock in Button
    clockIn = Button(window, text="Clock In", command=clockIn).grid(
        row=5, column=0, sticky="ew"
    )

    # Clock out Button
    clockOut = Button(window, text="Clock Out", command=clockOut).grid(
        row=6, column=0, sticky="ew"
    )

    # Display Inventory Button
    viewInventory = Button(
        window, text="View Inventory", command=displayInventory
    ).grid(row=7, column=0, sticky="ew")

    # View Sales Button
    viewSales = Button(window, text="View Sales", command=displaySales).grid(
        row=8, column=0, sticky="ew"
    )

    # Edit Employee List Button
    addEmployee = Button(window, text="Edit Employee", command=generateEmployee).grid(
        row=9, column=0, sticky="ew"
    )

    header1 = Label(window, text="Drink").grid(row=4, column=1)
    header2 = Label(window, text="Qty.").grid(row=4, column=2)
    header3 = Label(window, text="Employee ID: ").grid(row=6, column=3)

    empIdEntry = Entry(window)
    empIdEntry.grid(row=7, column=3)

    submitOrderButton = Button(
        window, text="Submit Order", command=(lambda: placeOrder(window, empIdEntry))
    ).grid(row=4, column=3)

    reorderButton = Button(
        window, text="Repeat Order", command=(lambda: repeatOrder(empIdEntry))
    ).grid(row=5, column=3)

    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()
