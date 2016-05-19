#!/usr/bin/python3

import os
import tkinter as tk
import signal

from tkinter import StringVar
from tkinter import messagebox
from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import simpledialog as sdg

import subprocess
import sys
import pexpect

class KeySimpleDialog(sdg.Dialog):

    def body(self, master):
        self.result = "default result"
        self.keytxt = StringVar()
        self.keylbl = Label(master, textvariable = self.keytxt).grid(row=0)
        self.keyentry = Entry(master,textvariable=self.keytxt)
        self.keytxt.set("[Key will go here]")
        self.grabbtn = Button(master, text="Grab Key from clipboard", command = self.grabKey).grid(row=1)

    def grabKey(self):
        print("Key: " + self.clipboard_get())
        self.keytxt.set(self.clipboard_get())
        self.result = self.clipboard_get()


    def apply(self):
        print("Apply caught.")
        print("Result: " + self.result)

    def validate(self):
        return 1

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        parent.minsize(width=250,height=100)
        self.parent = parent
        # Create GUI here
        self.btn_auth = Button(self, text="Authenticate", command = self.configDB)
        self.btn_import = Button(self, text="Import", command = self.importFiles)
        self.btn_export = Button(self, text="Export", command = self.exportFiles)
        self.btn_quit = Button(self,text="Quit", command=quit)

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

        ## Optional, only if there exists a config file already.
        try:
            child.expect('y/n> ',timeout=1)
            child.sendline('y')
        except pexpect.TIMEOUT:
            pass

        child.expect('https://.*response_type=code')

        mbrowser = subprocess.Popen(["/usr/bin/firefox", child.after], preexec_fn=os.setsid)

        mlines = ['Please sign in to your dropbox account', 'to allow rcopy to import/export data.', '', 'Your credentials are not read or stored by this process.', 'Once authenticated, copy and paste (ctrl-c, ctrl-v) the key', 'provided by dropbox into this dialog.', '']
        ##mykey = sdg.askstring("Key", "\n".join(mlines))
        d = KeySimpleDialog(root)
        mykey = d.result
        print("mykey: " + mykey)
        child.expect('Enter the code: ')

        ## Kill the browser.
        os.killpg(os.getpgid(mbrowser.pid), signal.SIGTERM)
        #print("Using key: " + mykey)
        child.sendline(mykey)

        child.expect('y/e/d> ')
        child.sendline('y')

        child.expect('e/n/d/s/q> ')
        child.sendline('q')

        child.close()
        messagebox.showinfo("Authentication","Authentication Successful.")


    def quit_proc(self):
        print("Quit event caught")
        quit()

    def tst2(self):
        stdoutdata = subprocess.getoutput("ls")
        messagebox.showinfo("Output",stdoutdata.split()[0])

    def importFiles(self):
        mimport = subprocess.call("/usr/bin/rclone copy ~/.unidata dropbox:unidata_sync/IDV",shell=True)
        messagebox.showinfo("Import","Files imported from dropbox:unidata_sync/IDV")

    def exportFiles(self):
        mexport = subprocess.call("/usr/bin/rclone copy ~/.unidata dropbox:unidata_sync/IDV",shell=True)
        messagebox.showinfo("Export","Files exported to dropbox:unidata_sync/IDV")

if __name__ == "__main__":
        root = tk.Tk()
        MainApplication(root).pack(side="top", fill="both", expand=True)

        root.mainloop()
