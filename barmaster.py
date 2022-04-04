from tkinter import *
from tkinter import ttk, messagebox


"""
Create Window Function: create_window()
    This function is responsible for the generation of the tkinter "Window" object, which is returned by this function
"""


def create_window():

    window = Tk()
    window.title("BarMaster POS")
    window.geometry("400x250")

    return window


def clockIn():
    return 1


def clockOut():
    return 1


def displayInventory():
    return 1


def addInventory():
    return 1


def displaySales():
    return 1


def repeatOrder():
    return 1


if __name__ == "__main__":

    window = create_window()

    clockIn = Button(window, text="Clock In", command=clockIn).grid(row=0, column=0)

    clockOut = Button(window, text="Clock Out", command=clockOut).grid(row=1, column=0)

    viewInventory = Button(
        window, text="View Inventory", command=displayInventory
    ).grid(row=2, column=0)

    fillInventory = Button(window, text="Add to Inventory", command=addInventory).grid(
        row=3, column=0
    )

    viewSales = Button(window, text="View Sales", command=displaySales).grid(
        row=4, column=0
    )

    reorder = Button(window, text="Repeat Last Order", command=repeatOrder).grid(
        row=5, column=0
    )

    window.mainloop()
