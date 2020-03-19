import argparse
import random
import string

import pyperclip
# TODO: README.md
all_chars = {
    'l': string.ascii_lowercase,
    'u': string.ascii_uppercase,
    'd': string.digits,
    'p': string.punctuation
}

parser = argparse.ArgumentParser(description="A password generator cli")

parser.add_argument("length",
                    type=int,
                    help="the length of the password to be generated")

parser.add_argument("-e", "--exclude-chars",
                    help="characters you want to be omitted. l for lowercase, u for uppercase, d for digits, "
                         "p for punctuation. Ensure that the length is specified before this command",
                    choices=['l', 'u', 'd', 'p'],
                    nargs='+')

parser.add_argument('-c', "--copy",
                    help="Copy the password to clipboard once generated",
                    action="store_true")

parser.add_argument('-v', "--verbose",
                    help="print out what it going on",
                    action="store_true")
args = parser.parse_args()

password = ''


def verbose_printer(verbose_val, message):
    """
    Prints out the message specified
    :param message: text that will be printed to the console
    :param verbose_val: boolean value of whether or not the user used the --verbose command
    :return:
    """
    if verbose_val:
        print(message)


def shuffle_ascii_chars(ascii_chars):
    """
    Shuffles the chars around in the string
    :param ascii_chars: string of ascii chars
    :return: a string shuffled around
    """
    char_list = list(ascii_chars)
    random.shuffle(char_list)
    return ''.join(char_list)


def concat_ascii_chars(chars_dict, verbose_val):
    """
    Join the remaining chars sets into one string
    :param verbose_val: boolean value of whether or not the user used the --verbose command
    :param chars_dict: (dictionary) similar to all_chars variable
    :return: string of the concatenation of all the values in chars_dict
    """
    verbose_printer(verbose_val=verbose_val, message="Starting to join all characters into a single value")

    joined_string = ''

    for key in iter(chars_dict):
        shuffled_chars = shuffle_ascii_chars(chars_dict[key])
        joined_string += shuffled_chars

    verbose_printer(verbose_val=verbose_val, message="Randomising all characters in the single value")

    shuffle_ascii_chars(joined_string)

    return joined_string


def generate_password(char_dict, length, verbose_val):
    """
    Generates the password chooses random chars
    :param verbose_val: boolean value of whether or not the user used the --verbose command
    :param length: length of the password required
    :param char_dict: dictionary of all the chars wanted which would be all_chars
    :return: a password
    """
    verbose_printer(verbose_val=verbose_val, message="Generating password")

    chars = concat_ascii_chars(chars_dict=char_dict, verbose_val=verbose_val)
    chosen_chars = random.choices(list(chars), k=length)
    return ''.join(chosen_chars)


verbose = args.verbose

if verbose:
    print("Verbose turned on")

if args.exclude_chars:
    # Remove the char sets not wanted by the user
    verbose_printer(verbose_val=verbose, message="Removing unwanted characters")
    for charset in args.exclude_chars:
        del all_chars[charset]

    password = generate_password(char_dict=all_chars, length=args.length, verbose_val=verbose)

else:
    password = generate_password(char_dict=all_chars, length=args.length, verbose_val=verbose)


if args.copy:
    verbose_printer(verbose_val=verbose, message="Copying password to clipboard")
    pyperclip.copy(password)

print("password: ", password)



