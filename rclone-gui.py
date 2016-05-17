#!/usr/bin/python3

import tkinter as tk
from tkinter import messagebox
from tkinter import Button
import subprocess

class MainApplication(tk.Frame):
        def __init__(self, parent, *args, **kwargs):
                tk.Frame.__init__(self, parent, *args, **kwargs)
                parent.minsize(width=150,height=100)
                self.parent = parent
                # Create GUI here
                self.B = Button(self, text="Hello", command = self.configDB)
                self.C = Button(self, text="cmd", command = self.tst2)

                self.B.pack(side="top",fill="x",expand=True)
                self.C.pack(side="top",fill="x",expand=True)

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
