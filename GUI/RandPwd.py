import random
from random import SystemRandom
from pwned import lookup_pwned_api
import string
import sys

def randSalt(length = 5):
	letters = string.ascii_letters + string.digits
	r = ''.join(random.SystemRandom().choice(letters) for i in range(length))

	return r


def randPass(length):
	symbols = '~`!@#$%^&*()[]<>;:.?/-_+='
	chars = string.ascii_letters + string.digits + symbols
	p = ''.join(random.SystemRandom().choice(chars) for i in range(length))
	lookup_pwned_api(p)
	return p
