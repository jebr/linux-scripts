#!/usr/bin/env python3

# Python script to show syslog with option for line count

import subprocess
import argparse

parser = argparse.ArgumentParser(description='Python script to show syslog with row count')

def get_syslog(rows):
    print(f"=========== SYSLOG ({rows} ROWS) ============")
    subprocess.check_call(["tail", f"-n {rows}", "/var/log/syslog"])


def clear_screen():
    subprocess.check_call(["clear"])


clear_screen()

# Optional arguments
parser.add_argument("-r", "--rows", help="Row count for syslog", metavar="", type=int)
args = parser.parse_args()
if args.rows:
    clear_screen()
    get_syslog(args.rows)
else:
    parser.print_help()
