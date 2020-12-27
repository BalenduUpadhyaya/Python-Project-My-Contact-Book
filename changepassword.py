from tkinter import *
from tkinter.ttk import *
from sqlite3 import *
from tkinter import messagebox

class Changepasswordframe(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.place(relx = .5, rely = .5, anchor = CENTER)

        s = Style()
        s.configure('TFrame', background = 'white')

        s.configure('TLabel', background = 'white', font = (NONE, 10))

        l1 = Label(self, text = "Old Password: ")
        l1.grid(row = 0, column = 0)

        self.e1 = Entry(self, font = (NONE, 10), width = 15, show = '*')
        self.e1.grid(row = 0, column = 1, pady = 10)

        l2 = Label(self, text = "New Password: ")
        l2.grid(row = 1, column = 0)

        self.e2 = Entry(self, font = (NONE, 10), width = 15, show = '*')
        self.e2.grid(row = 1, column = 1, pady = 10)

        l3 = Label(self, text = "Confirm Password: ")
        l3.grid(row = 2, column = 0)

        self.e3 = Entry(self, font = (NONE, 10), width = 15, show = '*')
        self.e3.grid(row = 2, column = 1, pady = 10)

        s.configure('TButton', width = 15, font = (NONE, 10))

        b = Button(self, text = "Change Password", command = self.change_password_button_click)
        b.grid(row = 3, column = 1, pady = 10)

    def change_password_button_click(self):
        con = connect('mycontacts.db')
        cur = con.cursor()
        cur.execute("select * from Login where Password = ?", (self.e1.get(),))
        row = cur.fetchone()
        if row is not None:
            new_password = self.e2.get()
            confirm_password = self.e3.get()
            if new_password == confirm_password:
                cur.execute("update Login set Password = ? where Password = ?",
                (self.e2.get(), self.e1.get()))
                con.commit()
                messagebox.showinfo("Success Message", "Password is changed successfully")
            else:
                messagebox.showerror("Error Message", "New and confirm passwords didn't match")
        else:
            messagebox.showerror("Error Message", "Incorrect old password")
            
        
        


        


        
