#!/usr/bin/env python3

# Python script voor het updaten van een Linux systeem

import subprocess
import argparse

parser = argparse.ArgumentParser(description='Python script voor het updaten van een Linux systeem')

def full():
    print("Updaten, upgraden en opschonen van het systeem...")
    subprocess.call(['sudo', 'apt-get', 'update', '-yy'])
    subprocess.call(['sudo', 'apt-get', 'dist-upgrade', '-yy'])

def update():
    print("Updaten van de repositories...")
    subprocess.call(['sudo', 'apt-get', 'update', '-yy'])

def upgrade():
    print("Upgraden van het systeem...")
    subprocess.call(['sudo', 'apt-get', 'dist-upgrade', '-yy'])

def clean():
    print("Opschonen van het systeem...")
    subprocess.call(['sudo', 'apt-get', 'autoremove', '-yy'])
    subprocess.call(['sudo', 'apt-get', 'autoclean'])

def leave():
    print("-----------------------------------")
    print("Update en upgrade is uitgevoerd en ")
    print("het systeem is opgeschoond         ")
    print("-----------------------------------")

def clear_screen():
    subprocess.check_call(["clear"])

# Optional arguments
parser.add_argument("--full", help="Volledige update van het systeem", action="store_true")
parser.add_argument("--update", help="Updaten van de repositories", action="store_true")
parser.add_argument("--upgrade", help="Upgraden van het systeem", action="store_true")
parser.add_argument("--clean", help="Opruimen van het systeem", action="store_true")
args = parser.parse_args()
if args.full:
    clear_screen()
    full()
    clean()
    clear_screen()
    leave()
elif args.update:
    clear_screen()
    update()
    clear_screen()
    print("Update van de repositories is uitgevoerd")
elif args.upgrade:
    clear_screen()
    upgrade()
    clear_screen()
    print("Het systeem is geupgraded")
elif args.clean:
    clear_screen()
    clean()
    clear_screen()
    print("Het systeem is opgeschoond")
else:
    parser.print_help()
