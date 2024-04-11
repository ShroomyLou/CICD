import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from playsound import playsound
import time
import random
from tabulate import tabulate

class App(Frame):
    def __init__(self, master=None):
        #create the main window
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        self.label = Label(text="", fg="Red", font=("Times New Roman", 18))
        self.label.place(x=480,y=20)
        message = "I am Devon the Divider"
        self.label.configure(text=message)

        #window background
        load = Image.open("Devon1.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)
        
        #create a menu
        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu)
        fileMenu.add_command(label="Item")
        fileMenu.add_command(label="Exit", command=self.exitProgram)
        menu.add_cascade(label="File", menu=fileMenu)

        editMenu = Menu(menu)
        editMenu.add_command(label="Undo")
        editMenu.add_command(label="Redo")
        menu.add_cascade(label="Edit", menu=editMenu)

        #make an exit button
        exitButton = Button(self, text="Exit", command=self.clickExitButton)
        exitButton.place(x=20, y=300)

        #make additional buttons
        divisionButton = Button(self, text="Division", command=self.clickdivisionButton)
        divisionButton.place(x=20, y=40)

        powersButton = Button(self, text="Powers", command=self.clickpowersButton)
        powersButton.place(x=20, y=70)

        squarerootButton = Button(self, text="Squareroots", command=self.clicksquarerootButton)
        squarerootButton.place(x=20, y=100)

        gamblingButton = Button(self, text="Gambling", command=self.clickgamblingButton)
        gamblingButton.place(x=20, y=130)

    #display a clock
        self.update_clock()
        
    def update_clock(self):
        self.clock = Label(text="", fg="Red", font=("Helvetica", 18))
        now = time.strftime("%H:%M:%S")
        self.clock.place(x=375,y=300)
        self.clock.configure(text=now)
        self.after(1000, self.update_clock)

    #This is for displaying the clock in an angle. Turns out it wasn't possible.
        #textID = w1.create_text(5, 5, anchor="nw", angle=90)

    #Functions for pressing buttons
    def clickdivisionButton(self):
            #create the input box
        first = Tk()
        first.geometry('400x300')
        first.resizable(False,False)
        first.title('Division numbers')


        def division():
            #text inside the input box
            tk.Label(first, text="Please enter numbers for division:").grid(row=0)
            tk.Label(first, text="Numerator:").grid(row=1)
            tk.Label(first, text="Denominator").grid(row=2)
            var1 = tk.Entry(first)#entry is tkinters input keyword
            var2 = tk.Entry(first)
            var1.grid(row=1, column=1)
            var2.grid(row=2, column=1)

            
            #Initiate division
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
    
    def clickpowersButton(self):
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

            #Initiate powers(calculations)
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

    def clicksquarerootButton(self):
        my_file = open("Devon_squareroots.txt", "w")

        #Initiate squareroots
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


    #Opens choice for Keno or Lotto
    def clickgamblingButton(self):
        self.label = Label(text="", fg="Blue", font=("Times New Roman", 16))
        self.label.place(x=20, y=130)
        playsound('Devontyping3.mp3')
        self.label.configure(text="A small time gambler eh?\n Pick your poison: Lottery or Keno")

        #buttons for lottery or keno
        lottoButton = Button(self, text="LOTTO", command=self.clicklottoButton)
        lottoButton.place(x=20, y=200)

        kenoButton = Button(self, text="KENO", command=self.clickkenoButton)
        kenoButton.place(x=80, y=200)


    #Initiate Lotto numbers
    def clicklottoButton(self):
        lotterynumbers = []

        for i in range(1,41):
            lotterynumbers.append(i)

        your_lottery = []
        extra_number = []

        for j in range(7):
            lotterynumb = random.choice(lotterynumbers)
            your_lottery.append(lotterynumb)
            lotterynumbers.remove(lotterynumb)

        lotto = '\n'.join(map(str, your_lottery))
        extra = extra_number.append(random.choice(lotterynumbers))
        extralotto = '\n'.join(map(str, extra_number))
        showinfo(
                title='Your LOTTO numbers',
                message=(f'Your LOTTO numbers for today are:\n {lotto}\n and the extra number is:\n {extralotto}!\n Let us hope I am right!')
                )


    #Initiate Keno numbers
    def clickkenoButton(self):

        #Choices for the amount of numbers for Keno
        root = tk.Tk()
        root.geometry('300x200')
        root.resizable(False,False)
        root.title('Combobox Keno')

        label = ttk.Label(text="Please select the amount of numbers for Keno:")
        label.pack(fill=tk.X, padx=5, pady=5)

        selected_amount = tk.StringVar()
        amount_cb = ttk.Combobox(root, textvariable=selected_amount)

        amount_cb['values'] = [2,3,4,5,6,7,8,9,10]
        amount_cb['state'] = 'readonly'

        amount_cb.pack(fill=tk.X, padx=5, pady=5)

        #This handles the change in amount of Keno numbers.
        def amount_changed(event):
            
            keno_amount = int(amount_cb.get())
            kenonumbers = []
            your_keno = []
            
            for x in range(1,71):
                kenonumbers.append(x)

            for y in range(keno_amount):
                kenonumb = random.choice(kenonumbers)
                your_keno.append(kenonumb)
                kenonumbers.remove(kenonumb)
            keno = '\n'.join(map(str, your_keno))
            
            showinfo(
                title='Amount of Keno numbers',
                message=f'You selected {amount_cb.get()}!\n Your KENO numbers for today are:\n {keno}\n May lady luck be on your side!'
                )
            
            
        amount_cb.bind('<<ComboboxSelected>>', amount_changed)

        root.mainloop()

    #Terminate the program
    def exitProgram(self):
        exit()

    def clickExitButton(self):
        exit()

#initialize tkinter
root = tk.Tk()
app = App(root)

#set window title
root.wm_title("Tkinter window")

#set the size for window
root.geometry("720x480")

#for the clock
root.after(1000, app.update_clock)

#show window
root.mainloop()




    
