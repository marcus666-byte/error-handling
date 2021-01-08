from tkinter import *
from tkinter import messagebox

ourframe2 = Tk()


def status():
    ourframe2 = Tk()
    ourframe2.geometry("300x500")
    ourframe2.title("Error Handling")

    label3 = Label(ourframe2, text="Please enter amount in your account")
    label3.pack()
    entry3 = Entry(ourframe2)
    entry3.pack()

    def checkm():
        if int(entry3.get()) >= 3000:
            messagebox.showinfo("my status", "You qualify for the Malaysia trip. Congratulations. ")
        else:
            messagebox.showinfo("My status" , "Please deposit more funds for this excursion.")

    button3 = Button(ourframe2, text="Check Qualification", command=checkm)
    button3.pack()


myb = Button(ourframe2, text="check status", command=status)
myb.pack()
ourframe2.mainloop()