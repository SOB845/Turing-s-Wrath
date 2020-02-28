import tkinter as tk
from tkinter import *
from tkinter import messagebox
from RandPwd import randPass
from pwned import lookup_pwned_api


try:
	from tkinter import *
except ModuleNotFoundError:
	print("### pip install tkinter ###")
	raise

intro = "Welcome to Turing's Wrath: Password Generator. \nMove the slider to choose password length:"

def Generate():
	
	## Gets the value from slider and generates a password of that length.
	## If the value is less than 6, generates the password alongside a warning.
	
	leng = sld.get()
	if leng <= 6:
		messagebox.showwarning("Warning!", "For better password security, the length should be greater than 6.")
	rand = randPass(leng)
	textfield.insert(INSERT,">>Your password is: \n" + rand + '\n\n')


def checkPwnage():
	checkWin = tk.Toplevel(root)
	txt = Label(checkWin, text="Type in the password to check if it's pwned.")
	txt.pack()
	ent = Entry(checkWin,show="*")
	ent.pack()
	passw = ent.get()
	go = Button(checkWin, text="Search", command=lookup_pwned_api(passw))
	go.pack(padx=10, pady=5,ipadx=5, ipady=2)
	checkWin.geometry("250x200")
	
	
def Clear():
	textfield.delete(1.0,END)	

def Quit():
	ex = messagebox.askyesno("Quit?","Are you sure you want to exit the program?")
	print(ex)
	if ex:
		root.quit()


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

# Call lookup_pwned_api to see if entered password is safe.
CheckPwnage = Button(root, height=2, text="Check if pwned", command=checkPwnage)
CheckPwnage.pack(padx=20, pady=10, ipadx=5, ipady=2)

quit = Button(root, text="QUIT", width=6, height=2, command= Quit)
quit.pack(padx=20, pady=10, ipadx=5, ipady=2)


# Textfield in which the passwords and other command results are shown
textfield = Text(root, width=60, height=15, yscrollcommand = scrollbar.set, bd=3, wrap=WORD)
textfield.pack()

# Button to delete everything in text field
clrText = Button(root, text="Clear Everything", width=12, height=2, bg="red", command=Clear)
clrText.pack(padx= 20, pady=5, ipadx=5, ipady=2)


root.iconbitmap('image files/AlanTuring(64x64).ico')
root.geometry("700x600")
root.mainloop()	# Used to keep program running
