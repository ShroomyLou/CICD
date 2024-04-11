import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from playsound import playsound
import time
import random
from tabulate import tabulate

def clickpowersButton():
    #create the input box
        first = Tk()
        first.geometry('400x300')
        first.resizable(False,False)
        first.title('Power')


        def powers():
            #text inside the input box
            tk.Label(first, text="Please enter a number for exponential powers:").grid(row=0)
            tk.Label(first, text="The number:").grid(row=1)
            var1 = tk.Entry(first)#entry is tkinters input keyword
            var1.grid(row=1, column=1)

            my_data = []
            my_file = open("Devon_results.txt", "w")
            def clickokayButton():
                numb = int(var1.get())
                power = 0
                expo = 0
                
                while expo < 11:
                    expo = expo + 1
                    power = pow(numb, expo)
                    temp_list = [numb, expo, power]
                    my_data.append(temp_list)

                    if expo == 10:
                        head = ["Number", "Exponent", "Result"]
                        table = tabulate(my_data, headers=head, tablefmt="grid")
                        my_file.write(table)
                        my_file.close()
                        showinfo(
                                title='Powers by Devon',
                                message=f'{table}'
                                )
                        first.destroy()
            #create a button to accept the given input
            mybutton = Button(first, text="Give me what you got Devon!", width = 40, command=clickokayButton)
            mybutton.place(x=50, y=150)
    
    



        powers()
    
    
clickpowersButton()
