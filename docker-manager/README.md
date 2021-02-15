<p align="center">
	<img alt="Logo" src="https://raw.githubusercontent.com/jebr/linux-scripts/main/demo/images/docker-manager.jpg">
</p>

# Docker Manager Script

A script to manage Docker containers

# Preview

## Linux Update Help Menu
<img src="https://raw.githubusercontent.com/jebr/linux-scripts/main/demo/images/docker-manager.png">


# Installation

To use this application, follow the steps below:
1. Install curl if you haven't already

`sudo apt install curl`

2. Download the Docker Manager script

`curl -LJO https://raw.githubusercontent.com/jebr/linux-scripts/main/docker-manager/docker-manager.py`

3. Make the script executable

`sudo chmod +x docker-manager.py`

4. Start the program

`./docker-manager.py`


# Usage

The following options are available for using the application:

| Option         | Explanation                         |
|----------------|-------------------------------------|
| --ls or --list | List running docker containers      |
| --cc           | Clean up unused Docker Containers   |
| --ci           | Clean up unused Docker Images       |
| --cv           | Clean up unused Docker Volumes      |
| --cn           | Clean up unused Docker Networks     |
| --ca           | Cleaning up everything at once      |

# License

[GNU General Public License version 3](https://raw.githubusercontent.com/jebr/linux-scripts/v1.0/LICENSE)

<hr>

:star: this project in GitHub if you found this automation scripts helpful.
