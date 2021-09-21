import random
from random import SystemRandom
import string
from string import ascii_letters, digits, punctuation
from functools import partial

def Generator(letter_set, num_set, symb_set ,length):
    alphabet = letter_set + num_set + symb_set
    password = "".join(random.SystemRandom().choice(alphabet) for i in range(length))
    return password

xclude_digits = partial(Generator,ascii_letters,'',punctuation)
xclude_symbols = partial(Generator,ascii_letters,digits,'')
xclude_digits_and_symbols = partial(Generator, ascii_letters,'','')
