#!/usr/bin/python

import Tkinter
import tkMessageBox
import subprocess

top = Tkinter.Tk()

def tst():
	p = subprocess.Popen("ls", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	stdout = []
	while True:
		line = p.stdout.readline()
		stdout.append(line)
		print line,
		if line == '' and p.poll() != None:
			break
	tkMessageBox.showinfo("Contents",''.join(stdout))
	
def configDB():
	tkMessageBox.showinfo("Hello Python", "Hello WOrld")

B = Tkinter.Button(top, text="Hello", command = configDB)
C = Tkinter.Button(top, text="cmd", command = tst)

B.pack()
C.pack()

top.mainloop()
