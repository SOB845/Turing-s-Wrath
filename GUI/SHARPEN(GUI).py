import tkinter as tk
from tkinter import *
from RandPwd import randPass

try:
	from tkinter import *
except ModuleNotFoundError:
	print("### pip install tkinter ###")
	raise

intro = "Welcome to S.H.A.R.P.E.N Password Generator. \nMove the slider to declare password length:"

def onClick():
	leng = sld.get()
	rand = randPass(leng)
	passw = Label(root, text=">> Here is your random password: \n"+ rand, bg="black", fg="white")
	passw.pack()

	return passw

def Donations():
	eth = Label(root, text=">> My Ethereum Address is: \n0xaA845d9D5C588Ee6E63D55544faf15466fc7DEA6", bg="green", fg="white")
	eth.pack()

	return eth

# Progam starts here
root = Tk()
root.title("S.H.A.R.P.E.N Password Generator")

intr = Label(root, text=intro, font="Helvetica")
intr.pack()

# Builds a simple slider for getting length of password
sld = Scale(root, from_=1, to=100, length=600, orient=HORIZONTAL)
sld.pack()

Generator = Button(root, text="Generate password", height=2, command=onClick)
Generator.pack(padx=10, pady=5)

Donate = Button(root, text="Felt useful? Donate now!", height=2, command=Donations)
Donate.pack(padx=20, pady=5)

quit = Button(root, text="QUIT", width=6, height=2, command=root.quit)
quit.pack()

root.geometry("600x600")
root.mainloop()	# to keep program running
