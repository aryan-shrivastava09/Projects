from tkinter import *
import string
import random
from tkinter import messagebox
import pyperclip
FONT = ("Arial",10,"normal")
letters = list(string.ascii_letters)
numbers = ['1','2','3','4','5','6','7','8','9','0']
special_chars = ["@","#","%","_","-","/", "!", "$"]

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def splitchar(str1):
    mlist = []
    for char in str1:
        mlist.append(char)
    return mlist

def password_generate():
    nl = random.randint(8,10)
    nn = random.randint(2,4)
    nc = random.randint(2,4)
    p1 = "".join(random.choices(letters, k = nl)) + "".join(random.choices(numbers, k = nn)) + "".join(random.choices(special_chars,k = nc))
    plist = splitchar(p1)
    random.shuffle(plist)
    finalp = "".join(plist)
    passwordEntry.insert(END, finalp)
    pyperclip.copy(finalp)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def addbutton():
    web = websiteEntry.get()
    email = emailEntry.get()
    password = passwordEntry.get()

    if len(web)==0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title= "Field Empty", message="Please don't leave any of the fields empty")

    else:
        is_ok = messagebox.askokcancel(title = web, message= f"Are you sure you want to save the info as it is?\nWebsite: {web}\nEmail/Username : {email}\nPassword: {password}")
        if is_ok:
            fhand = open("./p29PasswordManager/data.txt", mode = "a+")
            fhand.write(f"Website : {web} | email : {email} | password : {password} \n")
            fhand.close()
            websiteEntry.delete(0,END)
            emailEntry.delete(0,END)
            passwordEntry.delete(0,END)
            websiteEntry.focus()
            emailEntry.insert(END,"aryan.shrivastava9@gmail.com")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)

canvas = Canvas(width = 200, height = 200)
image = PhotoImage(file = "./p29PasswordManager/logo.png")
canvas.create_image(100, 100, image = image)
canvas.grid(column = 1, row =0)

#Labels
website = Label(text = "Website: ", font = FONT)
website.grid(column =0, row = 1)

email = Label(text= "Email/Username: ", font = FONT )
email.grid(column = 0, row = 2)

password = Label(text = "Password: ", font = FONT)
password.grid(column = 0, row = 3)

#Entry
websiteEntry = Entry(width = 52)
websiteEntry.grid(column = 1, row = 1, columnspan = 2)
websiteEntry.focus()

emailEntry = Entry(width = 52)
emailEntry.insert(END,"aryan.shrivastava9@gmail.com")
emailEntry.grid(column =1, row = 2, columnspan = 2)

passwordEntry = Entry(width = 34)
passwordEntry.grid(column= 1, row = 3)

#Buttons
gp = Button(text = "Generate Password", highlightthickness = 0, command = password_generate)
gp.grid(column = 2, row = 3, sticky = "W")

add = Button(text = "Add", width = 44, command = addbutton)
add.grid(column = 1, row = 4, columnspan = 2)


window.mainloop()