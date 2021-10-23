from tkinter import *
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
database = client.login
user = database.user

def Identification(): 
 screen= Tk()
 screen.title("Login")
 screen.resizable(False, False)
 screen.overrideredirect(False)
 screen.geometry("{0}x{1}+0+0".format(screen.winfo_screenwidth(), screen.winfo_screenheight()))
 global username_entry
 global password_entry

 Label(screen, text="LOGIN", font=("Arial black",25)).place(x=640,y=200)

 Label(screen,text="User name : ",font=("Arial black",12)).place(x=545,y=260)
 username_entry=Entry(screen, textvariable="",width=50)
 username_entry.place(x=545,y=290)

 Label(screen,text="Password : ",font=("Arial black",12)).place(x=545,y=320)
 password_entry=Entry(screen, textvariable="",width=50,show="*")
 password_entry.place(x=545,y=350)

 Button(screen, text="  Entrer  ", bg="#000000", fg="#ffffff",font=("Arial black",10),command=LoginFind).place(x=660,y=400)
 screen.mainloop()

def LoginFind():
    try:
        test = False
        nom = str(username_entry.get())
        word = str(password_entry.get())
        for val in user.find({},{"username": 1, "password": 1}):
            if nom == str(val["username"]) and word == str(val["password"]):
                 test = True
        if test == True :
            Add()
            username_entry.delete(0,END)
            password_entry.delete(0,END)
    except:
        pass

def Add():   
 screen1= Tk()
 screen1.title("Login")
 screen1.resizable(False, False)
 screen1.overrideredirect(False)
 screen1.geometry("{0}x{1}+0+0".format(screen1.winfo_screenwidth(), screen1.winfo_screenheight()))
 global username_add_entry
 global password_add_entry

 Label(screen1, text="Add User", font=("Arial black",25)).place(x=610,y=200)
 
 Label(screen1,text="User name : ",font=("Arial black",12)).place(x=545,y=260)
 username_add_entry=Entry(screen1, textvariable="",width=50)
 username_add_entry.place(x=545,y=290)
 
 Label(screen1,text="Password : ",font=("Arial black",12)).place(x=545,y=320)
 password_add_entry=Entry(screen1, textvariable="",width=50,show="*")
 password_add_entry.place(x=545,y=350)
 
 Button(screen1, text="Add", bg="#000000", fg="#ffffff",width=10,font=("Arial black",10),command=InsertUser).place(x=545,y=400)
 Button(screen1, text="Consult", bg="#000000", fg="#ffffff",width=10,font=("Arial black",10),command=ConsultBox).place(x=647,y=400)
 Button(screen1, text="Return", bg="#000000", fg="#ffffff",width=10,font=("Arial black",10),command=screen1.destroy).place(x=750,y=400)
 
 screen1.mainloop()

def InsertUser():
    try:
        nom = str(username_add_entry.get())
        word = str(password_add_entry.get())
        test = False
        if nom != "" :
            if word != "":
                for val in user.find({},{"username": 1, "password": 1}):
                    if nom == str(val["username"]) and word == str(val["password"]):
                        test = True
                if test == True :
                    pass
                else:    
                    doc = {
                        "username": f"{nom}",
                        "password": f"{word}",
                    }
                    user.insert_one(doc)
                    username_add_entry.delete(0,END)
                    password_add_entry.delete(0,END)
    except:
        pass

def Consultfunc():
    for val in user.find({},{"username":1,"password":1}):
        a=val["username"]
        b=val["password"]
        box.insert(END,f"username : {a}  password : {b}")

def ConsultBox():
    window =Tk()
    #window.resizable(False,False)
    window.geometry("250x280")
    window.title("all users")

    scrollbar = Scrollbar(window, orient="vertical")
    Label(window,text="Users",font = ("Arial black", 10)).pack()
    global box
    box = Listbox(window,yscrollcommand=scrollbar.set)
    scrollbar.config(command=box.yview)
    scrollbar.pack(side="right", fill="y")
    box.pack(fill="both", expand=True)
    Button(window,text="Qui",command=window.destroy,width=300).pack()
    Consultfunc()
    window.mainloop()

Identification() 
