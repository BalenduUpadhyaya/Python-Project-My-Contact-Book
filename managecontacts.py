from tkinter import *
from tkinter.ttk import *
from sqlite3 import *
from tkinter import messagebox

class Managecontactsframe(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.pack(fill = BOTH, expand = TRUE)

        s = Style()
        s.configure('TFrame', background = 'white')
        s.configure('TButton', font = (NONE, 10), width = 20)
        s.configure('TLabel', background = 'white', font = (NONE, 10))

        self.con = connect('mycontacts.db')
        self.cur = self.con.cursor()

        self.create_view_all_contacts_frame()

    def create_view_all_contacts_frame(self):
        self.vcf = Frame(self)
        self.vcf.place(relx = .5, rely = .5, anchor = CENTER)

        b = Button(self.vcf, text = "Add New Contact",
        command = self.create_add_new_contact_frame)
        b.grid(row = 0, column = 0, columnspan = 2, sticky = E, pady = 25)

        l = Label(self.vcf, text = "Name: ")
        l.grid(row = 1, column = 0, sticky = W, pady = 10)

        self.e = Entry(self.vcf, width = 75)
        self.e.grid(row = 1, column = 1)
        self.e.bind('<KeyRelease>', self.name_entry_key_release)

        self.ctv = Treeview(self.vcf, columns = ('name', 'phone_number', 'email_id', 'city'),
        show = 'headings')
        self.ctv.grid(row = 2, column = 0, columnspan = 2, pady = 10)
        self.ctv.heading('name', text = "Name", anchor = W)
        self.ctv.heading('phone_number', text = "Phone Number", anchor = W)
        self.ctv.heading('email_id', text = "Email Id", anchor = W)
        self.ctv.heading('city', text = "City", anchor = W)
        self.ctv.column('name', width = 150)
        self.ctv.column('phone_number', width = 100)
        self.ctv.column('email_id', width = 150)
        self.ctv.column('city', width = 100)
        self.cur.execute("select * from Contact")
        self.fill_contacts_treeview()
        self.ctv.bind('<<TreeviewSelect>>', self.contacts_treeview_selection)

    def name_entry_key_release(self, event):
        self.cur.execute("select * from Contact where name Like ?", ('%' + self.e.get() + '%',))
        self.fill_contacts_treeview()

    def fill_contacts_treeview(self):
        for contact in self.ctv.get_children():
            self.ctv.delete(contact)
        
        contacts = self.cur.fetchall()

        for contact in contacts:
            self.ctv.insert("", END, values = contact)

    def contacts_treeview_selection(self, event):
        contact = self.ctv.item(self.ctv.selection())['values']
        self.vcf.destroy()
        self.create_update_delete_frame(contact)

    def create_add_new_contact_frame(self):
        self.vcf.destroy()
        self.ancf = Frame(self)
        self.ancf.place(relx = .5, rely = .5, anchor = CENTER)

        l1 = Label(self.ancf, text = "Name: ")
        l1.grid(row = 0, column = 0, sticky = W)

        self.e1 = Entry(self.ancf, font = (NONE, 10), width = 20)
        self.e1.grid(row = 0, column = 1, pady = 10)

        l2 = Label(self.ancf, text = "Phone Number: ")
        l2.grid(row = 1, column = 0, sticky = W)

        self.e2 = Entry(self.ancf, font = (NONE, 10), width = 20)
        self.e2.grid(row = 1, column = 1, pady = 10)

        l3 = Label(self.ancf, text = "Email Id: ")
        l3.grid(row = 2, column = 0, sticky = W)

        self.e3 = Entry(self.ancf, font = (NONE, 10), width = 20)
        self.e3.grid(row = 2, column = 1, pady = 10)

        l4 = Label(self.ancf, text = "City: ")
        l4.grid(row = 3, column = 0, sticky = W)

        self.c = Combobox(self.ancf, values = ('Noida', 'Greater Noida',
        'Delhi', 'Banglore', 'Pune'), font = (NONE, 10), width = 18)
        self.c.grid(row = 3, column = 1, pady = 10)

        b = Button(self.ancf, text = "Add", command = self.add_new_contact_button_click)
        b.grid(row = 4, column = 1, pady = 10)

    def add_new_contact_button_click(self):
            self.cur.execute("select * from Contact where EmailId = ?", (self.e3.get(),))
            contact = self.cur.fetchone()
            if contact is None:
                self.cur.execute("insert into Contact values (?, ?, ?, ?)",
                (self.e1.get(), self.e2.get(), self.e3.get(), self.c.get()))
                self.con.commit()
                messagebox.showinfo("Success Message", "Contact details are added successfully")
                self.ancf.destroy()
                self.create_view_all_contacts_frame()
            else:
                messagebox.showerror("Error Message", "Contact details are already added")

    def create_update_delete_frame(self, contact):
        self.udcf = Frame(self)
        self.udcf.place(relx = .5, rely = .5, anchor = CENTER)

        l1 = Label(self.udcf, text = "Name: ")
        l1.grid(row = 0, column = 0, sticky = W)

        self.e1 = Entry(self.udcf, font = (NONE, 10), width = 20)
        self.e1.grid(row = 0, column = 1, pady = 10)
        self.e1.insert(END, contact[0])

        l2 = Label(self.udcf, text = "Phone Number: ")
        l2.grid(row = 1, column = 0, sticky = W)

        self.e2 = Entry(self.udcf, font = (NONE, 10), width = 20)
        self.e2.grid(row = 1, column = 1, pady = 10)
        self.e2.insert(END, contact[1])

        l3 = Label(self.udcf, text = "Email Id: ")
        l3.grid(row = 2, column = 0, sticky = W)

        self.e3 = Entry(self.udcf, font = (NONE, 10), width = 20)
        self.e3.grid(row = 2, column = 1, pady = 10)
        self.e3.insert(END, contact[2])
        self.old_email_id =  contact[2]

        l4 = Label(self.udcf, text = "City: ")
        l4.grid(row = 3, column = 0, sticky = W)

        self.c = Combobox(self.udcf, values = ('Noida', 'Greater Noida',
        'Delhi', 'Banglore', 'Pune'), font = (NONE, 10), width = 18)
        self.c.grid(row = 3, column = 1, pady = 10)
        self.c.set(contact[3])

        b1 = Button(self.udcf, text = "Update", width = 15, command = self.update_button_click)
        b1.grid(row = 4, column = 0, pady = 10, sticky = W)

        b2 = Button(self.udcf, text = "Delete", width = 15, command = self.delete_button_click)
        b2.grid(row = 4, column = 1, pady = 10, sticky = E)

    def update_button_click(self):
        self.cur.execute("""update Contact set Name = ?, PhoneNumber = ?,
        EmailId = ?, City = ? where EmailId = ?""", (self.e1.get(), self.e2.get(), self.e3.get(),
        self.c.get(), self.old_email_id))
        self.con.commit()
        messagebox.showinfo("Success Message", "Contact details updated successfully")
        self.udcf.destroy()
        self.create_view_all_contacts_frame()

    def delete_button_click(self):
       if messagebox.askquestion('Confirmation Message', 'Are you sure to delete?') == 'yes':
           self.cur.execute("delete from Contact where EmailId = ?", (self.old_email_id,))
           self.con.commit()
           messagebox.showinfo("Success Message", "Contact details deleted successfully")
       self.udcf.destroy()
       self.create_view_all_contacts_frame()
        

        

        
