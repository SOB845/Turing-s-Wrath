import tkinter as tk
from tkinter import *
from tkinter import messagebox
from randpass_generator import *
from pwned import lookup_pwned_api
from string import ascii_letters, digits, punctuation


try:
	from tkinter import *
except ModuleNotFoundError:
	print("### pip install tkinter ###")
	raise


# HERE ARE THE ESSENTIAL FUNTIONS (REFERRED AS COMMANDS IN TKINTER) THAT KEEP THE PROGRAM RUNNING.
# UNLESS YOU KNOW WHAT YOU'RE DOING, PLEASE DON'T TOUCH THEM.

def Generate():
	## Gets the value from slider and generates a password of that length.
	textfield.config(state="normal")
	leng = sld.get()
	i = 0
	while i < 2:
		if leng <= 6:
			messagebox.showwarning("Warning!", "For higher password security, the length should be greater than 6.")
		elif NUMS.get()==1 and SYMBS.get()==1:
			textfield.insert(INSERT,">> " + xclude_digits_and_symbols(leng)+'\n')
		elif NUMS.get() == 1:
			textfield.insert(INSERT, ">> " + xclude_digits(leng) +'\n')
		elif SYMBS.get() == 1:
			textfield.insert(INSERT, ">> " + xclude_symbols(leng) + '\n')
		else:
			textfield.insert(INSERT,">> " + Generator(ascii_letters,digits,punctuation,leng) + '\n')
		i += 1
	textfield.config(state="disabled")


def Destroy_CheckPwnageWindow():
	checkWin.destroy()

def call_lookup_api():
	entered_password = GetTxt.get()
	lookup_entered_password = lookup_pwned_api(entered_password)
	if entered_password == "":
		Label(checkWin, text="Please type something").pack()
	elif lookup_entered_password > 0:
		Label(checkWin, text="This password is compromised", fg='red').pack()
	else:
		Label(checkWin, text="This password is not compromised", fg='green').pack()

def CheckPwnageWindow():
	global checkWin
	checkWin = Toplevel(root)
	checkWin.title("Check pwnage")
	Label(checkWin, text="Enter your password to see if it's been pwned (Requires internet connection)").pack()
	Entry(checkWin, textvariable=GetTxt, width=30,bd=2).pack()
	Button(checkWin, height=2, width= 7, text="SEARCH", command=call_lookup_api).pack(padx=1, pady=10, ipadx=5, ipady=1)
	Button(checkWin, height=2, width=7, text="BACK", command=Destroy_CheckPwnageWindow).pack(padx=1, pady=10, ipadx=5, ipady=1)
	checkWin.geometry("440x220")
	checkWin.iconbitmap('AlanTuring(64x64).ico')


def Clr():
	textfield.config(state="normal")
	textfield.delete(1.0,END)

def Quit():
	ex = messagebox.askyesno("Quit?","Are you sure you want to exit the program?")
	print(ex)
	if ex:
		root.quit()


## Progam starts here
root = Tk()
root.title("Turing's Wrath")

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )

intro = Label(root, text="Turing's Wrath: The Password Generator\nMove the slider to choose desired length", font=('Times',20))
intro.pack()

#### Slider for choosing the length of random password
sld = Scale(root, from_=1, to=100, length=600, orient=HORIZONTAL)
sld.pack()

### Data storage
NUMS = BooleanVar()	# Stores Boolean data for exclude_digits checkbox
SYMBS = BooleanVar() # Stores Boolean data for exclude_symbols checkbox
GetTxt = StringVar()	# Stores entry data for call_lookup_api function

### Checkboxes
exclude_digits= Checkbutton(root, text="EXCLUDE NUMBERS FROM PASSWORD", variable = NUMS)
exclude_digits.pack(side=TOP)
exclude_symbols = Checkbutton(root, text="EXCLUDE SYMBOLS FROM PASSWORD", variable = SYMBS)
exclude_symbols.pack(side=TOP)

### Buttons
Generator_Button = Button(root, text="GENERATE PASSWORD", height=2, command=Generate)
Generator_Button.pack(padx=20, pady=5, ipadx= 5, ipady = 2)
CheckPwnage = Button(root, height=2, text="CHECK IF PWNED", command=CheckPwnageWindow)
CheckPwnage.pack(padx=20, pady=10, ipadx=5, ipady=2)
quit = Button(root, text="QUIT", width=6, height=2, command=Quit)
quit.pack(padx=20, pady=10, ipadx=5, ipady=2)

# The text field in which the random passwords are shown
textfield = Text(root, width=60, height=15, yscrollcommand = scrollbar.set, bd=3, wrap=WORD)
textfield.pack()

# Button to delete everything in the text field
clrText = Button(root, text="Clear Everything", width=12, height=2, fg="white" ,bg="red", command=Clr)
clrText.pack(padx= 20, pady=10, ipadx=5, ipady=2)

root.eval('tk::PlaceWindow . center')	# Centers the app window (NOT SO ACCURATELY)
root.iconbitmap('AlanTuring(64x64).ico')
root.geometry("700x700")
root.mainloop()	# Keeps program running
