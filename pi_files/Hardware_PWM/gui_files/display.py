from tkinter import *
from ..model_files.keypad import Keypad
from ..model_files.rotator import Rotator
from time import sleep

root = Tk()
root.title("Access Pad")
root.configure(bg="darkgrey")
root.attributes("-fullscreen",True)

operator = ""               # used when working with display on pin pad
correct_passkey = False     # used when updating pin to make sure old pin was entered first

text = StringVar() # a special object to store and manage string values that can be associated with tkinter widgets

def click(num):
    global operator
    operator = operator + str(num)
    text.set(operator)

def clear():
    global operator
    operator = ""
    text.set(operator)

def lock():
    global operator
    kp = Keypad()
    if text.get() == kp.pin:
        rt = Rotator(0)
        rt.rotate()
        sleep(1)
        text.set("DOOR IS LOCKED")
    else:
        text.set("INVALID")
    operator = ""

def unlock():
    global operator
    kp = Keypad()
    if text.get() == kp.pin:
        rt = Rotator(90)
        rt.rotate()
        sleep(1)
        text.set("DOOR IS UNLOCKED")
    else:
        text.set("INVALID")
    operator = ""
    
def update():
    global operator
    global correct_passkey
    kp = Keypad()
    if text.get() == kp.pin:
        text.set("Enter New Pin, then click CHANGE to save new pin:")
        correct_passkey = True
    else:
        text.set("INVALID, Pin Update FAIL")
    operator = ""

def is_clicked():
    global correct_passkey
    global operator
    if correct_passkey:
        kp = Keypad()
        new_passkey = text.get()
        kp.change_passkey(new_passkey)
        correct_passkey = False
        text.set("Pin Updated Successfully")
    operator = ""

display = Entry(root,bd=15,font=("times new roman",30,"bold"),bg="black",fg="white",justify="center",textvariable=text).grid(columnspan=3, sticky="nsew")

btn1 = Button(root,command=lambda:click(1),padx=30,pady=30,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="1").grid(row=1,column=0, sticky="nsew")
btn2 = Button(root,command=lambda:click(2),padx=30,pady=30,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="2").grid(row=1,column=1, sticky="nsew")
btn3 = Button(root,command=lambda:click(3),padx=30,pady=30,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="3").grid(row=1,column=2, sticky="nsew")
btn4 = Button(root,command=lambda:click(4),padx=30,pady=30,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="4").grid(row=2,column=0, sticky="nsew")
btn5 = Button(root,command=lambda:click(5),padx=30,pady=30,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="5").grid(row=2,column=1, sticky="nsew")
btn6 = Button(root,command=lambda:click(6),padx=30,pady=30,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="6").grid(row=2,column=2, sticky="nsew")
btn7 = Button(root,command=lambda:click(7),padx=30,pady=30,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="7").grid(row=3,column=0, sticky="nsew")
btn8 = Button(root,command=lambda:click(8),padx=30,pady=30,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="8").grid(row=3,column=1, sticky="nsew")
btn9 = Button(root,command=lambda:click(9),padx=30,pady=30,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="9").grid(row=3,column=2, sticky="nsew")
btn0 = Button(root,command=lambda:click(0),padx=30,pady=30,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="0").grid(row=4,column=1, sticky="nsew")

lockbtn =Button(root,command=lambda:lock(),padx=0,pady=0,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="LOCK").grid(row=4,column=2, sticky="nsew")
unlockbtn =Button(root,command=lambda:unlock(),padx=0,pady=0,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="UNLOCK").grid(row=5,column=2, sticky="nsew")

clearbtn =Button(root,command=lambda:clear(),padx=0,pady=0,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="CLEAR").grid(row=5, column=1, sticky="nsew")

updatebtn = Button(root,command=lambda:update(),padx=0,pady=0,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="UPDATE").grid(row=4, column=0, sticky="nsew")
changebtn = Button(root,command=lambda:is_clicked(),padx=0,pady=0,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="CHANGE").grid(row=5, column=0, sticky="nsew")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)

root.mainloop()
