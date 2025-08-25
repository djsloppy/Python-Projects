import tkinter as tk
from tkinter import *
import webbrowser

# Creates the GUI interface
class ParentWindow(Frame):
    # Sets the default frame for the GUI
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master.title("Web Page Generator")
        
        # creates the label, text input, and buttons
        self.btn_default = Button(self.master, text='Default HTML Page', width=30, height=2, command=self.defaultHTML)
        self.btn_default.grid(row=3, column=2,padx=(10,5), pady=(10,10), sticky=E)

        self.btn_custom = Button(self.master, text='Submit Custom Text', width=30, height=2, command=self.defaultHTML)
        self.btn_custom.grid(row=3, column=3,padx=(5,10), pady=(10,10), sticky=E)

        self.lbl = Label(self.master, text="Enter custom text or click the Default HTML page button:")
        self.lbl.grid(row=0, column=0, padx=(10,0), pady=(10,5), sticky=W)

        self.ety = Entry(self.master, width=100)
        self.ety.grid(row=1, column=0, columnspan=4, padx=(10,10), pady=(5,5), sticky=W+E)

    # creates the function to take the input (if any) and create the webpage then display it
    def defaultHTML(self):
        # Gets the custom text
        htmlText = self.ety.get()
        # checks to see if there is any custom text
        if htmlText == "":
            # if custom text is empty the will set the text to the default
            htmlText = "Stay tuned for our amazing summer sale!"
        # creates/opens the file index.html for writing to it.
        htmlFile = open("index.html", "w")
        # creates the content to the be added to the file
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        # actually writes the contect to the file here
        htmlFile.write(htmlContent)
        # closes the file
        htmlFile.close
        # displays the file in the web browser
        webbrowser.open_new_tab("index.html")
        # clears the Entry field of the custom data
        self.ety.delete(0,END)

# starts up the app
if __name__ == "__main__":
    # sets the root for the main frame
    root = tk.Tk()
    # starts the GUI
    App = ParentWindow(root)
    # keeps the frame running until closed
    root.mainloop()
