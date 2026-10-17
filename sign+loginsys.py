import sqlite3
from passlib.hash import argon2
global istrue
isTrue = True
con = sqlite3.connect("users.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)")   
def choice():
    while True:
        choice1 = input("Would you like to log in or sign up?type L for logging in, S for signing in " 
        "q for quitting:")
        if choice1 == 'l' or choice1 == 'L':
            login()
        elif choice1 == 's' or choice1 == 'S':
            register()
        elif choice1 == 'q' or choice1 == 'Q':
            break

    

def register():
    getuser = input("Enter your username:")
    getpass = input("Enter your password:")
    hashed_stored = argon2.hash(getpass)
    uandp = []
    uandp.append(getuser)#alkcz
    uandp.append(hashed_stored)
    try:
        cur.execute("INSERT INTO users(username,password) VALUES(?,?)",uandp)
    except sqlite3.IntegrityError:
        print("That username is already chosen please choose another username")
    finally:
        pass
        con.commit()
    con.commit()

    return hashed_stored
def login():
    data =  cur.execute("SELECT username, password FROM users")
    user = input("Enter your u8sername:")
    password = input("Enter your password:")

    for row in data:
        if user == row[0]:
            stored_hash = row[1]
            if argon2.verify(password,stored_hash) == True:
                print("You're  in")
                break
            else:
                print('password or username is  wrong')
        else:
            print('password or username are wrong')
            con.commit()
        con.commit()
    con.commit()


choice()
con.commit()
con.close()
