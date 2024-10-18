from tkinter import *
from keypad import Keypad
root = Tk()
root.title("Access Pad")
root.configure(bg="darkgrey")
root.attributes("-fullscreen",True)


operator = ""
text = StringVar()
correct_passkey = False     # used when updating pin to make sure old pin was entered first

def click(num):
    global operator
    operator = operator + str(num)
    text.set(operator)

def clear():
    global operator
    operator = ""
    text.set(operator)

def submit():
    global operator
    kp = Keypad()
    if text.get() == str(kp.pin):
        text.set("SUCCESS")
    else:
        text.set("INVALID")
    operator = ""
    
def update():
    global operator
    global correct_passkey
    kp = Keypad()
    if text.get() == str(kp.pin):
        text.set("Enter New Pin:")
        correct_passkey = True
    else:
        text.set("INVALID, Pin Update FAIL")
    operator = ""

def is_clicked():
    global correct_passkey
    global operator
    if correct_passkey:
        kp = Keypad()
        new_passkey = int(text.get())
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

clearbtn =Button(root,command=lambda:clear(),padx=0,pady=0,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="CLR").grid(row=5, column=0, sticky="nsew")
submitbtn =Button(root,command=lambda:submit(),padx=0,pady=0,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="ENT").grid(row=4,column=0, sticky="nsew")

updatebtn = Button(root,command=lambda:update(),padx=0,pady=0,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="UPD").grid(row=4, column=2, sticky="nsew")
changebtn = Button(root,command=lambda:is_clicked(),padx=0,pady=0,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="CHG").grid(row=5, column=2, sticky="nsew")

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
