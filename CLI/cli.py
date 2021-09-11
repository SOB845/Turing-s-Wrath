import hashlib as hsl
from colorama import *
import sys
from RandPwd import randSalt
from RandPwd import randPass
from pwned import lookup_pwned_api


# This needs to be added in order to colorama change text colors properly
try:
	from colorama import *
	init(convert=True)
except ModuleNotFoundError:
	print("### pip install colorama ###")
	raise


theLogo = ''' 

  _______ _    _ _____  _____ _   _  _____ _  _____  __          _______         _______ _    _ 
 |__   __| |  | |  __ \|_   _| \ | |/ ____( )/ ____| \ \        / /  __ \     /\|__   __| |  | |
    | |  | |  | | |__) | | | |  \| | |  __|/| (___    \ \  /\  / /| |__) |   /  \  | |  | |__| |
    | |  | |  | |  _  /  | | | . ` | | |_ |  \___ \    \ \/  \/ / |  _  /   / /\ \ | |  |  __  |
    | |  | |__| | | \ \ _| |_| |\  | |__| |  ____) |    \  /\  /  | | \ \  / ____ \| |  | |  | |
    |_|   \____/|_|  \_\_____|_| \_|\_____| |_____/      \/  \/   |_|  \_\/_/    \_\_|  |_|  |_|
                                                                                                
                                                                                                
'''


# Regardless of the user's choice, prints Sharpen at the beginning
print(Fore.RED + theLogo + Style.RESET_ALL)

While True:
	print("\n")
	# All options
	choose = int(input("Choose Your Option: \n \n* Text to SHA-256 converter (1) \n* Random Password Generator (2) \n* How does it work? (3) \n* Exit (4) \n"))

	if choose == 1:
		inp = str(input('\nEnter Your Password: '))
		hashed = hsl.sha256(inp.encode())
		print("\n>> Your SHA-2 hashed password is: " + hashed.hexdigest())

	elif choose == 2:
		length = int(input(">> Enter Password length: "))
		i = 0
		while i < length:
			password = randPass(length)
			print(">> Your Random Password is: "+password)
			i+=1
			if i == 5:
				break


	elif choose == 3:
		print(">> 'Turnig's Wrath' is a random password generator and text-to-hash converter. It's extremely easy to use, just type the instruction numbers and stay safe on the internet.")
		
	elif choose = 4:
		sys.exit()
		
	else:
		raise ValueError(Fore.RED+"Error! Undefined input value!" + Style.RESET_ALL)
		sys.exit()
