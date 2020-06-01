#!/usr/bin/python3.8
# coding: utf-8
import tkinter as tk
from tkinter import messagebox
import tkinter.messagebox
import string
from random import randint, choice

# Define the access password of this application
user_password = '1234'
folder = 'file/accounts.txt'

# window creation and settings
window = tk.Tk()
window.withdraw()
window.title('Stockage d\'identifiants')
window.geometry("975x650")
window.config(background='#353535')
window.resizable(width=False, height=True)

# Create an object list and login window
objects = []


class connect_window(object):
    loop = False
    attempts = 0

    def __init__(self, master):
        top = self.top = tk.Toplevel(master)
        top.title('Fenêtre de connexion')
        top.geometry('{}x{}'.format(350, 200))
        top.resizable(width=False, height=False)
        top.config(background='#353535')
        self.l = tk.Label(top,text=" Mot de Passe: ", font=('Courier', 20), bg='#353535', fg='white', justify=tk.CENTER)
        self.l.pack(expand=tk.YES)
        self.e = tk.Entry(top, show='*', bg='#353535', fg='white', width=20, font=('Courier', 14))
        self.e.pack(pady=7)
        self.b = tk.Button(top, text='Connexion', bg='#353535', fg='white', command=self.cleanup, font=('Courier', 18))
        self.b.pack(expand=tk.YES)

    # Close the popup if the password and just otherwise display an error message
    def cleanup(self):
        self.value = self.e.get()
        access = user_password
        if self.value == access:
            self.loop = True
            self.top.destroy()
            window.deiconify()
        else:
            self.attempts += 1
            if self.attempts == 5:
                window.quit()
            self.e.delete(0, 'end')
            messagebox.showerror('Mot de passe invalide !', 'Mot de passe invalide! Tentatives restantes: ' + str(5 - self.attempts))


# Encrypt the login and save it to a file
class entity_add:

    def __init__(self, master, s, n, p, e):
        self.site = s
        self.password = p
        self.name = n
        self.email = e
        self.window = master

    def write(self):
        f = open(folder, "a")
        s = self.site
        n = self.name
        e = self.email
        p = self.password

        encryptedS = ""
        encryptedN = ""
        encryptedE = ""
        encryptedP = ""

        for letter in s:
            if letter == ' ':
                encryptedS += ' '
            else:
                encryptedS += chr(ord(letter) + 5)
        for letter in n:
            if letter == ' ':
                encryptedN += ' '
            else:
                encryptedN += chr(ord(letter) + 5)
        for letter in e:
            if letter == ' ':
                encryptedE += ' '
            else:
                encryptedE += chr(ord(letter) + 5)
        for letter in p:
            if letter == ' ':
                encryptedP += ' '
            else:
                encryptedP += chr(ord(letter) + 5)

        f.write(encryptedS + ',' + encryptedN + ',' + encryptedE + ',' + encryptedP + ',' + '\n')
        f.close()


# Decrypt the login list and display it in table form
class entity_display:

    def __init__(self, master, s, n, e, p, i):
        self.site = s
        self.password = p
        self.name = n
        self.email = e
        self.window = master
        self.i = i

        decryptedS = ""
        decryptedN = ""
        decryptedE = ""
        decryptedP = ""
        for letter in self.site:
            if letter == ' ':
                decryptedS += ' '
            else:
                decryptedS += chr(ord(letter) - 5)
        for letter in self.name:
            if letter == ' ':
                decryptedN += ' '
            else:
                decryptedN += chr(ord(letter) - 5)
        for letter in self.email:
            if letter == ' ':
                decryptedE += ' '
            else:
                decryptedE += chr(ord(letter) - 5)
        for letter in self.password:
            if letter == ' ':
                decryptedP += ' '
            else:
                decryptedP += chr(ord(letter) - 5)

        self.label_site = tk.Label(self.window, text=decryptedS, font=('Courier', 14), bg='#353535', fg='white', pady=5)
        self.label_name = tk.Entry(self.window, text=decryptedN, font=('Courier', 12), bg='#353535', fg='white', width=17)
        self.label_name.delete(0, tk.END)
        self.label_name.insert(0, decryptedN)
        self.label_email = tk.Entry(self.window, text=decryptedE, font=('Courier', 12), bg='#353535', fg='white', width=30)
        self.label_email.delete(0, tk.END)
        self.label_email.insert(0, decryptedE)
        self.label_pass = tk.Entry(self.window, text=decryptedP, font=('Courier', 12), bg='#353535', fg='white', width=15)
        self.label_pass.delete(0, tk.END)
        self.label_pass.insert(0, decryptedP)
        self.deleteButton = tk.Button(self.window, text='X', fg='red', command=self.delete)

    # Table layout
    def display(self):
        self.label_site.grid(row=8 + self.i, column=0, padx=10, sticky=tk.W)
        self.label_name.grid(row=8 + self.i, column=1,padx=10, sticky=tk.W)
        self.label_email.grid(row=8 + self.i, column=2, padx=10)
        self.label_pass.grid(row=8 + self.i, column=3, padx=10, sticky=tk.E)
        self.deleteButton.grid(row=8 + self.i, column=4, padx=10, sticky=tk.E)

    # Delete the line requested by the user from the file
    def delete(self):
        answer = tkinter.messagebox.askquestion('Supprimer', 'Etes_vous sûr de vouloir supprimer se login ?')

        if answer == 'yes':
            for i in objects:
                i.destroy()

            f = open(folder, 'r')
            lines = f.readlines()
            f.close()

            login_select = self.site + ',' + self.name + ',' + self.email + ',' + self.password + ',' + '\n'
            lines.pop(lines.index(login_select))

            f = open(folder, "w")
            count = 0

            for line in lines:
                f.write(line)
                count += 1

            f.close()
            read_file()

    # Table efface the line requested by the user
    def destroy(self):
        self.label_site.destroy()
        self.label_name.destroy()
        self.label_email.destroy()
        self.label_pass.destroy()
        self.deleteButton.destroy()


# ******* Functions *********

# Generates a password and displays it in the password_entry
def generate_password():
    punctuation = """!#-/@_?'=%$"""
    all_chars = string.ascii_letters + string.digits + punctuation
    password = "".join(choice(all_chars) for x in range(randint(8, 12)))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


# Send login information as a list to entity_add
def on_submit():
    s = site_entry.get()
    m = email_entry.get()
    p = password_entry.get()
    n = name_entry.get()
    e = entity_add(frame, s, n, p, m)
    e.write()
    site_entry.delete(0, 'end')
    name_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    password_entry.delete(0, 'end')
    messagebox.showinfo('Enregistrement login', 'Login ajouter avec succès \n' + 'Site : ' + s + '\nPseudo : ' + n + '\nEmail : ' + m + '\nMot de passe : ' + p)
    read_file()
    site_entry.insert(0, 'aucun')
    name_entry.insert(0, 'aucun')
    email_entry.insert(0, 'aucun')
    generate_password()


# Clean the file
def clear_file():
    f = open(folder, "w")
    f.close()


# Read the encrypted file and send to entity_display
def read_file():
    f = open(folder, 'r')
    count = 0

    for line in f:
        entityList = line.split(',')
        e = entity_display(frame, entityList[0], entityList[1], entityList[2], entityList[3], count)
        objects.append(e)
        e.display()
        count += 1
    f.close()


# ******* APPLICATION LAYOUT *********

# Show login window
m = connect_window(window)

# Create scrollbar to axe y and axe x
scrollbar = tk.Canvas(window, bg='#353535', width=2, height=300, bd=0, highlightthickness=0, scrollregion=(0, 0, 0, 1500))
vbar = tk.Scrollbar(window, orient="v",command=scrollbar.yview)
vbar.pack(side=tk.RIGHT, fill=tk.Y)
scrollbar.configure(yscrollcommand=vbar.set)
scrollbar.pack(side=tk.TOP)

# Create frame principal
frame = tk.Frame(bg='#353535')

# Create logo in the frame
image = tk.PhotoImage(file='assets/folder.png')
canvas_1 = tk.Canvas(frame, width=230, height=230, bg='#353535', bd=0, highlightthickness=0)
canvas_1.create_image(230/2, 230/2, image=image)
canvas_1.grid(row=0, column=0, columnspan=4, sticky=tk.N)

# Create label for login in the frame
entity_label = tk.Label(frame, text='Rentrer les identifiants ici bas:', font=('Courier', 20), bg='#353535', fg='white', pady=10)
entity_label.grid(column=1, row=1, columnspan=3)
site_label = tk.Label(frame, text='Site :', font=('Courier', 14), bg='#353535', fg='white', pady=5)
site_label.grid(column=2, row=2, columnspan=1, padx=3, sticky=tk.W)
name_label = tk.Label(frame, text='Pseudo :', font=('Courier', 14), bg='#353535', fg='white', pady=5)
name_label.grid(row=3, column=0, columnspan=3)
email_label = tk.Label(frame, text='       Email :', font=('Courier', 16), bg='#353535', fg='white', pady=5)
email_label.grid(row=4, column=1, columnspan=3, padx=3, sticky=tk.W)
pass_label = tk.Label(frame, text='Mot de passe :', font=('Courier', 14), bg='#353535', fg='white', pady=5)
pass_label.grid(row=5, column=0, columnspan=3, padx=3)

# Create input for login in the frame
site_entry = tk.Entry(frame, font=('Courier', 14), bg='#353535', fg='white', width=15)
site_entry.grid(row=2, column=2, padx=2, columnspan=1, pady=2)
site_entry.insert(0, 'aucun')
name_entry = tk.Entry(frame, font=('Courier', 14), bg='#353535', fg='white', width=17)
name_entry.grid(row=3, column=2, columnspan=1, padx=2, pady=2)
name_entry.insert(0, 'aucun')
email_entry = tk.Entry(frame, font=('Courier', 14), bg='#353535', fg='white', width=30)
email_entry.grid(row=4, column=2, columnspan=1, padx=2, pady=2)
email_entry.insert(0, 'aucun')
password_entry = tk.Entry(frame, font=('Courier', 14), bg='#353535', fg='white', width=15)
password_entry.grid(row=5, column=1, columnspan=4, padx=2, pady=2)

# Create button in the frame
submit = tk.Button(frame, text='Enregistrer', command=on_submit,font=('Courier', 14), bg='#353535', fg='white')
submit.grid(column=1, row=6, columnspan=1,pady=10)
generate_pass_button = tk.Button(frame, text='Générer mot de passe', command=generate_password, font=('Courier', 14), bg='#353535', fg='white')
generate_pass_button.grid(row=6, column=2, columnspan=2)

# Create label for login list in the frame
site_label2 = tk.Label(frame, text='Site : ', font=('Courier', 14), bg='#353535', fg='white', pady=10)
site_label2.grid(row=7, column=0)
name_label2 = tk.Label(frame, text='Pseudo : ', font=('Courier', 14), bg='#353535', fg='white')
name_label2.grid(row=7, column=1)
email_label2 = tk.Label(frame, text='Email : ', font=('Courier', 14), bg='#353535', fg='white')
email_label2.grid(row=7, column=2)
pass_label2 = tk.Label(frame, text='MDP : ', font=('Courier', 14), bg='#353535', fg='white')
pass_label2.grid(row=7, column=3)

# Put the frame in the scrollbar canvas
scrollbar.create_window(0, 0, anchor=tk.N, window=frame)

# Generates a password when opening the application
generate_password()

# Read the file when opening the application to be able to display it
read_file()

# Show main window
window.mainloop()
