import tkinter as tk
from tkinter import *
from RandPwd import randPass

try:
	from tkinter import *
except ModuleNotFoundError:
	print("### pip install tkinter ###")
	raise

intro = "Welcome to Turing's Wrath: Password Generator. \nMove the slider to choose password length:"

def onClick():
	
	## Gets the value from slider and generates a password of that length.
	## If the value is less than 6, generates the password alongside a warning.
	
	leng = sld.get()
	if leng <= 6:
		warn = Label(root, text=">> For more secure passwords, make sure that length is greater than 6", bg="red", fg="white") 
		warn.pack()	
	rand = randPass(leng)
	textfield.insert(INSERT,">>Your password is: \n" + rand + '\n\n')

def Donations():
	textfield.insert(INSERT, ">> My Ethereum address: \n0xaA845d9D5C588Ee6E63D55544faf15466fc7DEA6" + '\n\n')


# Progam starts here
root = Tk()
root.title("Turing's Wrath")


# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )


# Introductary title
intr = Label(root, text=intro, font="Helvetica")
intr.pack()


# Builds a simple slider for getting the length of password
sld = Scale(root, from_=1, to=100, length=600, orient=HORIZONTAL)
sld.pack()


# Buttons
Generator = Button(root, text="Generate password", height=2, command=onClick)
Generator.pack(padx=20, pady=5, ipadx= 5, ipady= 2)

Donate = Button(root, text="Felt useful? Donate now!", height=2, command=Donations)
Donate.pack(padx=20, pady=5, ipadx=5, ipady=2)

quit = Button(root, text="QUIT", width=6, height=2, command=root.quit)
quit.pack(padx=20, pady=10, ipadx=5, ipady=2)


# Textfield in which the passwords and other command results are shown
textfield = Text(root, width=60, height=15, yscrollcommand = scrollbar.set, bd=3, wrap=WORD)
textfield.pack()


root.iconbitmap('image files/AlanTuring(32x32).ico')
root.geometry("700x600")
root.mainloop()	# Used to keep program running
