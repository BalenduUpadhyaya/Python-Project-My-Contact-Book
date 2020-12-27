from tkinter import *
from tkinter.ttk import *
from sqlite3 import *
from tkinter import messagebox
import home

class Loginwindow(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title("Login")
        self.geometry("300x250")

        s = Style()
        s.configure('hf.TFrame', background = 'blue')

        hf = Frame(self, style = 'hf.TFrame')
        hf.pack(fill = X)

        s.configure('hf.TLabel', background = 'blue', foreground = 'white', font = (NONE, 20))

        l = Label(hf, text = "My Contact Book", style = 'hf.TLabel')
        l.pack(pady = 10)

        s.configure('cf.TFrame', background = 'white')

        cf = Frame(self, style = 'cf.TFrame')
        cf.pack(fill = BOTH, expand = TRUE)

        lf = Frame(cf, style = 'cf.TFrame')
        lf.place(relx = .5, rely = .5, anchor = CENTER)

        s.configure('lf.TLabel', background = 'white', font = (NONE, 10))

        l1 = Label(lf, text = "Username: ", style = 'lf.TLabel')
        l1.grid(row = 0, column = 0)

        self.e1 = Entry(lf, font = (NONE, 10), width = 15)
        self.e1.grid(row = 0, column = 1, pady = 5)

        l2 = Label(lf, text = "Password: ", style = 'lf.TLabel')
        l2.grid(row = 1, column = 0)

        self.e2 = Entry(lf, font = (NONE, 10), width = 15, show = '*')
        self.e2.grid(row = 1, column = 1, pady = 5)

        s.configure('lf.TButton', font = (NONE, 10))        

        b = Button(lf, text = "Login", style = 'lf.TButton', width = 15, command = self.login_button_click)
        b.grid(row = 2, column = 1, pady = 5)
        b.bind('<Return>', self.login_button_click)

    def login_button_click(self, event = None):
        con = connect('mycontacts.db')
        cur = con.cursor()
        cur.execute("select * from Login where Username = ? and Password = ?", (self.e1.get(), self.e2.get()))
        row = cur.fetchone()
        if row is not None:
            self.destroy()
            home.Homewindow()
        else:
            messagebox.showerror("Error message", "Invalid username/password")

if __name__ == '__main__':
    lw = Loginwindow()
    lw.mainloop()
