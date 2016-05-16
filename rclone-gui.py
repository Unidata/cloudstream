#!/usr/bin/python3

import tkinter
from tkinter import messagebox

import subprocess

top = tkinter.Tk()

def quit(event):
        print("Quit event caught")
        top.quit()

def tst2():
        stdoutdata = subprocess.getoutput("ls")
        messagebox.showinfo("Outpout",stdoutdata.split()[0])

def tst():
        p = subprocess.Popen("echo hi", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout = []
        while True:
                line = p.stdout.readline()
                stdout.append(line)
                print(line),
                if line == '' and p.poll() != None:
                   break

        messagebox.showinfo("Contents",''.join(stdout))

def configDB():
        messagebox.showinfo("Hello Python", "Hello World")

B = tkinter.Button(top, text="Hello", command = configDB)
C = tkinter.Button(top, text="cmd", command = tst2)

B.pack()
C.pack()

top.bind('<Control-c>', quit)
top.mainloop()
