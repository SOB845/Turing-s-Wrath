import hashlib as h
import sys
from colorama import Fore, Style, init
from RandPwd import randSalt

try:
	from colorama import *
except ModuleNotFoundError:
	print("### pip install colorama ###")
	raise

# This needs to be added in order to colorama change text colors properly
init(convert=True)


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
choose = int(input("Choose Your Option: \n \n* SHA-256 (1) \n* SHA-1 (2) \n* SHA3-256 (3) \n* Donations (4) \n"))


if choose == 1:
	inp = str(input('\nEnter Your Password: '))
	hashed = h.sha1(inp.encode())
	print("\nYour SHA-1 hashed password is: " + hashed.hexdigest())


elif choose == 2:
	inp = str(input('\nEnter Your Password: '))
	hashed = h.sha1(inp.encode())
	print("\nYour SHA-1 hashed password is: " + hashed.hexdigest())

elif choose == 3:
	inp = str(input('\nEnter Your Password: '))
	hashed = h.sha1(inp.encode())
	print("\nYour SHA-1 hashed password is: " + hashed.hexdigest())

elif choose == 4:
	print(Fore.GREEN+"\nMy Ethereum Address is: " + Style.RESET_ALL)


else:
	raise ValueError(Fore.RED+"Error! Undefined input." + Style.RESET_ALL)
	sys.exit()
