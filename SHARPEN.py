import hashlib as h
import sys
from colorama import Fore, Style, init
from RandPwd import randSalt	# The function that produces random text to be used for salting hashes

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

# These are the available hashing functions which are named trivially
# They all get the 'inp' input variable as their input


def SHA1(input_pass):

	hashed = h.sha1(input_pass.encode())
	outp = print("\nYour SHA-1 hashed password is: " + hashed.hexdigest())

	return outp


def SHA2(input_pass):

	hashed = h.sha256(input_pass.encode())
	salted_hash = randSalt()
	hashed.update(hashed + salted_hash)
	outp = print("\nYour SHA-2 (256 bit) hashed password is: " + hashed.hexdigest())

	return outp


def SHA3(input_pass):
	hashed = h.sha3_256(input_pass.encode())
	outp = print("\nYour SHA-3 (256 bit) hashed password is: "+ hashed.hexdigest())

	return outp

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
	SHA2(inp)

elif choose == 3:
	inp = str(input('\nEnter Your Password: '))
	SHA3(inp)

elif choose == 4:
	print(Fore.GREEN+"\nMy Ethereum Address is: " + Style.RESET_ALL)


else:
	raise ValueError(Fore.RED+"Error! Undefined input." + Style.RESET_ALL)
	sys.exit()