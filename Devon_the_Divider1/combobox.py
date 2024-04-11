import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

##root = tk.Tk()
##
##root.geometry('300x200')
##root.resizable(False,False)
##root.title('Combobox Keno')
##
##label = ttk.Label(text="Please select the amount of numbers for Keno:")
##label.pack(fill=tk.X, padx=5, pady=5)
##
##selected_amount = tk.StringVar()
##amount_cb = ttk.Combobox(root, textvariable=selected_amount)
##
##amount_cb['values'] = [2,3,4,5,6,7,8,9,10]
##amount_cb['state'] = 'readonly'
##
##amount_cb.pack(fill=tk.X, padx=5, pady=5)
##
##def amount_changed(event):
##    """ handle the amount changed event """
##    showinfo(
##        title='Result',
##        message=f'You selected {selected_amount.get()}!'
##    )
##
##amount_cb.bind('<<ComboboxSelected>>', amount_changed)
##
##root.mainloop()


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
    showinfo(
        title='Amount of Keno numbers',
        message=f'You selected {selected_amount.get()}!'
    )
    print("asdad",selected_amount.get())
amount_cb.bind('<<ComboboxSelected>>', amount_changed)

root.mainloop()
