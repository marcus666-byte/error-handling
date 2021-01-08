from tkinter import *
from tkinter import messagebox

ourframe = Tk()
ourframe.geometry("500x500")
ourframe.title("Error Handling")

def verify():
    user_password1 = {"wade": "153", "pain": "555", "marc": "666", "gus": "223", "iron": "000", "gig": "454"}
    username = myentry1.get()
    password = myentry2.get()
    if (username, password) in user_password1.items():
        messagebox.showinfo("Checks", "Correct Login")
        ourframe.withdraw()
        import error2
        error2.status()
        
    else:
        messagebox.showinfo("Checks", "incorrect Login")


label1 = Label(ourframe, text="Enter username")
label1.pack()
myentry1 = Entry(ourframe, textvariable="username")
myentry1.pack()
myentry1.pack()
label2 = Label(ourframe, text="Enter password")
label2.pack()
myentry2 = Entry(ourframe, textvariable="password", show="*")
myentry2.pack()

mycheck = Button(ourframe, text="Check", command=verify)
mycheck.pack()
ourframe.mainloop()