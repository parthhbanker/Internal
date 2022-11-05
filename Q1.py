from tkinter import *
from tkinter import messagebox
import random

# initializing root window
root = Tk()
root.geometry("1305x652")
root.config(padx=100, pady=30)

lstVar = list()

isValidate = True

def changeTheme():
    global l
    colors = ('blue', 'white', 'red', 'yellow')
    rand_num = random.randint(0,len(colors)-1)
    # print()
    root.config(bg=colors[rand_num])
    rand_num = random.randint(0,len(colors)-1)
    l.config(bg=colors[rand_num])

def addData():
    global l
    data = dict()
    name = fn_var.get() + " " + ln_var.get()

    data['name'] = name
    if(gender_var.get() == 1):
        data["gender"] = ("MALE")
    elif(gender_var.get() == 2):
        data["gender"] =("FEMALE")
    if eng_var.get()==1:
        data["lang1"] =("English")
    if telu_var.get()==1:
        data["lang2"] =("Telugu")
    if hind_var.get()==1:
        data["lang3"] =("Hindi")
    data["email"] =(email_var.get())
    data["address"] =(add_var.get())
    data["state"] =(state_var.get())
    data["zip code"] =(zip_var.get())
    data["cc type"] =(cc_var.get())

    l.insert(END, data)

def delete():
    global l
    l.delete(l.curselection())

def validateForm():
    global isValidate
    try:
        number = int(zip_var.get())
    except:
        isValidate = False
        messagebox.showerror("Inavalid Zip Code","Only input number in zip code")

    for char in (fn_var.get() + " " + ln_var.get()):
        try:
            c = int(char)
            isValidate =False
            messagebox.showerror("Invalid Name","Name cannot container number")
            break
        except:
            continue

    email = email_var.get()
    if '@' not in email:
        isValidate = False
        messagebox.showerror("Invalid Email","Email should contain @")

    if(isValidate):
        addData()

# declaring all the variables for input
fn_var = StringVar()
ln_var = StringVar()
gender_var = IntVar()
email_var = StringVar()
add_var = StringVar()
state_var = StringVar()
zip_var = StringVar()
cc_var = StringVar()

eng_var = IntVar()
telu_var = IntVar()
hind_var = IntVar()

# initializing each label
fn_label = Label(root, text="First Name").grid(column=0, row=0,pady=5)
ln_label = Label(root, text="Last Name").grid(column=0, row=1,pady=5)
gender_label = Label(root, text="Gender").grid(column=0, row=2,pady=5)
lan_label = Label(root, text="Language").grid(column=0, row=3,pady=5)
email_label = Label(root, text="Email Address").grid(column=0, row=4,pady=5)
add_label = Label(root, text="Addres").grid(column=0, row=5,pady=5)
state_label = Label(root, text="state").grid(column=0, row=6,pady=5)
zip_label = Label(root, text="Zip").grid(column=0, row=7,pady=5)
cc_label = Label(root, text="Credit Card Type").grid(column=0, row=8,pady=5)

# initializing each entry
fn_inp = Entry(root, textvariable=fn_var).grid(column=1, row=0, columnspan=3)
ln_inp = Entry(root, textvariable=ln_var).grid(column=1, row=1, columnspan=3)
email_inp = Entry(root, textvariable=email_var).grid(column=1, row=4, columnspan=3)
add_inp = Text(root, width=18, height=5).grid(column=1, row=5, columnspan=3, pady=10)
zip_inp = Entry(root, textvariable=zip_var).grid(column=1, row=7, columnspan=3)

# gender radio
male_radio = Radiobutton(root, text="Male", value=1, variable=gender_var)
female_radio = Radiobutton(root, text="Female", value=2, variable=gender_var)
male_radio.grid(column=1, row=2)
female_radio.grid(column=2, row=2, columnspan=1)

# language check    
telu_check = Checkbutton(root,text="Telugu", variable=telu_var, onvalue=1, offvalue=0)
eng_check = Checkbutton(root, text="English", variable=eng_var, onvalue=1, offvalue=0)
hind_check = Checkbutton(root, text="Hindi", variable=hind_var, onvalue=1, offvalue=0)

telu_check.grid(column=1, row=3,)
eng_check.grid(column=2, row=3,)
hind_check.grid(column=3, row=3,)

# state select
state_menu = OptionMenu(root , state_var, "Gujarat", "MP", "Delhi", "Rajasthan")
state_menu.grid(column=1, row=6, columnspan=3)

# credit card select
cc_menu = OptionMenu(root, cc_var, "Master", "Maestro", "Visa", "Rupay")
cc_menu.grid(column=1, row=8, columnspan=3)


ins_btn = Button(root, text="Insert", command=validateForm, width=5, height=2, font=("Arial", 12))
ins_btn.grid(row=1, column=5, padx=50, columnspan=4)

del_btn = Button(root, text="Delete", command=delete, width=5, height=2, font=("Arial", 12))
del_btn.grid(row=3, column=5, padx=50, columnspan=4)

theme_btn = Button(root, text="Theme", command=changeTheme, width=5, height=2, font=("Arial", 12))
theme_btn.grid(row=5, column=5, padx=50, columnspan=4)

l = Listbox(root, bg="white", width=50, height=30)
lb = Label(root, text="Billing Records", padx=10 ,pady=10, font=("Arial", 28), bg="yellow").grid(row=0, column=9)
l.grid(row=1, column=9,rowspan=7, padx=20,)

root.mainloop()