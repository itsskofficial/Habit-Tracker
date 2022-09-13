from distutils.util import execute
import requests
import tkinter
import sqlite3

try:
    connection = sqlite3.connect("./app.sqlite")
    print("Connection to SQLite DB successful")
except sqlite3.Error as e:
    print(f"The error '{e}' occurred")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")

create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL,
  password TEXT NOT NULL
);
"""
execute_query(connection,create_users_table)








window = tkinter.Tk()
window.title("Habit Tracker")

def Login():
    pass

def Signup():
    global usernameEntry
    global passwordEntry
    url="https://pixe.la/v1/users"
    params={
        "token": passwordEntry.get(),
        "username": usernameEntry.get(),
        "agreeTermsOfService"  : "yes",
        "notminor":"yes"
        }
    print(params)

    response=requests.post(url,json=params)
    if response.status_code==200:
        



def onClickLogin():
    global usernameEntry
    global passwordEntry
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
    global usernameEntry
    global passwordEntry
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
        command=Signup,
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
