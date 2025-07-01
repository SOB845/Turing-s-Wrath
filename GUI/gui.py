import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from pwned import lookup_pwned_api
from randpass_generator import *
from string import ascii_letters, digits, punctuation
from Database import *
import os
import hashlib
import hmac


try:
	from tkinter import *
except ModuleNotFoundError:
	print("### pip install tkinter ###")
	raise

# HERE ARE THE ESSENTIAL FUNTIONS (REFERRED TO AS COMMANDS IN TKINTER) THAT KEEP THE PROGRAM RUNNING.
# UNLESS YOU KNOW WHAT YOU'RE DOING, PLEASE DON'T TOUCH THEM.

def ask_for_mainpass():
	global actual_password

	if not os.path.exists(mainpass_loc):
		pw = str(simpledialog.askstring("Set Password","Create a new Password",show="*"))
		recover = str(simpledialog.askstring("Recovery Word", "Where were you born?"))

		hashed_pw = hashlib.sha256(pw.encode('utf-8')).hexdigest()
		hashed_recover = hashlib.sha256(recover.encode('utf-8')).hexdigest()

		if not (pw or recover):
			sys.exit("Canceled")

		create_mainpass_database(hashed_pw,hashed_recover)
		messagebox.showinfo("Registered")

	else:
		input_pw = str(simpledialog.askstring("Login","Enter your Primary Password:",show="*"))
		hashed_input_pw = hashlib.sha256(input_pw.encode('utf-8')).hexdigest()

		if not input_pw:
			sys.exit("Canceled")
		connection = sqlite3.connect(mainpass_loc)
		cursor = connection.cursor()

		# Retreieve the current password saved in the Database and hash it
		actual_password = cursor.execute(''' SELECT Pass FROM main_password WHERE id = (SELECT MAX(id) FROM (SELECT id FROM main_password))''')
		actual_password = cursor.fetchone()[0] # Returns the query as a pure string instead of a tuple

		if hmac.compare_digest(str(actual_password), str(hashed_input_pw)):
			messagebox.showinfo("Correct","Entry Success!")
		elif not hmac.compare_digest(str(actual_password), str(hashed_input_pw)):
			messagebox.showerror("Unauthorized Access", "Wrong Password! Try Again.")
			sys.exit()

def Generate():
	## Gets the value from slider and generates a password of that length.
	textfield.config(state="normal")
	leng = sld.get()
	i = 0
	while i < 2:
		if leng <= 6:
			messagebox.showwarning("Warning!", "For higher password security, the length should be greater than 6.")
		elif NUMS.get() == 1 and SYMBS.get() == 1:
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
	Label(checkWin, text="Enter your password to see if it's been pwned (Requires internet connection)",font=('Ariel',11)).pack()
	Entry(checkWin, textvariable=GetTxt, width=30,bd=2).pack(pady=10)
	Button(checkWin, height=2, width= 7, text="SEARCH", command=call_lookup_api).pack(padx=1, pady=10, ipadx=5, ipady=1)
	Button(checkWin, height=2, width=7, text="BACK", command=Destroy_CheckPwnageWindow).pack(padx=1, pady=10, ipadx=5, ipady=1)
	checkWin.geometry("500x220")
	checkWin.iconbitmap('AlanTuring(64x64).ico')

def save_to_database():
	#Saves service name, username and password in the database
	#'e' stands for entry
	e1 = Service_Saver.get().lower() #Service name to lowercase
	e2 = Username_Saver.get() # Username
	e3 = Password_Saver.get() # Password

	if len(e1) == 0 or len(e3) == 0:
		messagebox.showerror("Error","Service and Password fields cannot be empty!")
	else:
		save_or_update_password(e1, e2, e3)
		savewin.destroy()
		messagebox.showinfo("Info", "Password Saved!")

def find_password(Service_Name, User_Name): #Connects to the database and looks for info of given Service name
	global res
	connection = sqlite3.connect(database_path)
	cursor = connection.cursor()

	# If no username was passed, it doesn't bother.
	# Otherwise returns the entry with expected username/email
	if User_Name =='':
		cursor.execute(''' SELECT * FROM (SELECT service,username,password,date_added FROM user_data WHERE service LIKE ?) WHERE date_added = (SELECT MAX(date_added)
		FROM (SELECT service,username,password,date_added FROM user_data WHERE service LIKE ?) )
		''',  (f'%{Service_Name}%', f'%{Service_Name}%') )
	else:
		cursor.execute('''
		SELECT * FROM (SELECT service,username,password,date_added FROM user_data WHERE service LIKE ? AND (username = ? OR username IS NULL OR username = ''))
		WHERE date_added = (SELECT MAX(date_added) FROM (SELECT service,username,password,date_added FROM user_data WHERE service LIKE ? AND (username = ? OR username IS NULL OR username = '') ))
		''', ( f'%{Service_Name}%', User_Name or None, f'%{Service_Name}%', User_Name or None))

	connection.commit()
	results = cursor.fetchall()

	for row in results:
		textfield.insert(INSERT, ">>"+"\n")
		textfield.insert(INSERT, row)
		textfield.insert(INSERT, "\n")

	textfield.config(state="disabled")
	connection.close()

# Find a password in the database ###############
def lookup_service():
	textfield.config(state="normal")
	sought_service = Search_Service_Saver.get().lower()
	sought_username = Search_Username_Saver.get()
	find_password(sought_service, sought_username)
####################################################

# Check user athenticity and update main password
def ConfirmChangePassword():
	Current = currentPass.get()
	Repeat_Current = ConfirmCurrentPass.get()
	New = NewPass.get()

	hashed_Current = hashlib.sha256(Current.encode('utf-8')).hexdigest()
	hashed_Repeat_Current = hashlib.sha256(Repeat_Current.encode('utf-8')).hexdigest()
	hashed_new = hashlib.sha256(New.encode('utf-8')).hexdigest()

	if not (Current or Repeat_Current or New):
		messagebox.showerror("Empty", "No textfields must be empty!")
	else:
		if not (hmac.compare_digest(str(hashed_Current), str(hashed_Repeat_Current)) and hmac.compare_digest(str(hashed_Current),actual_password) and
		hmac.compare_digest(str(hashed_Repeat_Current),actual_password)):
			messagebox.showerror("Error", "Two or more entries did no match!")
			updatewin.destroy()
		else:
			connection = sqlite3.connect(mainpass_loc)
			cursor = connection.cursor()

			Actual_Recovery = cursor.execute(''' SELECT Recovery FROM main_password WHERE id = (SELECT MAX(id) FROM (SELECT id FROM main_password))''')
			Actual_Recovery = cursor.fetchone()[0] # Returns the query as a pure string instead of a tuple

			create_mainpass_database(hashed_new, Actual_Recovery)
			messagebox.showinfo("Confirmed","Password Reset Successful!")
			updatewin.destroy()
		
########## WINDOWS #############

# SAVE WINDOW ###############################
def SaveWindow():
	global savewin
	savewin = Toplevel(root)
	Label(savewin, text="Type in the password and its associated service\n",font=('Ariel',12)).grid(row=0, column=1)
	Label(savewin,text="Service/App:").grid(row=1, column=0,ipady=10)
	Entry(savewin,width=35,bd=2, textvariable = Service_Saver).grid(row=1,column=1)

	Label(savewin, text="Username/Email:").grid(row=2,column=0,ipady=10)
	Entry(savewin,width=35,bd=2, textvariable = Username_Saver).grid(row=2,column=1)

	Label(savewin, text="Password:").grid(row=3,column=0,ipady=10)
	Entry(savewin,width=35,bd=2, textvariable = Password_Saver).grid(row=3,column=1)

	Button(savewin, text="SAVE",height=2, width=7, command=save_to_database).grid(row=4, column=1,padx=1, pady=18, ipadx=5, ipady=1)
	savewin.title("Save password")
	savewin.geometry("470x235")
	savewin.iconbitmap('AlanTuring(64x64).ico')
#################################################

# Search Window #####################################
def SearchWindow():
	global searchwin
	searchwin = Toplevel(root)
	Label(searchwin, text="Type in the name of the service\n",font=('Ariel',12)).grid(row=0, column=1)

	Label(searchwin,text="Service/App:").grid(row=1, column=0,ipady=10)
	Entry(searchwin,width=35,bd=2, textvariable=Search_Service_Saver).grid(row=1,column=1)

	Label(searchwin,text="Username/Email:").grid(row=2, column=0,ipady=10)
	Entry(searchwin,width=35,bd=2, textvariable=Search_Username_Saver).grid(row=2,column=1)

	Button(searchwin,text="Look Up",height=2, width=7, command=lookup_service).grid(row=3, column=1,padx=1, pady=18, ipadx=5, ipady=1)
	searchwin.title("Search Password")
	searchwin.geometry("400x250")
	searchwin.iconbitmap('AlanTuring(64x64).ico')
##################################################

# Update Main Password Window ####################
def UpdatePassWindow():
	global updatewin
	updatewin = Toplevel(root)
	Label(updatewin, text="To Update the main password please enter the current one\n",font=('Ariel',12)).grid(row=0, column=1)

	Label(updatewin,text="Current Password:").grid(row=1, column=0,ipady=10)
	Entry(updatewin,width=35,bd=2, textvariable=currentPass).grid(row=1,column=1)

	Label(updatewin,text="Repeat Current Password:").grid(row=2, column=0,ipady=10)
	Entry(updatewin,width=35,bd=2, textvariable=ConfirmCurrentPass).grid(row=2,column=1)

	Label(updatewin,text="New Password:").grid(row=3, column=0,ipady=10)
	Entry(updatewin,width=35,bd=2, textvariable=NewPass).grid(row=3,column=1)

	Button(updatewin,text="Confirm Update",height=2, width=7, command= ConfirmChangePassword).grid(row=4, column=1,padx=1, pady=20, ipadx=5, ipady=3)

	updatewin.title("Search Password")
	updatewin.geometry("550x300")
	updatewin.iconbitmap('AlanTuring(64x64).ico')
#################################################

def Clr():
	textfield.config(state="normal")
	textfield.delete(1.0,END)

def Quit():
	ex = messagebox.askyesno("Quit?","Are you sure you want to exit the program?")
	print(ex)
	if ex:
		root.quit()


### PROGRAM BEGINS FROM HERE ###############################################################################################
root = Tk()
root.title("Turing's Wrath")
root.withdraw()

ask_for_mainpass()

root.deiconify()

# Scrollbar #################################
scrollbar = Scrollbar(root)
scrollbar.grid(row=0, column=1,sticky='ns' )

intro = Label(root, text="Turing's Wrath: The Password Generator\nMove the slider to choose desired length", font=('Times',20))
intro.grid(row=0,column=1)
#############################################


#### Slider for choosing the length of random password
sld = Scale(root, from_=1, to=69, length=600, orient=HORIZONTAL)
sld.grid(row=5, column=1)
#############################################


### Text Variable storage ############################
NUMS = BooleanVar()	#Stores Boolean data for exclude_digits checkbox
SYMBS = BooleanVar() #Stores Boolean data for exclude_symbols checkbox
GetTxt = StringVar() #Stores entry data for call_lookup_api function
Service_Saver = StringVar() #Stores entry data for SaveWindow
Username_Saver = StringVar() #Stores entry data for SaveWindow
Password_Saver = StringVar() #Stores entry data for SaveWindow
Search_Service_Saver = StringVar() #Stores entry data for SearchWindow
Search_Username_Saver = StringVar() #Stores entry data for SearchWindow
currentPass = StringVar()	# Currently set Password
ConfirmCurrentPass = StringVar()
NewPass = StringVar()
#############################################


### Checkboxes ##############################
exclude_digits= Checkbutton(root, text="EXCLUDE NUMBERS FROM PASSWORD", variable = NUMS)
exclude_digits.grid(row=7,column=0)
exclude_symbols = Checkbutton(root, text="EXCLUDE SYMBOLS FROM PASSWORD", variable = SYMBS)
exclude_symbols.grid(row=7,column=1)
#############################################


### Buttons ################################################

Generator_Button = Button(root, text="GENERATE PASSWORD", height=2, bd = 8, command=Generate)
Generator_Button.grid(row=1,column=0,padx=20, pady=5, ipadx= 5, ipady = 2)

CheckPwnage = Button(root, height=2, text="CHECK IF PWNED", command=CheckPwnageWindow)
CheckPwnage.grid(row=2,column=0,padx=20, pady=10, ipadx=5, ipady=2)

Save = Button(root, text="SAVE PASSWORD", height=2, command=SaveWindow)
Save.grid(row=1,column=1,padx=20, pady=10, ipadx=5, ipady=2)

OpenSearch = Button(root, text="SEARCH SERVICE", height=2, command=SearchWindow)
OpenSearch.grid(row=2,column=1,padx=20, pady=10, ipadx=5, ipady=2)

UpdatePasswordButton = Button(root, height=2, text="Update Password", command= UpdatePassWindow)
UpdatePasswordButton.grid(row=3,column=1,padx=20, pady=10, ipadx=5, ipady=2)

quit = Button(root, text="QUIT", width=6, height=2, command=Quit)
quit.grid(row=4,column=1,padx=20, pady=10, ipadx=5, ipady=2)
############################################################


# The text field in which the random passwords are shown
textfield = Text(root, width=80, height=15, yscrollcommand = scrollbar.set, bd=3, wrap=WORD)
textfield.grid(row=6, column=1)

# Button to delete everything in the text field
clrText = Button(root, text="Clear Everything", width=12, height=2, fg="white" ,bg="red", command=Clr)
clrText.grid(row=3,column=0,padx= 20, pady=10, ipadx=5, ipady=2)

root.iconbitmap('AlanTuring(64x64).ico')
root.geometry("1080x720")
root.eval('tk::PlaceWindow . center')	# Centers the app window (NOT SO ACCURATELY)
root.mainloop()	# Keeps program running
