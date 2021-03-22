#!/usr/bin/env python3

# Python script to setup Ansible master

import subprocess
import argparse
import getpass

parser = argparse.ArgumentParser(description='Python script to setup Ansible master')


def install_ansible():
    clear_screen()
    print("Installing Ansible...")
    subprocess.call(['sudo', 'apt', 'update', '-yy'])
    subprocess.call(['sudo', 'apt', 'install', 'software-properties-common', '-yy'])
    subprocess.check_call(['sudo', 'apt-add-repository', '--yes', '--update', 'ppa:ansible/ansible'])
    subprocess.check_call(['sudo', 'apt', 'install', 'ansible', '-yy'])
    clear_screen()
    print("Ansible installed")


def create_ppk():
    clear_screen()
    print("Creating private and public key...")
    subprocess.check_call(['ssh-keygen', '-t', 'rsa', '-b', '4096'])
    print("Private and public key created")


def copy_public_key():
    clear_screen()
    print("Copy public key to host.")
    host = input("Enter host IP address: ")
    username = input("Enter username of host: ")

    subprocess.check_call([f'ssh-copy-id', f'{username}@{host}'])


def define_hosts():
    # Create group to access Ansible hosts file
    subprocess.check_call(['sudo', 'groupadd', 'ansible'])
    subprocess.check_call(['sudo', 'usermod', '-aG', 'ansible', f'{getpass.getuser()}'])
    subprocess.check_call(['sudo', 'chown', f'{getpass.getuser()}:ansible', '/etc/ansible/hosts'])
    clear_screen()
    print("Define Ansible nodes one group add the time")
    print("Enter IP-addresses, hit enter to exit")
    hosts = []
    while True:
        host = input("IP address host: ")
        hosts.append(f'{host}\n')
        if host == "":
            break

    group_name = input("Enter group name of hosts: ")
    username = input("Enter username of hosts: ")

    # Add hosts to /etc/ansible/hosts
    with open('/etc/ansible/hosts', 'a') as inventory:
        inventory.write(f'[{group_name}]\n')

    for host in hosts:
        with open('/etc/ansible/hosts', 'a') as inventory:
            inventory.write(host)

    with open('/etc/ansible/hosts', 'a') as inventory:
        inventory.write(f'[{group_name}:vars]\nansible_username={username}')

    clear_screen()
    print("Hosts added to inventory")
    print("Test Ansible ping hosts...")
    subprocess.check_call(['ansible', '-m', 'ping', f'{group_name}'])


def clear_screen():
    subprocess.check_call(["clear"])


clear_screen()

# Optional arguments
parser.add_argument("--install", help="Install Ansible", action="store_true")
parser.add_argument("--ppk", help="Create private and public key", action="store_true")
parser.add_argument("--copy", help="Copy public key to host", action="store_true")
parser.add_argument("--hosts", help="Define hosts and test Ansible", action="store_true")

args = parser.parse_args()

if args.install:
    install_ansible()
elif args.ppk:
    create_ppk()
elif args.copy:
    copy_public_key()
elif args.hosts:
    define_hosts()
else:
    parser.print_help()
