import requests
import tkinter
from functions import *

window = tkinter.Tk()
window.title("Habit Tracker")


def Login():
    pass

def Signup(usernameEntry,usernameLabel):
    url="https://pixe.la/v1/users"
    params={
        "token": usernameEntry.get(),
        "username": usernameLabel["text"],
        "agreeTermsOfService"  : "yes",
        "notminor":"yes"
        }
    print(params)

    response=requests.post(url,params=params)
    print(response)



def onClickLogin():
    btn1.destroy()
    btn2.destroy()
    lbl1.config(text="Login")
    lbl1.grid(columnspan=2)
    usernameLabel = tkinter.Label(window, text="Username :", font=("Montserrat", 15))
    usernameEntry = tkinter.Entry(window, font=("Montserrat", 15))
    usernameLabel.grid(row=1, column=1, pady=20)
    usernameEntry.grid(row=1, column=2, pady=20)
    passwordLabel = tkinter.Label(window, text="Password :", font=("Montserrat", 15))
    passwordEntry = tkinter.Entry(window, font=("Montserrat", 15))
    passwordLabel.grid(row=2, column=1, pady=20)
    passwordEntry.grid(row=2, column=2, pady=20)
    loginButton = tkinter.Button(
        window,
        text="Login",
        width=20,
        height=3,
        font=("Montserrat", 15),
        command=Login,
    )
    loginButton.grid(row=3, column=2, columnspan=2, pady=20)

def onClickSignup():
    btn1.destroy()
    btn2.destroy()
    lbl1.config(text="Signup")
    lbl1.grid(columnspan=2)
    usernameLabel = tkinter.Label(window, text="Username :", font=("Montserrat", 15))
    usernameEntry = tkinter.Entry(window, font=("Montserrat", 15))
    usernameLabel.grid(row=1, column=1, pady=20)
    usernameEntry.grid(row=1, column=2, pady=20)
    passwordLabel = tkinter.Label(window, text="Password :", font=("Montserrat", 15))
    passwordEntry = tkinter.Entry(window, font=("Montserrat", 15))
    passwordLabel.grid(row=2, column=1, pady=20)
    passwordEntry.grid(row=2, column=2, pady=20)
    signupButton = tkinter.Button(
        window,
        text="Signup",
        width=20,
        height=3,
        font=("Montserrat", 15),
        command=Signup(usernameEntry,usernameLabel),
    )
    signupButton.grid(row=3, column=1, columnspan=2, pady=20)


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

btn1 = tkinter.Button(
    window,
    text="Login",
    width=20,
    height=3,
    font=("Montserrat", 15),
    command=onClickLogin,
)
btn2 = tkinter.Button(
    window, text="Signup", width=20, height=3, font=("Montserrat", 15),command=onClickSignup,
)
btn1.grid(row=1, column=1, pady=20)
btn2.grid(row=2, column=1, pady=20)


window.mainloop()
