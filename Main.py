#!/usr/bin/python3
# -*- coding: utf-8 -*-
import Options  # Import of annex python files.
import Connexion

import sys  # Import of python modules.
import string
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from functools import partial
from random import randint, choice

file = 'file/accounts.txt'  # Path to login file.
objects = []  # Create list for functions Read login file.
update_login = []  # List for login update.
update_login_select = []  # List for login update select.


class Application(tk.Tk):  # Application creation.
    def __init__(self):
        self.folder = file  # Retrieves the file variable.
        # ********* Window creation and settings. *********
        tk.Tk.__init__(self)  # Create window
        self.title('Accounts Storage - Page d\'acceuil')  # Window settings.
        self.geometry("1050x680")  # Window settings.
        self.option_bar = tk.Menu(self)  # Create bar option.
        self.color_bg = '#353535'  # Window settings.
        self.color_fg = 'white'  # Window settings.
        self.bd_entry = 5  # Window settings.
        self.bd_button = 5  # Window settings.
        self.font = 'Courier'  # Text settings.
        self.font_style = 'bold italic'  # Text settings.
        self.picture = 'assets/folder.png'  # Picture for header.
        self.config(background=self.color_bg, menu=self.option_bar)  # Window settings.
        self.resizable(width=False, height=False)  # Window settings.
        if sys.platform == 'win32':  # Check operating system execute by the computer.
            self.iconphoto(True, tk.PhotoImage(file=self.picture))  # Logo application if windows operating system.
        self.option_menu = tk.Menu(self.option_bar, tearoff=0)  # Create menu option.
        self.option_bar.add_cascade(label="Options", menu=self.option_menu)  # Add cascading bar.
        self.menu_option_bar()  # Add menu to option bar.
        self.header_frame = tk.Frame(self, bg=self.color_bg)  # Create header frame.
        self.header_frame.pack(side=tk.TOP)
        self.title_frame = tk.Frame(self.header_frame, bg=self.color_bg)  # Create title frame.
        self.title_frame.pack(side=tk.TOP)
        self.button_frame = tk.Frame(self, bg=self.color_bg)  # Create button frame.
        self.button_frame.pack(side=tk.TOP)
        self.title_label = tk.Label(self.title_frame, text='Bienvenue', font=(self.font, 30, self.font_style), bg=self.color_bg, fg=self.color_fg, anchor=tk.CENTER).grid(pady=5)  # Apply header elements.
        self.image = tk.PhotoImage(file=self.picture)  # Apply header elements.
        self.canvas_1 = tk.Canvas(self.title_frame, width=230, height=230, bg=self.color_bg, bd=0, highlightthickness=0)  # Apply header elements.
        self.canvas_1.create_image(230 / 2, 230 / 2, image=self.image)  # Apply header elements.
        self.canvas_1.grid()  # Apply header elements.
        self.scrollbar = tk.Canvas(self, bg=self.color_bg, height=580, highlightthickness=0)  # Create the canvas for the scrollbar.
        self.login_frame = tk.Frame(self.scrollbar, bg=self.color_bg, highlightthickness=0, padx=15)  # Create the frame that will be contained in the canvas to be scrollable.
        self.add_login = tk.Button(self.button_frame, text='Ajouter un identifiants', font=(self.font, 16, self.font_style), bg=self.color_bg, bd=self.bd_button, fg=self.color_fg, command=partial(Manage_login, self, self.login_frame, "add"))  # Apply button.
        self.add_login.pack(pady=5)
        self.space_frame = tk.Frame(self, bg=self.color_bg, height=52)  # Create space frame.
        self.space_frame.pack(fill=tk.X, pady=5)
        self.title_login = tk.Label(self, text='***** Liste identifiants enregistré: *****', font=(self.font, 14, self.font_style), bg=self.color_bg, fg=self.color_fg)  # Apply labels.
        self.title_login.pack()
        self.title_login.place(x=325, y=350)
        self.underline = tkFont.Font(self.title_login, self.title_login.cget("font"))  # Underlines the labels.
        self.underline.configure(underline=True)
        self.title_login.configure(font=self.underline)
        self.site_label = tk.Label(self, text='Site :', font=(self.font, 14, self.font_style), bg=self.color_bg, fg=self.color_fg)  # Apply labels.
        self.site_label.pack()
        self.site_label.place(x=55, y=381)
        self.site_label.configure(font=self.underline)  # Underlines the labels.
        self.name_label = tk.Label(self, text='Pseudo :', font=(self.font, 14, self.font_style), bg=self.color_bg, fg=self.color_fg)  # Apply labels.
        self.name_label.pack()
        self.name_label.place(x=225, y=381)
        self.name_label.configure(font=self.underline)  # Underlines the labels.
        self.email_label = tk.Label(self, text='Email :', font=(self.font, 14, self.font_style), bg=self.color_bg, fg=self.color_fg)  # Apply labels.
        self.email_label.pack()
        self.email_label.place(x=490, y=381)
        self.email_label.configure(font=self.underline)  # Underlines the labels.
        self.pass_label = tk.Label(self, text='MDP :', font=(self.font, 14, self.font_style), bg=self.color_bg, fg=self.color_fg)  # Apply labels.
        self.pass_label.pack()
        self.pass_label.place(x=755, y=381)
        self.pass_label.configure(font=self.underline)  # Underlines the labels.
        self.login_frame.grid()
        self.vbar = tk.Scrollbar(self, orient="vertical", command=self.scrollbar.yview)  # Create the scroll bar and apply it to the canvas.
        self.scrollbar.configure(yscrollcommand=self.vbar.set)
        self.vbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.scrollbar.pack(side=tk.BOTTOM, fil=tk.X)
        self.login_frame.bind('<Enter>', self._bound_to_mousewheel)  # Lets you link a function when you enter the canvass.
        self.login_frame.bind('<Leave>', self._unbound_to_mousewheel)  # Allows you to break the link with a function when you leave the canvas.
        self.login_frame.bind("<Configure>", lambda event, canvas=self.scrollbar: self.on_frame_configure(canvas))  # Link the canvas to the on frame configure function.
        self.scrollbar.create_window(0, 0, anchor=tk.N, window=self.login_frame)  # Display the canvas for the scrollbar with the frame contained in it.
        read_file_login(self.login_frame, self)  # Read the file for send to login_display.
        Options.window_centering(self)  # Center main window.
        Connexion.Connect_window(self)  # Show login popup.

    def menu_option_bar(self):  # Menu for options bar.
        self.option_menu.add_command(label="Modifier le mot de passe de connexion", command=partial(Options.Password_update, self))
        self.option_menu.add_command(label="Vidé la liste d'identifiants", command=self.clear_login_file)
        self.option_menu.add_command(label="Voir fichier Log", command=partial(Options.View_log, self))
        self.option_menu.add_command(label="À propos", command=partial(Options.About, self))
        self.option_menu.add_command(label="Quitter", command=self.quit)

    def _bound_to_mousewheel(self, event):  # Allows you to link the mouse wheel as a scroll function.
        self.scrollbar.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbound_to_mousewheel(self, event):  # Allows you to break the mouse wheel as a scroll function.
        self.scrollbar.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):  # Allows you to link the mouse entry on the canvas.
        self.scrollbar.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def on_frame_configure(self, canvas):  # Allows you to scroll the canvas without having to be on the scrollbar.
        canvas.configure(scrollregion=canvas.bbox("all"))

    def clear_login_file(self):  # Clean the login file.
        answer = tkinter.messagebox.askquestion('Supprimer', 'Etes_vous sûr de vouloir vidé votre liste d\'identifiants ?')  # Request confirmation.
        if answer == 'yes':
            Login_display.clear_login_file(self.login_frame)
            read_file_login(self.login_frame, self)


class Login_display:  # Decrypt the login list and display it in table form.

    def __init__(self, master, s, n, e, p, i, window):
        self.color_bg = '#353535'  # Window settings.
        self.color_fg = 'white'  # Window settings.
        self.bd_entry = 5  # Window settings.
        self.font = 'Courier'  # Text settings.
        self.font_style = 'bold italic'  # Text settings.
        self.bd_button = 5  # Window settings.
        self.window = master  # Window or display logins.
        self.screen = window
        self.site = s  # Recover encrypted site.
        self.password = p  # Recover encrypted password.
        self.name = n  # Recover encrypted name.
        self.email = e  # Recover encrypted email.
        self.i = i  # Get the count value of the read login file function.
        self.login_select = self.site + ',' + self.name + ',' + self.email + ',' + self.password + ',' + '\n'  # Identifiers select.
        self.delete_fail_login = self.site + ',' + self.name + ',' + self.email + ',' + self.password  # Identifiers select for log message.

        self.decryptedS = ""  # Variable that contains the values ​​once decrypted.
        self.decryptedN = ""
        self.decryptedE = ""
        self.decryptedP = ""
        for letter in self.site:
            if letter == ' ':
                self.decryptedS += ' '
            else:
                self.decryptedS += chr(ord(letter) - 5)
        for letter in self.name:
            if letter == ' ':
                self.decryptedN += ' '
            else:
                self.decryptedN += chr(ord(letter) - 5)
        for letter in self.email:
            if letter == ' ':
                self.decryptedE += ' '
            else:
                self.decryptedE += chr(ord(letter) - 5)
        for letter in self.password:
            if letter == ' ':
                self.decryptedP += ' '
            else:
                self.decryptedP += chr(ord(letter) - 5)

        self.label_site = tk.Entry(self.window, text=self.decryptedS, font=(self.font, 12, self.font_style), bg=self.color_bg, fg=self.color_fg, bd=self.bd_entry, width=15)  # Displays the decrypted logins.
        self.label_site.delete(0, tk.END)
        self.label_site.insert(0, self.decryptedS)
        self.label_name = tk.Entry(self.window, text=self.decryptedN, font=(self.font, 12, self.font_style), bg=self.color_bg, fg=self.color_fg, bd=self.bd_entry, width=17)
        self.label_name.delete(0, tk.END)
        self.label_name.insert(0, self.decryptedN)
        self.label_email = tk.Entry(self.window, text=self.decryptedE, font=(self.font, 12, self.font_style), bg=self.color_bg, fg=self.color_fg, bd=self.bd_entry, width=30)
        self.label_email.delete(0, tk.END)
        self.label_email.insert(0, self.decryptedE)
        self.label_pass = tk.Entry(self.window, text=self.decryptedP, font=(self.font, 12, self.font_style), bg=self.color_bg, fg=self.color_fg, bd=self.bd_entry, width=15)
        self.label_pass.delete(0, tk.END)
        self.label_pass.insert(0, self.decryptedP)
        self.update_button = tk.Button(self.window, text='Modifier', command=self.send_update, fg=self.color_fg, font=(self.font, 12, self.font_style), bg=self.color_bg, bd=self.bd_button)  # Add 2 options buttons.
        self.delete_button = tk.Button(self.window, text='X', fg='red', font=(self.font, 12, self.font_style), bg=self.color_bg, bd=self.bd_button, command=self.delete)

    def display(self):  # Table layout
        self.label_site.grid(row=0 + self.i, column=0, padx=5, pady=10, sticky=tk.W)
        self.label_name.grid(row=0 + self.i, column=1, padx=5, sticky=tk.W)
        self.label_email.grid(row=0 + self.i, column=2, padx=5)
        self.label_pass.grid(row=0 + self.i, column=3, padx=5, sticky=tk.E)
        self.update_button.grid(row=0 + self.i, column=4, padx=5, pady=5, sticky=tk.E)
        self.delete_button.grid(row=0 + self.i, column=5, padx=5, sticky=tk.E)

    def send_update(self):
        answer = tkinter.messagebox.askquestion('Modifications', 'Etes-vous sûr de vouloir modifiez cette identifiant ?')
        if answer == 'yes':
            update_login.extend([self.decryptedS, self.decryptedN, self.decryptedE, self.decryptedP])
            update_login_select.extend([self.login_select])
            Manage_login(self.screen, self.window, "edit")  # partial(Manage_login, window, self.window, "edit")

    def clear_login_file(self):
        for i in objects:
            i.destroy()
        f = open(file, 'w')
        f.close()

    def delete(self):  # Delete the line requested by the user from the file
        answer = tkinter.messagebox.askquestion('Supprimer', 'Etes_vous sûr de vouloir supprimer se login ?')  # Request confirmation.
        check_delete = True
        if answer == 'yes':
            for i in objects:
                i.destroy()

            f = open(file, 'r')  # Open the file for reading to retrieve the content in a list.
            login_list = f.readlines()
            f.close()

            decrypted_id = ''
            for letter in self.site:  # Client decryption for log file.
                if letter == ' ':
                    decrypted_id += ' '
                else:
                    decrypted_id += chr(ord(letter) - 5)

            decrypted_pseudo = ''
            for letter in self.name:  # Name decryption for log file.
                if letter == ' ':
                    decrypted_pseudo += ' '
                else:
                    decrypted_pseudo += chr(ord(letter) - 5)

            if not self.login_select in login_list:  # Check that the chosen login is in the list.
                check_delete = False
                Options.Write_log(" LOGIN DELETE ERROR !!! Impossible de supprimer l\'identifiant: " + self.delete_fail_login + ", supprimer le manuellement du fichiers accounts.txt")  # Write a message in the log indicating the number of tries.
                tk.messagebox.showerror('Beug à la suppression !', 'Oups... \n' + 'Tu semble être tombé sur une faille temporelle... \n' + 'Je ne peut pas effectuer cette action !\n' + 'Va voir fichier log pour contrôler l\'erreur:\n' + ' LOGIN DELETE ERROR !!!')
            else:
                login_list.pop(login_list.index(self.login_select))  # We remove the object from the list by its index

            f = open(file, "w")
            count = 0
            for line in login_list:
                f.write(line)
                count += 1
            f.close()
            read_file_login(self.window, self.screen)  # Update the login list displayed on the screen after deletion.
            if check_delete:
                Options.Write_log(" LOGIN DELETE !!! Vous avez supprimé l'identifiants du site: " + decrypted_id + ", avec le pseudo: '" + decrypted_pseudo + "'.")  # Write a message in the log to say that an identifier has been deleted.
                tk.messagebox.showinfo('Suppression identifiants', 'L\'identifiants du site "' + decrypted_id + "', avec le pseudo: '" + decrypted_pseudo + '" à bien été supprimer.')  # Displays an info window to confirm the deletion.

    def destroy(self):  # Table efface the line requested by the user.
        self.label_site.destroy()
        self.label_name.destroy()
        self.label_email.destroy()
        self.label_pass.destroy()
        self.delete_button.destroy()
        self.update_button.destroy()


class Manage_login:
    def __init__(self, master, frame, add_edit):
        self.window = master  # Arguments to interact with the main window and the connection popup window.
        self.frame = frame  # Arguments to interact with the frame where the logins are displayed.
        self.choice = add_edit
        if self.choice == "add":
            label_text = 'Indiquer l\'identifiant:'
            button_text = 'Enregistrer identifiant'
            title_popup = 'Accounts Storage - Enregistrer un identifiant'
        else:
            label_text = 'Modifier l\'identifiant:'
            button_text = 'Enregistrer modification'
            title_popup = 'Accounts Storage - Modifier un identifiant'
        self.folder = file
        self.color_bg = '#353535'  # Popup settings.
        self.color_fg = 'white'  # Popup settings.
        self.bd_entry = 5  # Popup settings.
        self.bd_button = 5  # Popup settings.
        self.font = 'Courier'  # Text settings.
        self.font_style = 'bold italic'  # Text settings.
        self.default_text = 'aucun'  # Default text for entries.
        self.login_manage = tk.Toplevel(master)  # Create popup.
        self.login_manage.title(title_popup)  # Popup settings.
        self.login_manage.geometry("700x350")  # Popup settings.
        self.login_manage.config(background=self.color_bg)  # Popup settings.
        self.login_manage.resizable(width=False, height=False)  # Popup settings.
        self.entity_label = tk.Label(self.login_manage, text=label_text, font=(self.font, 20, self.font_style), bg=self.color_bg, fg=self.color_fg)  # Apply header elements.
        self.entity_label.pack()
        self.entity_label.place(x=160, y=35)
        self.underline = tkFont.Font(self.entity_label, self.entity_label.cget("font"))  # Underlines the labels.
        self.underline.configure(underline=True)
        self.entity_label.configure(font=self.underline)
        self.site_label = tk.Label(self.login_manage, text='Site:', font=(self.font, 16, self.font_style), bg=self.color_bg, fg=self.color_fg)  # Apply labels.
        self.site_label.pack()
        self.site_label.place(x=190, y=90)
        self.underline_label = tkFont.Font(self.site_label, self.site_label.cget("font"))  # Underlines the labels.
        self.underline_label.configure(underline=True)
        self.site_label.configure(font=self.underline_label)
        self.name_label = tk.Label(self.login_manage, text='Nom utilisateur:', font=(self.font, 16, self.font_style), bg=self.color_bg, fg=self.color_fg)  # Apply labels.
        self.name_label.pack()
        self.name_label.place(x=365, y=90)
        self.name_label.configure(font=self.underline_label)
        self.site_entry = tk.Entry(self.login_manage, font=(self.font, 16, self.font_style), bg=self.color_bg, fg=self.color_fg, bd=self.bd_entry, width=15)  # Apply inputs.
        self.site_entry.pack()
        self.site_entry.place(x=125, y=122)
        self.name_entry = tk.Entry(self.login_manage, font=(self.font, 16, self.font_style), bg=self.color_bg, fg=self.color_fg, bd=self.bd_entry, width=15)  # Apply inputs.
        self.name_entry.pack()
        self.name_entry.place(x=365, y=122)
        self.email_label = tk.Label(self.login_manage, text='Email:', font=(self.font, 16, self.font_style), bg=self.color_bg, fg=self.color_fg)  # Apply labels.
        self.email_label.pack()
        self.email_label.place(x=185, y=170)
        self.email_label.configure(font=self.underline_label)
        self.pass_label = tk.Label(self.login_manage, text='Mot de passe:', font=(self.font, 16, self.font_style), bg=self.color_bg, fg=self.color_fg)  # Apply labels.
        self.pass_label.pack()
        self.pass_label.place(x=425, y=170)
        self.pass_label.configure(font=self.underline_label)
        self.email_entry = tk.Entry(self.login_manage, font=(self.font, 16, self.font_style), bg=self.color_bg, fg=self.color_fg, bd=self.bd_entry, width=20)  # Apply inputs.
        self.email_entry.pack()
        self.email_entry.place(x=90, y=202)
        self.password_entry = tk.Entry(self.login_manage, font=(self.font, 16, self.font_style), bg=self.color_bg, fg=self.color_fg, bd=self.bd_entry, width=15)  # Apply inputs.
        self.password_entry.pack()
        self.password_entry.place(x=405, y=202)
        self.button_frame = tk.Frame(self.login_manage, bg=self.color_bg)  # Create button frame.
        self.button_frame.pack()
        self.button_frame.place(x=18, y=265)
        if self.choice == "add":
            self.submit_button = tk.Button(self.button_frame, text=button_text, command=self.on_submit, font=(self.font, 14, self.font_style), bd=self.bd_button, bg=self.color_bg, fg=self.color_fg).grid(row=0, column=0, padx=50)  # Apply button.
            self.login_manage.bind('<Return>', lambda e: self.on_submit())  # When we press enter it validates the connection.
        else:
            self.submit_button = tk.Button(self.button_frame, text=button_text, command=self.on_update, font=(self.font, 14, self.font_style), bd=self.bd_button, bg=self.color_bg, fg=self.color_fg).grid(row=0, column=0, padx=50)  # Apply button.
            self.login_manage.bind('<Return>', lambda e: self.on_update())  # When we press enter it validates the connection.
        if self.choice == "add":
            self.site_entry.insert(0, self.default_text)  # Set the default entry text.
            self.name_entry.insert(0, self.default_text)
            self.email_entry.insert(0, self.default_text)
            generate_password(self.password_entry)  # Generates a password when the popup page is displayed.
        else:
            self.site_entry.insert(0, update_login[0])
            self.name_entry.insert(0, update_login[1])
            self.email_entry.insert(0, update_login[2])
            self.password_entry.insert(0, update_login[3])
            self.login_select = update_login_select[0]
            update_login.clear()
            update_login_select.clear()

        self.generate_pass_button = tk.Button(self.button_frame, text='Générer mot de passe', bd=self.bd_button, command=partial(generate_password, self.password_entry), font=(self.font, 14, self.font_style), bg=self.color_bg, fg=self.color_fg).grid(row=0,                                                                                                                                                                                                             column=1)  # Apply button.
        self.window.iconify()  # Hide main window.
        Options.window_centering(self.login_manage)  # Center main window.
        self.login_manage.protocol("WM_DELETE_WINDOW", self.window.deiconify)  # Make sure that you close the popup with the cross that quits the application.

    def on_submit(self):
        s = self.site_entry.get()
        n = self.name_entry.get()
        m = self.email_entry.get()
        p = self.password_entry.get()
        e = Login_add(self.frame, s, n, m, p)
        e.write()
        self.site_entry.delete(0, 'end')
        self.name_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')
        read_file_login(self.frame, self.window)
        self.site_entry.insert(0, 'aucun')
        self.name_entry.insert(0, 'aucun')
        self.email_entry.insert(0, 'aucun')
        self.login_manage.destroy()
        self.window.deiconify()  # Displays the main window.
        tk.messagebox.showinfo('Enregistrement login', 'Login ajouter avec succès \n' + 'Site : ' + s + '\nPseudo : ' + n + '\nEmail : ' + m + '\nMot de passe : ' + p)

    def on_update(self):
        answer = tkinter.messagebox.askquestion('Modifier', 'Confirmer vous cette modification ?')
        if answer == 'yes':
            site = self.site_entry.get()
            name = self.name_entry.get()
            email = self.email_entry.get()
            pswd = self.password_entry.get()
            result = Login_update(self.frame, site, name, email, pswd, self.login_select, self.window, self.frame)
            result.write()
            read_file_login(self.frame, self.window)
            self.login_manage.destroy()
            self.window.deiconify()  # Displays the main window.


class Login_update:
    def __init__(self, master, site, name, email, pswd, login_select, window, frame):
        self.folder = file
        self.site_update = site
        self.name_update = name
        self.email_update = email
        self.pswd_update = pswd
        self.window = window
        self.frame = frame
        self.login_select = login_select
        f = open(self.folder, "r")
        self.list_for_update = f.readlines()
        f.close()

    def write(self):
        check_delete = True
        encryptedSite = ""
        encryptedName = ""
        encryptedEmail = ""
        encryptedPswd = ""

        for letter in self.site_update:
            if letter == ' ':
                encryptedSite += ' '
            else:
                encryptedSite += chr(ord(letter) + 5)
        for letter in self.name_update:
            if letter == ' ':
                encryptedName += ' '
            else:
                encryptedName += chr(ord(letter) + 5)
        for letter in self.email_update:
            if letter == ' ':
                encryptedEmail += ' '
            else:
                encryptedEmail += chr(ord(letter) + 5)
        for letter in self.pswd_update:
            if letter == ' ':
                encryptedPswd += ' '
            else:
                encryptedPswd += chr(ord(letter) + 5)

        self.edit_login = encryptedSite + ',' + encryptedName + ',' + encryptedEmail + ',' + encryptedPswd + ',' + '\n'

        if not self.login_select in self.list_for_update:
            check_delete = False
            tk.messagebox.showerror('Beug à la modification !', 'Oups... \n' + 'Tu semble être tombé sur une faille temporelle... \n' + 'Je ne peut pas effectuer cette action !\n' + 'Ta devoir supprimer cette identifiant pour l\'enregistré à nouveaux !!!')
        else:
            self.list_for_update[self.list_for_update.index(self.login_select)] = self.edit_login

        f = open(self.folder, "w")
        for login in self.list_for_update:
            f.write(login)
        f.close()

        read_file_login(self.frame, self.window)
        if check_delete:
            Options.Write_log(" LOGIN UPDATE !!! Vous avez modifier l'identifiants du site: " + self.site_update + ", avec le pseudo: '" + self.name_update + "'.")
            tk.messagebox.showinfo('Modification login', 'Login modifié avec succès: \n' + 'Site: ' + self.site_update + '\nPseudo: ' + self.name_update + '\nEmail: ' + self.email_update + '\nMot de passe: ' + self.pswd_update)  # Displays an info window to confirm the deletion.


class Login_add:  # Encrypt the login and backup it to a file.
    def __init__(self, master, s, n, m, p):
        self.folder = file
        self.site = s
        self.name = n
        self.email = m
        self.password = p

    def write(self):
        f = open(self.folder, "a")

        encryptedS = ""
        encryptedN = ""
        encryptedE = ""
        encryptedP = ""

        for letter in self.site:
            if letter == ' ':
                encryptedS += ' '
            else:
                encryptedS += chr(ord(letter) + 5)
        for letter in self.name:
            if letter == ' ':
                encryptedN += ' '
            else:
                encryptedN += chr(ord(letter) + 5)
        for letter in self.email:
            if letter == ' ':
                encryptedE += ' '
            else:
                encryptedE += chr(ord(letter) + 5)
        for letter in self.password:
            if letter == ' ':
                encryptedP += ' '
            else:
                encryptedP += chr(ord(letter) + 5)

        f.write(encryptedS + ',' + encryptedN + ',' + encryptedE + ',' + encryptedP + ',' + '\n')
        f.close()
        Options.Write_log(" LOGIN ADD !!! Nouveaux identifiant pour le site: " + self.site)


def read_file_login(frame, window):  # Read the encrypted file and send to login_display.
    f = open(file, 'r')
    count = 0

    for login in f:
        login_encrypted = login.split(',')
        e = Login_display(frame, login_encrypted[0], login_encrypted[1], login_encrypted[2], login_encrypted[3], count, window)
        objects.append(e)
        e.display()
        count += 1
    f.close()


def generate_password(password_entry):  # Generates a password and displays it in the password_entry.
    punctuation = "#@_-"
    all_chars = string.ascii_letters + string.digits + punctuation
    password_genere = "".join(choice(all_chars) for x in range(randint(8, 12)))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password_genere)


# ********* Main code. *********
app = Application()  # Create main window.
app.withdraw()  # Hide the main window during the connection.
app.mainloop()  # Show main window.
