import hashlib as h
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

# All options
choose = int(input("Choose Your Option: \n \n* Text to SHA-256 converter (1) \n* Random Password Generator (2) \n* How does it work? (3) \n* Donations (4) \n"))


if choose == 1:
	inp = str(input('\nEnter Your Password: '))
	hashed = h.sha256(inp.encode())
	print("\n>> Your SHA-2 hashed password is: " + hashed.hexdigest())

elif choose == 2:
	# lg denotes the lengths of password
	lg = int(input(">> Enter Password length: "))
	password = randPass(lg)
	print(">> Your Random Password is: "+password)


elif choose == 3:
	print(">> 'Turnig's Wrath' is a random password generator and text-to-hash converter. It's extremely easy to use, just type the instruction numbers and stay safe on the internet.")


elif choose == 4:
	print(Fore.WHITE + ">> If you enjoyed Turnig's Wrath, please concider sending us your tips :) \n" + Style.RESET_ALL)
	print(Fore.GREEN+"\n>> Our Ethereum Address is: 0xaA845d9D5C588Ee6E63D55544faf15466fc7DEA6" + Style.RESET_ALL)

else:
	raise ValueError(Fore.RED+"Error! Undefined input value!" + Style.RESET_ALL)
	sys.exit()
