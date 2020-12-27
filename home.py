from tkinter import *
from tkinter.ttk import *
import login
import changepassword
import managecontacts

class Homewindow(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title("Home")
        self.state("zoomed")

        s = Style()
        s.configure("hf.TFrame", background = 'blue')

        hf = Frame(self, style = "hf.TFrame")
        hf.pack(fill = X)

        s.configure('hf.TLabel', background = 'blue', foreground = 'white', font = (NONE, 20))

        hl = Label(hf, text = "My Contact Book", style = 'hf.TLabel')
        hl.pack(pady = 10)

        nf = Frame(self, style = "hf.TFrame")
        nf.pack(side = LEFT, fill = Y)

        s.configure('nf.TButton', width = 15, font = (NONE, 15))

        b1 = Button(nf, text = "Manage Contacts", style = 'nf.TButton',
        command = self.manage_contacts_button_click)
        b1.pack(ipady = 10, pady = 1)

        b2 = Button(nf, text = "Change Password", style = 'nf.TButton',
        command = self.change_password_button_click)
        b2.pack(ipady = 10, pady = 1)

        b3 = Button(nf, text = "Logout", style = 'nf.TButton', command = self.logout_button_click)
        b3.pack(ipady = 10, pady = 1)

        s.configure("cf.TFrame", background = 'white')

        self.cf = Frame(self, style = 'cf.TFrame')
        self.cf.pack(fill = BOTH, expand = TRUE)

        managecontacts.Managecontactsframe(self.cf)

    def logout_button_click(self):
        self.destroy()
        login.Loginwindow()

    def change_password_button_click(self):
        for inner_frame in self.cf.winfo_children():
            inner_frame.destroy()
        changepassword.Changepasswordframe(self.cf)

    def manage_contacts_button_click(self):
        for inner_frame in self.cf.winfo_children():
            inner_frame.destroy()
        managecontacts.Managecontactsframe(self.cf)
       





        
        
