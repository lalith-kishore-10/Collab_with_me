import tkinter as tk
from tkinter import *
from tkinter import messagebox
def Anime():
 """
 app = Tk()
 app.geometry("500x400")
 l = Label(app, text = "Anime watched :")
 l.pack()

 lst = Label(app,text = "1. Death Note\n2.Baki\n3.Naruto\n4.Naruto Shippuden\n5.Attack On Titans\n6.When i reincarnated as a demon king\n7.King of 10 rings\n8.Dragon Ball Super\n9.HunterxHunter\n10.Bluelock\n11.Castlevania\n12.Kengen ashura\n13.Bleach\n14.Demon Slayer\n15.Jujutsu Kaisen\n16.Wind breaker\n17.Solo leveling\n\n")
 lst.pack()

 l1 = Label(app,text = "Currently watching:\n\nVinland saga")
 l1.pack()"""


App = tk.Tk()
App.geometry("400x200")
App.title("Calculator")

def Calculation():
    num1 = Entry1.get()
    num2 = Enter2.get()
    cal = opE.get()
    result = 0
    if cal == '+':
        result = num1 + num
    elif cal == '-':
        result = num1 - num2
    elif cal == '*':
        result = num1 * num2
    elif cal == '/':
        result = num1 / num2
    else:
        tkinter.messagebox.showwarning("Error","Invalid Input")

    tkinter.messagebox.showinfo("Result",result)

Heading = Label(App, text = "Enter data's to calculate :\n")
Heading.grid(column = 1,row = 1)

Enter1 = Entry(App)
Enter1.grid(column = 2, row = 3)

Enter2 = Entry(App)
Enter2.grid(column = 2, row = 4)

opL = Label(App, text = "Select any operation from the options:\n 1. +\n2. -\n3. *\n4. /")
opL.grid(column = 2,row = 5)

opE = Entry(App)
opE.grid(column = 2,row = 6)

calculate = Button(App,text = "Calculate", command = Calculation)
calculate.grid(column = 2,row = 7)

App.mainloop()