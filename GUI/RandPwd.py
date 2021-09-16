import random
from random import SystemRandom
import string
import sys


def Secure_randPass(length):
	symbols = '`~!@#$%^&*()-=_+[]}{|\/;,.<>?'
	chars = string.ascii_letters + string.digits + symbols
	p = ''.join(random.SystemRandom().choice(chars) for i in range(length))
	return p

def randPass_without_digits_and_symbols(length):
	chars = string.ascii_letters
	password = ""
	while len(password) < length:
		password += random.SystemRandom().choice(chars)
	return password

def randPass_without_digits(length):
	symbols = '`~!@#$%^&*()-=_+[]}{|\/;,.<>?'
	chars = string.ascii_letters+symbols
	p = ""
	while len(p) < length:
		p += random.SystemRandom().choice(chars)
	return p

def randPass_without_symbols(length):
	chars = string.ascii_letters + string.digits
	p = ''.join(random.SystemRandom().choice(chars) for i in range(length))

	return p
