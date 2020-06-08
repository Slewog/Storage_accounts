# === Storage_accounts ===

# ![Window Connect](https://media.discordapp.net/attachments/715165934209335315/716755411750879332/storage_accounts_connect.PNG)

# Application to store identifiers and generate a password

# ![Window](https://media.discordapp.net/attachments/715165934209335315/716797950335909939/storage_accounts.PNG?width=968&height=677)

# How to use the script under Windows:

# 1 Set run.bat file:
- Update the path of the python interpreter in the file "run.bat".
- PS : If you don't have python installed, download it here and install it: https://www.python.org/downloads/windows/

# 2 Start the script:
- Start the script by double-clicking on run.bat.

# ===

# How to use the script under Linux:

# 1 Install the necessary libraries:
- Install the Tkinter library if you don't have it:
- sudo apt get update
- sudo apt install python3-tk
- sudo apt install python3-pip

# 2 Start the scripts:
- Launch the script from a terminal.

# ===

# Functions:
- Ask for a password when opening the application.
- Generate a password if necessary.
- Save the login in an encrypted file.
- Delete logins that are no longer up to date.

# Update 1.1:
- Addition of a backup function for the encrypted login file.
- Adding a window logo for windows don't work on linux.
- Now the password is no longer hard coded, you set it the first time you open the application. The password is encrypted in his file.
- Adding a log file where we find the actions performed and errors identified.
- Close the application if you leave one of the pop-up connexion windows.
- Options menu to change the password for connection to the application, view the log file, empty the list of identifiers.
- Windows no longer appear at random positions on the screen.
- You can modify a registered identifier without having to delete it before.
- Graphical interface changes.

# Developed by Slewog
