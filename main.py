from turtle import title
import requests
import tkinter

window = tkinter.Tk()
window.title("Habit Tracker")


# Create label
lbl1 = tkinter.Label(
    window,
    text="Welcome to Habit Tracker!",
    width=50,
    height=10,
    font=("Helvetica", 30),
)
lbl1.grid(row=0, column=1)
# Create buttons
btn1 = tkinter.Button(window, text="Login",width=20,height=3)
btn2 = tkinter.Button(window, text="Signup", width=20, height=3)
btn1.grid(row=1, column=1, pady=10)
btn2.grid(row=2, column=1, pady=10)


window.mainloop()
