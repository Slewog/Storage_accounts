import Options  # Import of annex python files.

# ********* Import of python modules. *********
import os
import time
import shutil
import tkinter as tk


class Connect_window(object):  # Login pop-up with password.
    def __init__(self, master, ):
        self.loop = False  # Allows you to deactivate or not the popup after pressing the confirm button.
        self.login_file = "accounts.txt"
        self.folder = "file/" + self.login_file
        self.password_folder = "file/security"  # Path to password file.
        self.file_password = "password.txt"
        self.save_folder = "file/backup"  # Destination file for saving identifiers.
        self.save_file_rename = "accounts_" + self.date_formatting(time.localtime()) + ".txt"  # File name once saved.
        if not os.path.exists(self.save_folder):  # If the backup folder does not exist, it is created.
            os.mkdir(self.save_folder)
        self.number_file = len(os.listdir(self.save_folder))
        self.title_text = 'Accounts Storage - Page de connexion'  # Popup settings.
        self.color_bg = '#353535'  # Popup settings.
        self.color_fg = 'white'  # Popup settings.
        self.size_bd = 5  # Popup settings.
        self.font = 'Courier'  # Text settings.
        self.font_style = 'bold italic'  # Text settings.
        self.size = "375x200"  # Popup settings.
        self.window = master  # Arguments to interact with the main window and the connection popup window.
        self.attempts = 0  # Set the number of connection attempts to zero.
        if not os.path.exists(self.password_folder):  # If the security folder does not exist, it is created.
            os.mkdir(self.password_folder)
        if not os.path.exists(self.password_folder + '/' + self.file_password):  # If the file password doesn't exist, open pop-up create password.
            self.creation_password = tk.Toplevel(master)  # Create popup for create a password.
            self.creation_password.title(self.title_text)  # Popup settings.
            self.creation_password.geometry(self.size)  # Popup settings.
            self.creation_password.resizable(width=False, height=False)  # Popup settings.
            self.creation_password.config(background=self.color_bg)  # Popup settings.
            self.title_create = tk.Label(self.creation_password, text=" Créer mot de passe: ", font=(self.font, 20, self.font_style), bg=self.color_bg, fg=self.color_fg, justify=tk.CENTER)  # Title Frame.
            self.title_create.pack(expand=tk.YES)
            self.entry_password = tk.Entry(self.creation_password, show='*', bg=self.color_bg, fg=self.color_fg, width=20, bd=self.size_bd, font=(self.font, 14, self.font_style))  # Apply inputs.
            self.entry_password.pack(pady=7)  # Apply labels and inputs.
            self.button_confirm = tk.Button(self.creation_password, text='Confirmer', bg=self.color_bg, fg=self.color_fg, bd=self.size_bd, command=self.encrypt_password, font=(self.font, 20, self.font_style))  # Apply button.
            self.button_confirm.pack(expand=tk.YES)
            self.creation_password.bind('<Escape>', lambda e: self.window.destroy())  # Link the escape key to the popup displayed in order to exit the application if you close the popup.
            self.creation_password.bind('<Return>', lambda e: self.encrypt_password())  # When we press enter it validates the connection.
            self.creation_password.protocol("WM_DELETE_WINDOW", self.closing_app)  # Make sure that you close the popup with the cross that quits the application.
            Options.window_centering(self.creation_password)  # Centers the popup on the screen.
        else:  # Else open pop-up connect.
            self.login_window = tk.Toplevel(master)  # Create connexion popup.
            self.login_window.title(self.title_text)  # Popup settings.
            self.login_window.geometry(self.size)  # Popup settings.
            self.login_window.resizable(width=False, height=False)  # Popup settings.
            self.login_window.config(background=self.color_bg)  # Popup settings.
            self.title_connect = tk.Label(self.login_window, text=" Entrer mot de passe: ", font=(self.font, 20, self.font_style), bg=self.color_bg, fg=self.color_fg, justify=tk.CENTER).pack(expand=tk.YES)  # Apply inputs.
            self.password_entry = tk.Entry(self.login_window, show='*', bg=self.color_bg, fg=self.color_fg, width=20, bd=self.size_bd, font=(self.font, 14, self.font_style))  # Apply inputs.
            self.password_entry.pack(pady=7)
            self.button_connect = tk.Button(self.login_window, text='Connexion', bg=self.color_bg, fg=self.color_fg, bd=self.size_bd, command=self.cleanup, font=(self.font, 18, self.font_style)).pack(expand=tk.YES)  # Apply button.
            self.login_window.bind('<Escape>', lambda e: self.window.destroy())  # Link the escape key to the popup displayed in order to exit the application if you close the popup.
            self.login_window.bind('<Return>', lambda e: self.cleanup())  # When we press enter it validates the connection.
            self.login_window.protocol("WM_DELETE_WINDOW", self.closing_app)  # Make sure that you close the popup with the cross that quits the application.
            Options.window_centering(self.login_window)  # Centers the popup on the screen.

    def cleanup(self):  # Close the popup if the password and just otherwise display an error message.
        if self.password_entry.get() == self.decrypted_password():  # Check if the password is correct.
            self.save_file()  # Backup of the accounts file after authentication.
            self.loop = True
            self.login_window.destroy()  # Destroys the popup.
            self.window.deiconify()  # Displays the main window.
        else:
            self.attempts += 1  # Increment by 1 attempts.
            if self.attempts == 5:
                tk.messagebox.showerror('Fermeture application!', 'Êtes-vous sûr de connaître le mot de passe')
                Options.Write_log(" CONNECT ERROR !!! Fermeture forcée de l'application à cause de 5 erreurs mot de passe.")  # Write a message in the log indicating the number of tries.
                self.window.quit()  # Leave the application.
            else:
                self.password_entry.delete(0, 'end')  # Reset the empty input field.
                tk.messagebox.showerror('Mot de passe invalide !', 'Mot de passe invalide! Tentatives restantes: ' + str(5 - self.attempts))  # Show info message for say the password is invalid.

    def encrypt_password(self):  # Encrypted the  new password and save in file.
        encrypted_password = ''
        f = open(self.password_folder + '/' + self.file_password, "a")  # Open file password for append a password.
        for letter in self.entry_password.get():  # Encrypts password.
            if letter == ' ':
                encrypted_password += ' '
            else:
                encrypted_password += chr(ord(letter) + 5)
        f.write(encrypted_password)  # Write the encrypted password in the file.
        f.close()  # Close file log.
        Options.Write_log(" PSWD CREATE !!! Vous avez créer votre premier mot de passe de connexion.")  # Write a message for say one password has are define in log file.
        tk.messagebox.showinfo('Enregistrement Mot de passe', 'Votre mot de passe à bien été créer.')  # Show info message for confirmed the new password has been create.
        self.loop = True
        self.creation_password.destroy()  # Destroys the popup.
        self.window.deiconify()  # Displays the main window.

    def decrypted_password(self):  # Decrypts the password stored in its file
        if os.path.exists(self.password_folder + '/' + self.file_password):  # Check if the password file exists.
            password = ''
            f = open(self.password_folder + '/' + self.file_password, "r")
            encrypted = f.readline()
            f.close()
            for letter in encrypted:
                if letter == ' ':
                    password += ' '
                else:
                    password += chr(ord(letter) - 5)
            return password

    def save_file(self):  # Copied the file with date of execution in other folder.
        if self.number_file >= 5:  # If there are more than 5 files, we delete them to leave 2.
            while self.number_file > 2:
                file_list = os.listdir(self.save_folder)
                os.remove(r'' + self.save_folder + '/' + file_list[0])
                self.number_file = len(os.listdir(self.save_folder))
        if os.path.exists(self.save_folder + '/' + self.save_file_rename):
            Options.Write_log(" SAVE LEAVE !!! Il existe déja une sauvegarde du fichier identifiants à cette date.")
        else:
            shutil.copy(self.folder, self.save_folder)
            os.rename(r'' + self.save_folder + "/" + self.login_file, r'' + self.save_folder + "/" + self.save_file_rename)
            Options.Write_log(" SAVE OK !!! Sauvegarde du fichier identifiants.")
            tk.messagebox.showinfo('Sauvegarde', 'Fichier sauvegarder avec succès')

    def date_formatting(self, date):  # Put the date in order to add it to file names.
        date_list = [date.tm_mday, date.tm_mon, date.tm_year]  # , date.tm_hour, date.tm_min]
        index = 0
        while index < len(date_list):
            date_list[index] = self.zero_add_to_date(date_list[index])
            index += 1
        date_now = date_list[0] + '-' + date_list[1] + '-' + date_list[2]  # + 'à' + date_list[3] + 'H' + date_list[4]
        return date_now

    def zero_add_to_date(self, value):  # Add a zero if the number is less than or equal to 9.
        self.value = value
        if self.value <= 9:
            self.value = "0" + str(self.value)
        else:
            self.value = str(self.value)
        return self.value

    def closing_app(self):  # Close the application if you leave one of the pop-up windows.
        self.window.quit()  # Leave the application.
