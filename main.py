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


def verbos_printer(verbose, message):
    # TODO: Add verbos printing
    """
    Prints out the message specified
    :param message: text that will be printed to the console
    :param verbose: boolean value of whether or not the user used the --verbose command
    :return:
    """
    if verbose:
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


def concat_ascii_chars(chars_dict):
    """
    Join the remaining chars sets into one string
    :param chars_dict: (dictionary) similar to all_chars variable
    :return: string of the concatenation of all the values in chars_dict
    """
    joined_string = ''

    for key in iter(chars_dict):
        shuffled_chars = shuffle_ascii_chars(chars_dict[key])
        joined_string += shuffled_chars

    shuffle_ascii_chars(joined_string)

    return joined_string


if args.exclude_chars:
    # Remove the char sets not wanted by the user
    for charset in args.exclude_chars:
        del all_chars[charset]
    # TODO: Refactor this code as its repeated
    chars = concat_ascii_chars(all_chars)

    chosen_chars = random.choices(list(chars), k=args.length)
    password = ''.join(chosen_chars)
else:
    chars = concat_ascii_chars(all_chars)

    chosen_chars = random.choices(list(chars), k=args.length)
    password = ''.join(chosen_chars)

if args.copy:
    pyperclip.copy(password)

print("password: ", password)



