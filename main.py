import argparse
import random
import string

import pyperclip

all_chars = {
    'l': string.ascii_lowercase,
    'u': string.ascii_uppercase,
    'd': string.digits,
    'p': string.punctuation
}

parser = argparse.ArgumentParser(description="A password generator cli")

parser.add_argument("length", type=int,
                    help="the length of the password to be generated")

parser.add_argument("-e", "--exclude-chars", help="characters you want to be omitted. l for lowercase, u for "
                                                  "uppercase, d for digits, p for punctuation. Ensure this is the "
                                                  "last argument you call", choices=['l', 'u', 'd', 'p'], nargs='+')

parser.add_argument("-v", "--verbosity", action="count", default=0,
                    help="increase output verbosity")
args = parser.parse_args()

password = ''

if args.exclude_chars:
    chars = ''
    # Remove the char sets not wanted by the user
    for charset in args.exclude_chars:
        del all_chars[charset]

    # Join the remaining chars sets into one string
    for key in iter(all_chars):
        chars += all_chars[key]

    chosen_chars = random.choices(list(chars), k=args.length)
    password = ''.join(chosen_chars)
else:
    chars = ''
    # Join the remaining chars sets into one string
    for key in iter(all_chars):
        chars += all_chars[key]

    chosen_chars = random.choices(list(chars), k=args.length)
    password = ''.join(chosen_chars)

print(password)

response = input("Do you want to copy the password to your clipboard? y (yes), n (no): \n")

if response == 'y':
    pyperclip.copy(password)

# if args.verbosity >= 2:
#     print("the square of {} equals {}".format(2, 2))
# elif args.verbosity >= 1:
#     print("{}^2 == {}".format(2, 2))
# else:
#     print(2)
