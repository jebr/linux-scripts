<p align="center">
	<img alt="Logo" src="https://raw.githubusercontent.com/jebr/linux-scripts/main/demo/images/ansible-setup.png">
</p>

# Deploy Ansible Master Server

A script to deploy Ansible with the following features:
  * Install Ansible
  * Create private and public key
  * Copy public key to node (host)
  * Add hosts with variables to Ansible inventory (/etc/ansible/hosts)
  * Test host connection with `ansible -m ping`

# Preview

## Linux Update Help Menu
<img src="https://raw.githubusercontent.com/jebr/linux-scripts/main/demo/images/ansible-terminal.png">


# Installation

To use this application, follow the steps below:
1. Install curl if you haven't already

`sudo apt install curl`

2. Download the Linux update script

`curl -LJO https://raw.githubusercontent.com/jebr/linux-scripts/main/ansible-setup/ansible-setup`

3. Make the script executable

`sudo chmod +x ansible-setup.py`

4. Start the program

`./ansible-setup.py`


# Usage

The following options are available for using the application:

| Option    | Explanation                   |
|-----------|-------------------------------|
| --install | Install Ansible               |
| --ppk     | Create private and public key |
| --copy    | Copy public key to host       |
| --hosts   | Define hosts and test Ansible |

# License

[GNU General Public License version 3](https://raw.githubusercontent.com/jebr/linux-scripts/v1.0/LICENSE)

<hr>

:star: this project in GitHub if you found this automation scripts helpful.
