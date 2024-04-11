import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from playsound import playsound
import time
import random
from tabulate import tabulate


def clicksquarerootButton():

    my_file = open("Devon_squareroots.txt", "w")

    def devonsquares():

        base = 0

        my_squares = []

        while base < 26:
            base = base + 1
            square = base ** 0.5
            temp_squares = [base, square]
            my_squares.append(temp_squares)

            if base == 25:
                head = ["Number", "Squareroot"]
                table = tabulate(my_squares, headers=head, tablefmt="grid")
                my_file.write(table)
                showinfo(
                        title = "Devon's squares",
                        message=f'{table}'
                        )
                #first.destroy()
                my_file.close()

    devonsquares()

clicksquarerootButton()
