## Criar uma GUI em TKINTER para LOGIN

import pyrebase
import tkinter
import customtkinter

from OOP_prototype.bulidtest.guiv1 import GUI

fireBaseConfig = {
    "apiKey": "AIzaSyDOhQqt7TvCNTUq8HhJdFP4JoMkXM43SVg",
    "authDomain": "bulidtest.firebaseapp.com",
    "projectId": "bulidtest",
    "databaseURL": "https://console.firebase.google.com/project/bulidtest/database/bulidtest-default-rtdb/data/~2F",
    "storageBucket": "bulidtest.appspot.com",
    "messagingSenderId": "516788987739",
    "appId": "1:516788987739:web:23d1791d0b3380b2a9dc7e",
    "measurementId": "G-GE9F8EHH2W"
}

firebase = pyrebase.initialize_app(fireBaseConfig)
auth = firebase.auth()

def logon_task():
    email = username_entry.get()
    password = password_entry.get()
    try:
        login = auth.sign_in_with_email_and_password(email, password)
        result.configure(text="Successfully signed in")
       
        try:
        # Open new test window
            app.destroy()
            new_window = GUI()
            print("Opened new window")
        except:
            print("FUCK YOU")
    except:
        result.configure(text="Invalid email or password")
    return

def signup_task():
    email = username_entry.get()
    password = password_entry.get()
    try:
        user = auth.create_user_with_email_and_password(email, password)
        result.configure(text="Successfully signed up")
    except:
        result.configure(text="Failed to create user")
    return

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("400x240")

username = customtkinter.CTkLabel(master=app,
                                  text="Username:",
                                  width=80,
                                  height=25,
                                  text_color="black",
                                  fg_color="white",
                                  corner_radius=8)
username.place(relx=0.3, rely=0.3, anchor=tkinter.CENTER)

password = customtkinter.CTkLabel(master=app,
                                    text="Password:",
                                    width=80,
                                    height=25,
                                    text_color="black",
                                    fg_color="white",
                                    corner_radius=8)
password.place(relx=0.3, rely=0.5, anchor=tkinter.CENTER)

## Entrada de utilizador e placement
username_entry = customtkinter.CTkEntry(master=app,
                                        placeholder_text="Username",
                                        width=180,
                                        height=25,
                                        border_width=2,
                                        corner_radius=10)
username_entry.place(relx=0.65, rely=0.3, anchor=tkinter.CENTER)


## Entrada de password e placement
password_entry = customtkinter.CTkEntry(master=app,
                                        placeholder_text="Password",
                                        width=180,
                                        height=25,
                                        border_width=2,
                                        corner_radius=10)
password_entry.place(relx=0.65, rely=0.5, anchor=tkinter.CENTER)

## Login action button
login_button = customtkinter.CTkButton(master=app,
                                        text="Login",
                                        width=80,
                                        height=32,
                                        corner_radius=8,
                                        fg_color="white",
                                        text_color="black",
                                        command=logon_task, ## função de login
                                        hover_color="light blue")
login_button.place(relx=0.71, rely=0.7, anchor=tkinter.CENTER)

## Signup button action

signup_button = customtkinter.CTkButton(master=app,
                                        width=80,
                                        height=32,
                                        text="Signup",
                                        command=signup_task, ## função de signup
                                        corner_radius=8)
signup_button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

## Result output
result = customtkinter.CTkLabel(master=app,
                                text = "",
                                width=120,
                                height=25,
                                text_color="black",
                                fg_color="white",
                                corner_radius=8)
result.place(relx=0.62, rely=0.85, anchor=tkinter.CENTER)


app.mainloop()
