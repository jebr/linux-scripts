<p align="center">
	<img alt="Logo" src="https://raw.githubusercontent.com/jebr/linux-scripts/main/demo/images/syslog.jpg">
</p>

# Syslog script

A script to view a certain of rows from the Syslog (`/var/log/syslog`)

# Preview

## Syslog Help Menu
<img src="https://raw.githubusercontent.com/jebr/linux-scripts/main/demo/images/syslog.png">


# Installation

To use this application, follow the steps below:
1. Install curl if you haven't already

`sudo apt install curl`

2. Download the Docker Manager script

`curl -LJO https://raw.githubusercontent.com/jebr/linux-scripts/main/syslog/syslog.py`

3. Make the script executable

`sudo chmod +x syslog.py`

4. Start the program

`./syslog.py`


# Usage

The following options are available for using the application:

| Option         | Explanation                         |
|----------------|-------------------------------------|
| -r or --rows   | Row count for syslog                |

# License

[GNU General Public License version 3](https://raw.githubusercontent.com/jebr/linux-scripts/v1.0/LICENSE)

<hr>

:star: this project in GitHub if you found this automation scripts helpful.
