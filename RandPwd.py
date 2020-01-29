import random
from random import SystemRandom
from pwned import lookup_pwned_api
import string
import sys

def randSalt(length=5):
	letters = string.ascii_letters + string.digits
	r = ''.join(random.SystemRandom().choice(letters) for i in range(length))

	return r


def random_password(length):
	# Uses a combination of 52 lower-upper case letters,
	# 10 digits,
	# 15 symbols,
	# In total 7800 random possible characters
	symbols = '!@#$%^7&*()<>;:'
	chars = string.ascii_letters + string.digits + symbols
	p = ''.join(random.SystemRandom().choice(chars) for i in range(length))

	return p
