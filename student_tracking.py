# Import all the needed modules
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sqlite3
import os

# Start with the Tkinter frame class and build out the User Interface
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Builds the main window
        self.master = master
        self.master.minsize(425,360)
        self.master.maxsize(425,360)
        self.master.title("Student Tracking")
        self.master.configure(bg="#f1f1f1")

        # Sets the option to use the Windows 'X' to close
        self.master.protocol("WM_DELETE_WINDOW", lambda: ask_quit(self))

        # creates the Label widgets/form on the window using the grid geometry
        self.lbl_fname = tk.Label(self.master, text='First Name:',font=("Industry Test", 11))
        self.lbl_fname.grid(row=1,column=1,padx=(25,0),pady=(10,0),sticky=N+W)
        self.lbl_lname = tk.Label(self.master, text='Last Name:',font=("Industry Test", 11))
        self.lbl_lname.grid(row=3,column=1,padx=(25,0),pady=(10,0),sticky=N+W)
        self.lbl_phone = tk.Label(self.master, text='Phone Number:',font=("Industry Test", 11))
        self.lbl_phone.grid(row=5,column=1,padx=(25,0),pady=(10,0),sticky=N+W)
        self.lbl_email = tk.Label(self.master, text='Email:',font=("Industry Test", 11))
        self.lbl_email.grid(row=7,column=1,padx=(25,0),pady=(10,0),sticky=N+W)
        self.lbl_course = tk.Label(self.master, text='Current Course:',font=("Industry Test", 11))
        self.lbl_course.grid(row=9,column=1,padx=(25,0),pady=(10,0),sticky=N+W)
        self.lbl_students = tk.Label(self.master, text='List of Students:',font=("Industry Test", 11))
        self.lbl_students.grid(row=1,column=2,rowspan=1,columnspan=3,padx=(0,0),pady=(10,0),sticky=N+W)

        # creates the listbox with scrollbar on the window using the grid geometry
        self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
        self.lstStudents = Listbox(self.master,font=("Industry Test", 9),exportselection=0,yscrollcommand=self.scrollbar1.set)
        self.lstStudents.bind('<<ListboxSelect>>',lambda event: onSelect(self,event))
        self.scrollbar1.config(command=self.lstStudents.yview)
        self.scrollbar1.grid(row=2,column=6,rowspan=9,columnspan=1,padx=(0,0),pady=(0,0),sticky=N+E+S)
        self.lstStudents.grid(row=2,column=2,rowspan=9,columnspan=4,padx=(0,0),pady=(0,0),sticky=N+E+S+W)

        # creates the Text Box widgets/form on the window using grid geometry
        self.txt_fname = tk.Entry(self.master,text='',font=("Industry Test", 9))
        self.txt_fname.grid(row=2,column=1,padx=(25,25),pady=(0,0),sticky=N+E+W)
        self.txt_lname = tk.Entry(self.master,text='',font=("Industry Test", 9))
        self.txt_lname.grid(row=4,column=1,padx=(25,25),pady=(0,0),sticky=N+E+W)
        self.txt_phone = tk.Entry(self.master,text='',font=("Industry Test", 9))
        self.txt_phone.grid(row=6,column=1,padx=(25,25),pady=(0,0),sticky=N+E+W)
        self.txt_email = tk.Entry(self.master,text='',font=("Industry Test", 9))
        self.txt_email.grid(row=8,column=1,padx=(25,25),pady=(0,0),sticky=N+E+W)
        self.txt_course = tk.Entry(self.master,text='',font=("Industry Test", 9))
        self.txt_course.grid(row=10,column=1,padx=(25,25),pady=(0,0),sticky=N+E+W)

        # creates the Button widget on the window using the grid geometry
        self.btn_submit = tk.Button(self.master,width=6,height=2,bg='green',fg='white',text='Submit',font=("Industry Test", 14),command=lambda: onSubmit(self))
        self.btn_submit.grid(row=11,column=1,padx=(0,20),pady=(25,0),sticky=E)
        self.btn_delete = tk.Button(self.master,width=6,height=2,bg='red',text='Delete',font=("Industry Test", 14),command=lambda: onDelete(self))
        self.btn_delete.grid(row=11,column=2,padx=(0,10),pady=(25,0))
        self.btn_close = tk.Button(self.master,width=6,height=2,bg='darkred',fg='white',text='Close',font=("Industry Test", 14),command=lambda: ask_quit(self))
        self.btn_close.grid(row=11,column=3,padx=(10,0),pady=(25,0),sticky=W)

        # Calls function to create the database
        createDB(self)
        onRefresh(self)

# Build functionality to the Windows 'X' feature
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Ok to close app?"):
        self.master.destroy
        os._exit(0)

# Creates the database table that we will use. Will check if it exists and if so will not create again.
def createDB(self):
    conn = sqlite3.connect('StudentDB.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_students( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            fname TEXT, \
            lname TEXT, \
            fullname TEXT, \
            phone TEXT, \
            email TEXT, \
            course TEXT \
            );")
        conn.commit()
    conn.close()

# Function when user clicks the Submit button and will add data to database. Error checking included.
def onSubmit(self):
    # Get data from form and normalize it for database integrity
    var_fname = self.txt_fname.get().strip().title()
    var_lname = self.txt_lname.get().strip().title()
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    var_course = self.txt_course.get()

    # Create full name from first and last for the database field
    var_fullname = ("{} {}".format(var_fname, var_lname))

    # Verify the email address is in valid format
    if not "@" or not "." in var_email:
        messagebox.showerror("Invalid Email Format:","Email is not in correct format.")

    # checks to verify all fields have data and then add to database
    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email) > 0) and (len(var_course) > 0):
        conn = sqlite3.connect('StudentDB.db')
        with conn:
            cur = conn.cursor()
            # check database for potential data entry duplication and set count to chkName
            cur.execute("""SELECT COUNT(fullname) FROM tbl_students WHERE fullname = '{}'""".format(var_fullname))
            chkName = cur.fetchone()[0]
            # if chkName = 0 then that name does not exist in database and we get data ready to be entered in database
            if chkName == 0:
                cur.execute("""INSERT INTO tbl_students (fname,lname,fullname,phone,email,course) VALUES (?,?,?,?,?,?)""",(var_fname,var_lname,var_fullname,var_phone,var_email,var_course))
                # Updates list box with new name
                self.lstStudents.insert(END,var_fullname)
                # Calls function to clear the textboxes
                onClear(self)
            else:
                # Displays error that name already exists in database also will then clear the textboxes
                messagebox.showerror("Name Error:","'{}' already exists in the database!\n\nPlease enter a different name.".format(var_fullname))
                onClear(self)
        # Commits data to the database at this point
        conn.commit()
        conn.close()
    else:
        # A text field was empty and now we will let the user know
        messagebox.showerror("Missing Data Error:","One or more text fields are missing data.\n\nPlease verify and update.")

# Function when user click the Delete button
def onDelete(self):
    var_select = self.lstStudents.get(self.lstStudents.curselection())
    conn = sqlite3.connect('StudentDB.db')
    with conn:
        cur = conn.cursor()

        # Verifies that this isn't the only record in the database. Removing the last one
        # will cause issues and errors. So let's not try that.
        cur.execute("""SELECT COUNT(*) FROM tbl_students""")
        count = cur.fetchone()[0]
        if count > 1:
            # Verifys the user wants to delete the record
            confirm= messagebox.askokcancel("Delete Confirmation:","{} is about to disappear forever from this database.\n\n Are you positive?".format(var_select))
            if confirm:
                cur.execute("""DELETE FROM tbl_students WHERE fullname = '{}'""".format(var_select))
                onClear(self)
                try:
                    index = self.lstStudents.curselection()[0]
                    self.lstStudents.delete(index)
                except IndexError:
                    pass
                conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Error:", "({}) is the last record in the database and cannot be deleted at this time. \n\nTo complete this deletion you will need to add another record first then you may attempt to delete ({}).".format(var_select,var_select))
    conn.close()

# Function when user click in the list box to display the data in the textboxes
def onSelect(self, event):
    var_list = event.widget
    select = var_list.curselection()[0]
    value = var_list.get(select)
    conn = sqlite3.connect('StudentDB.db')
    with conn:
        cur = conn.cursor()

        # Selects all data for selected name
        cur.execute("""SELECT fname, lname, phone, email, course FROM tbl_students WHERE fullname = (?)""",[value])
        varData = cur.fetchall()

        # With all data clear out the field first and then enter the new data
        for data in varData:
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])
            self.txt_course.delete(0,END)
            self.txt_course.insert(0,data[4])

# Function to clear all the text boxes
def onClear(self):
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_course.delete(0,END)

# Function to refresh the List box with all names from the database
def onRefresh(self):
    self.lstStudents.delete(0,END)
    conn = sqlite3.connect('StudentDB.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT COUNT(*) FROM tbl_students""")
        count = cur.fetchone()[0]
        i=0
        while i < count:
            cur.execute("""SELECT fullname from tbl_students""")
            varList = cur.fetchall()[i]
            for item in varList:
                self.lstStudents.insert(0,str(item))
                i += 1
    conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
