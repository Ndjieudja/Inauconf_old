

# --*-- coding: utf8 --*--
# !/usr/bin/env python3

# Code to create app to read .inc file

from tkinter import *


class Application(Frame):

    # main application
    def __init__(self):
        Frame.__init__(self)

        self.master.title("INC Reader")
        self.configure(bg = "dark grey", relief = GROOVE)
       
        # ============== Menu File ================
        fileMenu = Menubutton(self, text = "File", relief = SUNKEN, width = 10)
        fileMenu.pack()

        # deroulment part
        menu1 = Menu(fileMenu)

        menu1.add_command(label = "Open file....", underline = 1, command = self.parcourir)
        menu1.add_command(label = "Quit", underline = 0, command = self.quit)
     
        # intergrating of menu
        fileMenu.configure(menu = menu1)

        self.can = Canvas(self, bg = "light grey", height = 500, width = 700, borderwidth = 10)

        self.can.pack()
        self.pack()
        self.mainloop()


    def parcourir(self):

        from tkinter.filedialog import askopenfilename
        filename = askopenfilename()


if __name__ == "__main__":
    app = Application()





