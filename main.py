from turtle import onclick, title
from xml.dom.minidom import Entity
import requests
import tkinter
from functions import *

window = tkinter.Tk()
window.title("Habit Tracker")

def onClickLogin():
    btn1.destroy()
    btn2.destroy()
    lbl1.config(text="Login")
    usernameLabel=tkinter.Label(window,text="Username")
    usernameEntry=tkinter.Entry(window)
    usernameLabel.grid(row=1,column=1)
    usernameEntry.grid(row=1,column=1)

# Create label
lbl1 = tkinter.Label(
    window,
    text="Welcome to Habit Tracker",
    width=50,
    height=10,
    font=("Helvetica", 30),
)
lbl1.grid(row=0, column=1)
# Create buttons
btn1 = tkinter.Button(window, text="Login",width=20,height=3,font=("Montserrat",15),command=onClickLogin)
btn2 = tkinter.Button(window, text="Signup", width=20, height=3,font=("Montserrat",15))
btn1.grid(row=1, column=1, pady=10)
btn2.grid(row=2, column=1, pady=10)


window.mainloop()
