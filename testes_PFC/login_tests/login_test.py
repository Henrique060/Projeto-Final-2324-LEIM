import pyrebase


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

def login():
    print("Log in...")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    try:
        login = auth.sign_in_with_email_and_password(email, password)
        print("Successfully signed in")
        

    except:
        print("Invalid email or password")

def signup():
    print("Sign up...")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    try:
        user = auth.create_user_with_email_and_password(email, password)
    except:
        print("Failed to create user")
    return

ans = input("Are you a new user? (y/n): ")

if ans == 'y':
    signup()
elif ans == 'n':
    login()
