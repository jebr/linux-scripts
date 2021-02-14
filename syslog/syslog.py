#!/usr/bin/env python3

# Python script voor het weergeven van de syslog met optie voor aantal regels

import subprocess
import argparse

parser = argparse.ArgumentParser(description='Python script voor het weergeven van de syslog')

def get_syslog(rows):
    print(f"=========== SYSLOG ({rows} ROWS) ============")
    subprocess.check_call(["tail", f"-n {rows}", "/var/log/syslog"])


def clear_screen():
    subprocess.check_call(["clear"])


# Optional arguments
parser.add_argument("-r", "--rows", help="Aantal rijen van de syslog", metavar="", type=int)
args = parser.parse_args()
if args.rows:
    clear_screen()
    get_syslog(args.rows)
else:
    parser.print_help()
