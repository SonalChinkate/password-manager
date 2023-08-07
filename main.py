
from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
BACKGROUND="#B0DAFF"
FOREGROUND="#164B60"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pass():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters)for _ in range(randint(4, 8))]
    password_sym = [choice(symbols)for _ in range(randint(2, 4))]
    password_num = [choice(numbers)for _ in range(randint(2, 4))]

    password_list=[]
    password_list = password_letters + password_sym + password_num
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0,f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    if len(website)==0 or len(password)== 0 or len(email)==0:
        messagebox.showinfo(title="error",message="Please make sure don\'t leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"This are the details entered:\nEmail: {email}\nPassword: {password}\n"
                            f"\nIs it ok to save?")
        if is_ok:
            with open("data.txt","a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n") 
                website_input.delete(0,END)
                password_input.delete(0,END)
            messagebox.showinfo(title="Message",message="Saved Successfully")


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=20,bg=BACKGROUND)


canvas = Canvas(width=200,height=200)
logo_image = PhotoImage(file="lockpass.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(column=1,row=0)

#Labels
website_label = Label(text="Website",font=("Bookman Old Style",11,'bold'),bg=BACKGROUND,fg=FOREGROUND)
website_label.grid(column=0,row=1)
email_label = Label(text="Email/Username",font=("Bookman Old Style",11,'bold'),bg=BACKGROUND,fg=FOREGROUND)
email_label.grid(column=0,row=2)
password_label = Label(text="Password",font=("Bookman Old Style",11,'bold'),bg=BACKGROUND,fg=FOREGROUND)
password_label.grid(column=0,row=3)

#Input entries
website_input = Entry(width=40)
website_input.grid(column=1,row=1,columnspan=2)
website_input.focus()
email_input = Entry(width=40)
email_input.grid(column=1,row=2,columnspan=2)
email_input.insert(0,"sonalchinkate970@gmail.com")
password_input = Entry(width=30)
password_input.grid(column=1,row=3)

gen_pass_button = Button(text="Generate Password",command=generate_pass)
gen_pass_button.config(background="#749BC2",fg="#F2EAD3")
gen_pass_button.grid(column=2,row=3)

add_button = Button(text="Add",width=36, command=save)
add_button.config(background="#4682A9",fg="#F6F4EB")
add_button.grid(column=1,row=4,columnspan=2)

window.mainloop()