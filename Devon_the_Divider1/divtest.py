import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo

    #create the input box
first = Tk()
first.geometry('400x300')
first.resizable(False,False)
first.title('Division nunmbers')


def division():
    #text inside the input box
    tk.Label(first, text="Please enter numbers for division:").grid(row=0)
    tk.Label(first, text="Numerator:").grid(row=1)
    tk.Label(first, text="Denominator").grid(row=2)
    var1 = tk.Entry(first)#entry is tkinters input keyword
    var2 = tk.Entry(first)
    var1.grid(row=1, column=1)
    var2.grid(row=2, column=1)

    def clickokayButton():
        num1 = int(var1.get())
        num2 = int(var2.get())
        try:
            division = num1/num2
            showinfo(
                    title='Division by Devon',
                    message=f'You chose {num1} as the numerator.\nYou chose {num2} as the denominator.\n The quotient is {division}.'
                    )
            first.destroy()
        except ZeroDivisionError:
            showinfo(
                    title='Really?',
                    message=f'You chose {num1} as the numerator.\nYou chose {num2} as the denominator.\nIn case you did not know it by now:\nYou. Cannot. Divide. With. Zero.'
                    )
            first.destroy()
    #create a button to accept the given input
    mybutton = Button(first, text="Give me what you got Devon!", width = 40, command=clickokayButton)
    mybutton.place(x=50, y=150)
    
    



division()

