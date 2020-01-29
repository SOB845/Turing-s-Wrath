import hashlib as h
import sys
from colorama import Fore, Style, init
from RandPwd import randSalt
from 

try:
	from colorama import *
	init(convert=True)
except ModuleNotFoundError:
	print("### pip install colorama ###")
	raise

# This needs to be added in order to colorama change text colors properly

theLogo = ''' 
===============================================================================
||   ******** **      **     **     *******   *******  ******** ****     *** ||
||  **////// /**     /**    ****   /**////** /**////**/**///// /**/**   /**/ ||
|| /**       /**     /**   **//**  /**   /** /**   /**/**      /**//**  /**/ ||
|| /*********/**********  **  //** /*******  /******* /******* /** //** /**/ ||
|| ////////**/**//////** **********/**///**  /**////  /**////  /**  //**/**/ ||
||        /**/**     /**/**//////**/**  //** /**      /**      /**   //****/ ||
||  ******** /**     /**/**     /**/**   //**/**      /********/**    //***/ ||
|| ////////  //      // //      // //     // //       //////// //      ////  ||
===============================================================================

'''

# Regardless of the user's choice, prints Sharpen at the beginning
print(Fore.RED + theLogo + Style.RESET_ALL)

# All options
choose = int(input("Choose Your Option: \n \n* SHA-256 (1) \n* SHA-1 (2) \n* SHA3-256 (3) \n* Random Password Generator (4) \n* Donations (5) \n"))


if choose == 1:
	inp = str(input('\nEnter Your Password: '))
	hashed = h.sha1(inp.encode())
	print("\n>> Your SHA-1 hashed password is: " + hashed.hexdigest())


elif choose == 2:
	inp = str(input('\nEnter Your Password: '))
	hashed = h.sha1(inp.encode())
	print("\n>> Your SHA-1 hashed password is: " + hashed.hexdigest())

elif choose == 3:
	inp = str(input('\nEnter Your Password: '))
	hashed = h.sha1(inp.encode())
	print("\n>> Your SHA-1 hashed password is: " + hashed.hexdigest())

elif choose == 4:
	#lg denotes the lengths of password
	lg = int(input(">> Password length: "))
	password = randPass(lg)
	print(">> Your Random Password is: "+password)
	
elif choose == 5:
	print(Fore.WHITE + ">> If you enjoyed SHARPEN, please concider sending us your tips :) \n" + Style.RESET_ALL)
	print(Fore.GREEN+"\n>> My Ethereum Address is: 0xaA845d9D5C588Ee6E63D55544faf15466fc7DEA6" + Style.RESET_ALL)


else:
	raise ValueError(Fore.RED+"Error! Undefined input." + Style.RESET_ALL)
	sys.exit()
