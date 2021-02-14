#!/usr/bin/env python3

# Python program to create a secure password

import argparse
import json
import pyperclip
import random
import os
import sys
import subprocess

try:
    os.chdir(os.path.dirname(sys.argv[0]))
except Exception:
    pass


# Resource path bepalen
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.environ.get("_MEIPASS2", os.path.abspath("."))
    # logging.info('Pyinstaller file location {}'.format(base_path))
    return os.path.join(base_path, relative_path)


# External Files
dict_dutch = resource_path('dictionaries/wordlist_dutch.json')
dict_english = resource_path('dictionaries/wordlist_english.json')

parser = argparse.ArgumentParser(description='Python password generator')

LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
CHARACTERS = "!@#$%^&*()_+-={}[]\\|?/<,>.:;"


def random_password_only_letter(length):
    password = create_password(length, characters=LETTERS)
    copy_password(password)
    leave(password)


def random_password_letter_numbers(length):
    password = create_password(length, characters=LETTERS+NUMBERS)
    copy_password(password)
    leave(password)


def random_password_letters_numbers_characters(length):
    password = create_password(length, characters=LETTERS+NUMBERS+CHARACTERS)
    copy_password(password)
    leave(password)


def random_dictionary_password_dutch(length):
    password_words = []
    password_number = create_password(4, characters=NUMBERS)
    count = length

    with open(dict_dutch) as w:
        words = json.load(w)

    while count > 0:
        word = random.choice(words)
        if (len(word) < 5) or (len(word) > 5):
            continue
        else:
            password_words.append(word)
            count -= 1

    password = str.join('.', password_words)
    password = password + "." + password_number

    copy_password(password)
    leave(password)


def random_dictionary_password_english(length):
    password_words = []
    password_number = create_password(4, characters=NUMBERS)
    count = length

    with open(dict_english) as w:
        words = json.load(w)

    while count > 0:
        word = random.choice(words)
        if (len(word) < 5) or (len(word) > 5):
            continue
        else:
            password_words.append(word)
            count -= 1

    password = str.join('.', password_words)
    password = password + "." + password_number

    copy_password(password)
    leave(password)


def create_password(length, characters):
    password = ""
    for i in range(length):
        char = random.choice(characters)
        password += char
    return password


def copy_password(password):
    pyperclip.copy(password)


def leave(password):
    print(f"Password is: {password}\nPassword is copied to your clipboard."
          f"\nThe password has a length of {len(password)} characters")
    sys.exit()


def clear_screen():
    subprocess.check_call("clear")


def main():
    clear_screen()
    parser.add_argument("-pl", "--pl", help="Create password with only "
                                            "letters. Add number after option"
                                            " for password length",
                        metavar="", type=int)
    parser.add_argument("-pln", "--pln", help="Create password with letters"
                                              " and numbers. Add number after"
                                              " option for password length",
                        metavar="", type=int)
    parser.add_argument("-plnc", "--plnc", help="Create password with letters,"
                                                " numbers and characters. "
                                                "Add number after option for"
                                                " password length",
                        metavar="", type=int)
    parser.add_argument("-pwrd", "--pwrd", help="Create password with words "
                                                "and numbers (NL) Add number "
                                                "after option for word count",
                        metavar="", type=int)
    parser.add_argument("-pwre", "--pwre", help="Create password with words "
                                                "and numbers (EN) Add number "
                                                "after option for word count.",
                        metavar="", type=int)

    args = parser.parse_args()
    if args.pl:
        random_password_only_letter(args.pl)
    if args.pln:
        random_password_letter_numbers(args.pln)
    if args.plnc:
        random_password_letters_numbers_characters(args.plnc)
    if args.pwrd:
        random_dictionary_password_dutch(args.pwrd)
    if args.pwre:
        random_dictionary_password_english(args.pwre)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()


