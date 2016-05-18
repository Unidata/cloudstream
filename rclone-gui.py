#!/usr/bin/python3

import tkinter as tk
from tkinter import messagebox
from tkinter import Button
from tkinter import simpledialog as sdg

import subprocess
import sys
import pexpect

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        parent.minsize(width=250,height=100)
        self.parent = parent
        # Create GUI here
        self.btn_auth = Button(self, text="Authenticate", command = self.configDB)
        self.btn_import = Button(self, text="Import", command = self.import)
        self.btn_export = Button(self, text="Export", command = self.export)
        self.btn_quit = Button(self,text="Quit")

        self.btn_auth.pack(side="top",fill="both",padx=10,expand=True)
        self.btn_import.pack(side="top",fill="both",padx=10,expand=True)
        self.btn_export.pack(side="top",fill="both",padx=10,expand=True)
        self.btn_quit.pack(side="bottom",fill="both",padx=10,expand=True)

        parent.bind('<Control-c>', self.quit_proc)

    def configDB(self):
        child = pexpect.spawnu('rclone config')
        child.logfile = sys.stdout

        child.expect(['n/s/q> ', 'e/n/d/s/q> '])
        child.sendline('n')

        child.expect('name> ')
        child.sendline('dropbox')

        child.expect('Storage> ')
        child.sendline('dropbox')

        child.expect('app_key> ')
        child.sendline('')

        child.expect('app_secret> ')
        child.sendline('')



        child.expect('https://.*response_type=code')

        subprocess.run(["/usr/bin/xdg-open", child.after])

        mykey = sdg.askstring("Key", "Key provided by dropbox.",initialvalue=self.clipboard_get())

        child.expect('Enter the code: ')
        #print("Using key: " + mykey)
        child.sendline(mykey)

        child.expect('y/e/d> ')
        child.sendline('y')

        child.expect('e/n/d/s/q> ')
        child.sendline('q')

        child.close()

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
