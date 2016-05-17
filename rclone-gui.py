#!/usr/bin/python3

import tkinter as tk
from tkinter import messagebox
from tkinter import Button
import subprocess

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        parent.minsize(width=250,height=100)
        self.parent = parent
        # Create GUI here
        self.btn_auth = Button(self, text="Authenticate", command = self.configDB)
        self.btn_import = Button(self, text="Import", command = self.tst2)
        self.btn_export = Button(self, text="Export")
        self.btn_quit = Button(self,text="Quit")

        self.btn_auth.pack(side="top",fill="both",padx=10,expand=True)
        self.btn_import.pack(side="top",fill="both",padx=10,expand=True)
        self.btn_export.pack(side="top",fill="both",padx=10,expand=True)
        self.btn_quit.pack(side="bottom",fill="both",padx=10,expand=True)
        
        parent.bind('<Control-c>', self.quit_proc)

    def configDB(self):
        messagebox.showinfo("Hello Python", "Hello World")

    def quit_proc(self):
        print("Quit event caught")
        quit()

    def tst2(self):
        stdoutdata = subprocess.getoutput("ls")
        messagebox.showinfo("Outpout",stdoutdata.split()[0])





if __name__ == "__main__":
        root = tk.Tk()
        MainApplication(root).pack(side="top", fill="both", expand=True)

        root.mainloop()
