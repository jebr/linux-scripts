<p align="center">
	<img alt="Logo" src="https://raw.githubusercontent.com/jebr/linux-scripts/main/demo/images/password-generator-512x384.jpg">
</p>

# Password Generator (Linux terminal)

A password generator that can be used from the linux terminal.

You can choose to generator either a password or a passphrase. Supported languages for passphrases are Dutch and English.

After creating the password or passphrase, the password will be visible in the terminal and it will be copied to the clipboard, where you can paste the password with CTRL-V to the desired location. 

# Preview

## Password Generator Help Menu
<img src="https://raw.githubusercontent.com/jebr/linux-scripts/main/demo/images/password-gen-01.png">

## Example creating a password with only letters and a length of 64 characters
<img src="https://raw.githubusercontent.com/jebr/linux-scripts/main/demo/images/password-gen-02.png">


# Installation

To use this application, follow the steps below:
1. Download the latest release from the [link](https://github.com/jebr/linux-scripts/releases). 
2. Copy the application to the location of your choice. 
3. Make the program executable

`sudo chmod +x password-generator.py`

4. Start the application

`./password-generator`

# Usage

The following options are available for using the application: 

| Option                                | Explanation                                                                            |
|---------------------------------------|----------------------------------------------------------------------------------------|
| -pl or --pl [number of characters]    | Create password with only letters. Add a number for password length                    |
| -pln or --pln [number of characters]  | Create password with letters and numbers. Add a number for password length             |
| -plnc or --plnc [number of characters]| Create password with letters, numbers and characters. Add a number for password length |
| -pwrd or --pwrd [number of words]     | Create password with words and numbers (NL). Add number for word count                 |
| -pwre or --pwre [number of words]     | Create password with words and numbers (EN). Add number for word count                 |

# Releases

[Releases](https://github.com/jebr/linux-scripts/releases)

# License

[GNU General Public License version 3](https://raw.githubusercontent.com/jebr/linux-scripts/v1.0/LICENSE)

<hr>

:star: this project in GitHub if you found this automation scripts helpful.
