import random
import string
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pyperclip

# main UI
root = Tk()
root.title('Random Password Generator')
root.geometry("540x640+250+180")
root.configure(bg="#E8E4E3")

label = Label(root, text='Random Password Generator', bg="#E8E4E3", font=("Arial", 16 , 'bold'))
label.place(x=160, y=100)

note_text = tk.Text(root , wrap = 'word' , height = 1.5, width = 47)
note_text.place(x = 70 , y = 400)
note_text.insert(tk.END , 'The password generator can generate passwords of up to 8 characters in length.')
# Check boxes
check_box1_var = tk.IntVar()
check_box1 = tk.Checkbutton(root, text='A-Z', variable = check_box1_var, onvalue=1, offvalue=0)
check_box1.place(x = 50 , y = 150)

check_box2_var = tk.IntVar()
check_box2 = tk.Checkbutton(root, text='a-z', variable = check_box2_var, onvalue=1, offvalue=0)
check_box2.place(x = 50 , y = 200)

check_box3_var = tk.IntVar()
check_box3 = tk.Checkbutton(root , text = '0-9' ,variable = check_box3_var, onvalue = 1 , offvalue = 0 )
check_box3.place(x = 50 , y = 250)

check_box4_var = tk.IntVar()
check_box4 = tk.Checkbutton(root , text = '!@#$%^' , variable = check_box4_var , onvalue = 1 , offvalue = 0)
check_box4.place(x = 50 , y = 300)

# Output text Widget
output_text = Text(root , width = 45 , height = 1.5)
output_text.place(x = 150 , y = 175)

# Password Strength text widget
password_textfield = Text(root , font = ('Arial' , 8,'bold') , width = 25 , height = 0.5 , bg = '#E8E4E3')
password_textfield.place(x = 350 , y = 145)

Password = ''

def main():
    
    get_password_length() 
    clipboard()
    strength()

def password_generator():
    global Password
    Password = ''
    
    # Calculate the total length of the password based on the number of checkboxes checked
    total_length = sum([check_box1_var.get(), check_box2_var.get(), check_box3_var.get(), check_box4_var.get()])

    # Ensure the total length of the password is at least 8 characters
    if all([check_box1_var.get() == 0 and check_box2_var.get() == 0 and check_box3_var.get() == 0 and check_box4_var.get() == 0]):
        messagebox.showinfo('Error' , 'All checkboxes are Empty')
        return

    # Calculate the length of each part of the password
    part_length = 8 // total_length

    if check_box1_var.get() == 1:  # If checkbox for uppercase letters is checked
        Password += ''.join(random.choices(string.ascii_uppercase, k=part_length))
    if check_box2_var.get() == 1:  # If checkbox for lowercase letters is checked
        Password += ''.join(random.choices(string.ascii_lowercase, k=part_length))
    if check_box3_var.get() == 1:  # If checkbox for numerals in checked
        Password += ''.join(random.choices(string.digits, k=part_length))
    if check_box4_var.get() == 1:  # If checkbox for punctuations is checked
        Password += ''.join(random.choices(string.punctuation, k=part_length))

    # Fill up any remaining characters to ensure the password length is 8
    if len(Password) < 8:
        available_length = 8 - len(Password)
        available_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        Password += ''.join(random.choices(available_chars, k=available_length))

        Password_list = list(Password)
        random.shuffle(Password_list)
        Password = ''.join(Password_list)
        
    # Update the output text widget with the generated password
    output_text.delete("1.0", END)  # Clear any existing text in the output text widget
    output_text.insert(END, Password)  # Insert the generated password into the output text widget

    # Check password strength
    password_strength = strength(Password)
    password_textfield.delete("1.0", END)  # Clear any existing text in the password strength text field
    password_textfield.insert(END, f"Password Strength: {password_strength}")  # Display password strength in the text field

    return Password

def get_password_length():
    # Calculate the length of the generated password without displaying it
    total_length = sum([check_box1_var.get(), check_box2_var.get(), check_box3_var.get(), check_box4_var.get()])
    part_length = 8 // total_length
    return part_length

def strength(Password):
    has_upper = any(character.isupper() for character in Password)
    has_lower = any(character.islower() for character in Password)
    has_number = any(character.isdigit() for character in Password)
    has_punc = any(character in string.punctuation for character in Password)

    if has_upper and has_lower and has_number and has_punc:
        return 'Strong'
    else:
        return 'Weak'

def exit_win():
    if root.winfo_exists():  # Check if the root window exists
        confirm_msg = messagebox.askyesno('Exit', 'Are you sure to want to exit')
        if confirm_msg:
            root.destroy()
            return True
    else:
        return False  # Return False if the root window doesn't exist


def clipboard():
    copy_to_clipboard = Password
    if copy_to_clipboard:
        pyperclip.copy(copy_to_clipboard)
        messagebox.showinfo('Random Password Generator' , 'Text Copied to Clipboard')
    else:
        messagebox.showerror('Error' , 'Text box is empty')

# Password Generate Button
generate_button = Button(text='GENERATE' , command = password_generator , width = 10 , height = 2 , font = 'arial 14 bold')
generate_button.place(x = 225 , y = 225)

# Window exittong button
exit_button = Button(text = 'Exit' , command = exit_win , width = 7 , height = 1 , font = 'arial 14 bold')
exit_button.place(x = 245 , y = 300)

# Copy to clipboard button
clip_button = Button(text = 'Copy' , command = clipboard , width = 4 , height = 1 , font = 'arial 14 ')
clip_button.place(x = 450 , y = 225)

image_icon = PhotoImage(file="C://Users//wolle//Downloads//images.png")
root.iconphoto(False, image_icon)

root.mainloop()
 