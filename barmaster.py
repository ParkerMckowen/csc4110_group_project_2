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


if __name__ == "__main__":

    window = create_window()
    window.mainloop()
