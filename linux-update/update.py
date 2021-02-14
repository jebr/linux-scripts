#!/usr/bin/env python3

# Python script to update Linux system

import subprocess
import argparse

parser = argparse.ArgumentParser(description='Python script to update your Linux system')

def full():
    print("Update, upgrade and clean the system...")
    subprocess.call(['sudo', 'apt-get', 'update', '-yy'])
    subprocess.call(['sudo', 'apt-get', 'dist-upgrade', '-yy'])

def update():
    print("Update repositories...")
    subprocess.call(['sudo', 'apt-get', 'update', '-yy'])

def upgrade():
    print("Upgrade system...")
    subprocess.call(['sudo', 'apt-get', 'dist-upgrade', '-yy'])

def clean():
    print("Cleanup the system...")
    subprocess.call(['sudo', 'apt-get', 'autoremove', '-yy'])
    subprocess.call(['sudo', 'apt-get', 'autoclean'])

def leave():
    print("-----------------------------------")
    print("Update upgrade done                ")
    print("The system is cleaned up           ")
    print("-----------------------------------")

def clear_screen():
    subprocess.check_call(["clear"])

clear_screen()

# Optional arguments
parser.add_argument("--full", help="Full update of the system", action="store_true")
parser.add_argument("--update", help="Update of repositories", action="store_true")
parser.add_argument("--upgrade", help="Upgrade of the system", action="store_true")
parser.add_argument("--clean", help="Cleanup the system", action="store_true")
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
    print("Update of repositories is done")
elif args.upgrade:
    clear_screen()
    upgrade()
    clear_screen()
    print("Upgrade system done")
elif args.clean:
    clear_screen()
    clean()
    clear_screen()
    print("The system is cleaned up")
else:
    parser.print_help()
