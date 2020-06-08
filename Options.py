#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os  # Import of python modules.
import datetime
import webbrowser
import tkinter as tk
import tkinter.messagebox
from tkinter.scrolledtext import ScrolledText


class View_log:
    def __init__(self, master):
        self.window = master  # Arguments to interact with the main window and the connection popup window.
        self.file_location = "file/log.txt"  # Log file path.
        self.color_bg = '#353535'  # Popup settings.
        self.color_fg = 'white'  # Popup settings.
        self.font = 'Courier'  # Popup settings.
        self.font_style = 'bold italic'  # Text settings.
        self.font_button = 'Courier 12 bold italic'  # Text button settings.
        self.size = "950x550"  # Popup settings.
        self.size_bd = 5  # Popup settings.
        self.log_view = tk.Toplevel(master)  # Create popup.
        self.option_bar = tk.Menu(self.log_view)  # Create bar option.
        self.log_view.title('Accounts Storage - Fichier Journal')  # Popup settings.
        self.log_view.geometry(self.size)  # Popup settings.
        self.log_view.minsize(width=750, height=350)  # Popup settings.
        self.log_view.maxsize(width=1000, height=600)  # Popup settings.
        self.log_view.resizable(width=False, height=False)  # Popup settings.
        self.log_view.config(background=self.color_bg, menu=self.option_bar)  # Popup settings.
        self.option_menu = tk.Menu(self.option_bar, tearoff=0)  # Create menu option.
        self.option_bar.add_cascade(label="Options", menu=self.option_menu)  # Add cascading bar.
        self.menu_option_bar()  # Add menu to option bar.
        self.container_display = tk.Frame(self.log_view, background=self.color_bg)  # Create a container for the display.
        self.container_display.columnconfigure(0, weight=1)  # Make the container resizable.
        self.container_display.rowconfigure(1, weight=1)
        tk.Label(self.container_display, text="Fichier Journal :", bg=self.color_bg, fg=self.color_fg, font=(self.font, 22, self.font_style), width=15).grid(row=0, column=0, sticky=tk.EW, pady=5)
        self.text_window = ScrolledText(self.container_display, bg=self.color_bg, fg=self.color_fg, font=self.font_button, height=10, width=20)  # Create text display area.
        self.text_window.grid(row=1, column=0, sticky=tk.NS + tk.EW)
        self.container_display.grid(row=0, column=1, sticky=tk.NS + tk.EW)  # Apply the container in the windows.
        self.log_view.rowconfigure(0, weight=1)  # Make the window resizable.
        self.log_view.columnconfigure(1, weight=1)
        self.read_log()  # Read the log file.
        self.window.iconify()  # Hide main window.
        self.log_view.protocol("WM_DELETE_WINDOW", self.quit_log)  # Make sure that you close the popup with the cross that quits the application.
        self.log_view.bind('<Escape>', lambda e: self.quit_log())  # Link the escape key to the popup displayed in order to exit the application if you close the popup.
        window_centering(self.log_view)  # Centers the popup on the screen.

    def read_log(self):  # Read the log file and display.
        with open(self.file_location, encoding='utf-8') as log_file:
            self.text_window.delete("1.0", tk.END)
            self.text_window.insert("1.0", log_file.read())

    def menu_option_bar(self):  # Menu for options bar.
        self.option_menu.add_command(label="Rafraîchir la page", command=self.read_log)
        self.option_menu.add_command(label="Quitter", command=self.quit_log)

    def quit_log(self):
        self.log_view.destroy()  # Destroys the pop up.
        self.window.deiconify()  # Displays the main window.


class Write_log:
    def __init__(self, log_message):
        self.date_message_log = datetime.datetime.now().strftime("%d-%m-%Y à %H:%M:%S")
        self.log_location = "file/log.txt"  # Log file path
        self.content_log = []  #
        self.log_message = log_message  #
        self.manage_file()  #

    def manage_file(self):
        if not os.path.exists(self.log_location):
            f = open(self.log_location, "w+")
            f.close()
            self.write_result()
        else:
            f = open(self.log_location, "r")
            number_log = len(open(self.log_location).readlines())
            f.close()
            if number_log > 999:  # If it is more than 250 lines we rename it.
                f = open(self.log_location, "w+")
                f.close()
                self.write_result()
            else:
                self.write_result()

    def write_result(self):
        f = open(self.log_location, "r", encoding="utf-8")
        self.content_log = f.readlines()
        f.close()
        self.content_log.insert(0, self.date_message_log + ',' + self.log_message + '\n')
        f = open(self.log_location, "w", encoding="utf-8")
        for line in self.content_log:
            f.write(line)
        f.close()


# Change login password.
class Password_update:
    def __init__(self, master):
        self.answer = tkinter.messagebox.askquestion('Modifier mot de passe', 'Etes-vous sûr de vouloir modifier votre mot de passe ?')  # Make sure you are sure you want to change the login password.
        if self.answer == 'yes':
            self.window = master  # Arguments to interact with the main window and the connection popup window.
            self.update = tk.Toplevel(master)  # Create popup.
            self.color_bg = '#353535'  # Popup settings.
            self.color_fg = 'white'  # Popup settings.
            self.font = 'Courier bold'  # Text settings.
            self.font_style = 'bold italic'  # Text settings.
            self.size = "370x200"  # Popup settings.
            self.size_bd = 5  # Popup settings.
            self.update.title('Accounts Storage - Nouveaux mot de passe')  # Popup settings.
            self.update.geometry(self.size)  # Popup settings.
            self.update.resizable(width=False, height=False)  # Popup settings.
            self.update.config(background=self.color_bg)  # Popup settings.
            self.title_update = tk.Label(self.update, text=" Modifier mot de passe: ", font=(self.font, 20, self.font_style), bg=self.color_bg, fg=self.color_fg, justify=tk.CENTER)  # Apply labels and inputs.
            self.title_update.pack(expand=tk.YES)  # Apply labels and inputs.
            self.update_password = tk.Entry(self.update, show='*', bg=self.color_bg, fg=self.color_fg, width=20, bd=self.size_bd, font=(self.font, 14, self.font_style))  # Apply labels and inputs.
            self.update_password.pack(pady=7)  # Apply labels and inputs.
            self.button_confirm = tk.Button(self.update, text='Confirmer', bg=self.color_bg, fg=self.color_fg, bd=self.size_bd, font=(self.font, 20, self.font_style), command=self.encrypt_password)  # Apply labels and inputs.
            self.button_confirm.pack(expand=tk.YES)  # Apply labels and inputs.
            self.update.protocol("WM_DELETE_WINDOW", self.close_popup)  # Displays the main window if the popup is closed.
            self.update.bind('<Escape>', lambda e: self.update.destroy())  # Link the escape key to the popup displayed in order to exit the application if you close the popup.
            self.update.bind('<Return>', lambda e: self.encrypt_password())  # When we press enter it validates the connection.
            self.window.iconify()  # Hide main window.
            window_centering(self.update)  # Centers the popup on the screen.

    def encrypt_password(self):  # Encrypted the  new password and save in file.
        encrypted_password = ''  # Variable that contains the encrypted password.
        f = open("file/security/password.txt", "w")  # Open file password for append a password.
        for letter in self.update_password.get():  # Encrypts password.
            if letter == ' ':
                encrypted_password += ' '
            else:
                encrypted_password += chr(ord(letter) + 5)
        f.write(encrypted_password)  # Write the encrypted password in the file
        f.close()  # Close file log.
        Write_log(" PSWD UPDATE !!! Mot de passe de connexion modifier.")  # Write a message for say one new password has are define in log file.
        tk.messagebox.showinfo('Mise à jour mot de passe Mot de passe', 'Votre mot de passe à bien été modifier.')  # Show info message for confirmed the new password has been create.
        self.update.destroy()  # Destroys the popup.
        self.window.deiconify()  # Displays the main window.

    def close_popup(self):
        self.window.deiconify()  # Displays the main window.


# Displays the information popup window.
class About:
    def __init__(self, master):
        self.about = tk.Toplevel(master)  # Create popup.
        self.color_bg = '#353535'  # Popup settings.
        self.color_fg = 'white'  # Popup settings.
        self.font = 'Courier'  # Text settings.
        self.font_style = 'bold italic'  # Text settings.
        self.about.title('Accounts Storage - À propos')  # Popup settings.
        self.about.geometry("410x150")  # Popup settings.
        self.about.resizable(width=False, height=False)  # Popup settings.
        self.about.config(background=self.color_bg)  # Popup settings.
        self.about_title = tk.Label(self.about, text=" Cette application à été développée \n par Slewog", font=(self.font, 14, self.font_style), bg=self.color_bg, fg=self.color_fg, justify=tk.CENTER)  # Apply labels.
        self.about_title.pack()
        self.about_title.place(x=3, y=20)
        self.button = tk.Button(self.about, text='Voir le projet sur Github', bg=self.color_bg, fg=self.color_fg, bd=5, command=self.open_browser, font=(self.font, 14, self.font_style))  # Apply button.
        self.button.pack()
        self.button.place(x=60, y=85)
        window_centering(self.about)  # Centers the popup on the screen.

    def open_browser(self):  # Open the project's Github link.
        webbrowser.open('https://github.com/Slewog/Storage_accounts')
        self.about.destroy()


def geometry_list(g):  # Get window size and position.
    r = [i for i in range(0, len(g)) if not g[i].isdigit()]
    return [int(g[0:r[0]]), int(g[r[0] + 1:r[1]]), int(g[r[1] + 1:r[2]]), int(g[r[2] + 1:])]


def window_centering(screen):  # Calculates the center of the screen and applies it to the window.
    screen.update_idletasks()
    l, h, x, y = geometry_list(screen.geometry())
    screen.geometry("%dx%d%+d%+d" % (l, h, (screen.winfo_screenwidth() - l) // 2, (screen.winfo_screenheight() - h) // 2))