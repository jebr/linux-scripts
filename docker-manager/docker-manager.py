#!/usr/bin/env python3

# Python program to manage Docker server

import os
import subprocess
import argparse

parser = argparse.ArgumentParser(description='Python script voor het updaten en beheren van docker containers')


def clear_screen():
    subprocess.check_call(["clear"])

def update_container():
    clear_screen()
    subprocess.check_call(["docker-compose", "pull"])
    subprocess.check_call(["docker-compose", "up", "-d"])

def list_docker_containers():
    clear_screen()
    subprocess.check_call(["docker", "ps"])

def clean_unused_containers():
    clear_screen()
    subprocess.check_call(["docker", "container", "prune", "-f"])

def clean_unused_images():
    clear_screen()
    subprocess.check_call(["docker", "image", "prune", "-f"])

def clean_unused_volumes():
    clear_screen()
    subprocess.check_call(["docker", "volume", "prune", "-f"])

def clean_unused_networks():
    clear_screen()
    subprocess.check_call(["docker", "network", "prune", "-f"])

def clean_everything():
    clear_screen()
    subprocess.check_call(["docker", "system", "prune", "-f"])

clear_screen()

# Optional arguments
parser.add_argument("--ls", "--list", help="List running docker containers", action="store_true")
parser.add_argument("--cc", help="Clean up unused Docker Containers", action="store_true")
parser.add_argument("--ci", help="Clean up unused Docker Images", action="store_true")
parser.add_argument("--cv", help="Clean up unused Docker Volumes", action="store_true")
parser.add_argument("--cn", help="Clean up unused Docker Networks", action="store_true")
parser.add_argument("--ca", help="Cleaning up everything at once", action="store_true")
args = parser.parse_args()
if args.ls:
    list_docker_containers()
elif args.cc:
    clean_unused_containers()
elif args.ci:
    clean_unused_images()
elif args.cv:
    clean_unused_volumes()
elif args.cn:
    clean_unused_networks()
elif args.ca:
    clean_everything()
else:
    parser.print_help()
