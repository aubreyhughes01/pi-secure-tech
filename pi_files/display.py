from tkinter import *
from keypad import Keypad
root = Tk()
root.title("Access Pad")
root.configure(bg="darkgrey")
root.attributes("-fullscreen",True)


def Click(num):
    global operator
    operator = operator + str(num)
    text.set(operator)

def Clear():
    global operator
    operator = ""
    text.set(operator)

def Submit():
    global operator
    kp = Keypad()
    if text.get() == str(kp.pin):
        text.set("SUCCESS")
    else:
        text.set("INVALID")
    operator = ""
    
    

operator = ""
text = StringVar()

display = Entry(root,bd=15,font=("times new roman",30,"bold"),bg="black",fg="white",justify="center",textvariable=text).grid(columnspan=3, sticky="nsew")

btn1 = Button(root,command=lambda:Click(1),padx=30,pady=30,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="1").grid(row=1,column=0, sticky="nsew")
btn2 = Button(root,command=lambda:Click(2),padx=30,pady=30,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="2").grid(row=1,column=1, sticky="nsew")
btn3 = Button(root,command=lambda:Click(3),padx=30,pady=30,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="3").grid(row=1,column=2, sticky="nsew")
btn4 = Button(root,command=lambda:Click(4),padx=30,pady=30,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="4").grid(row=2,column=0, sticky="nsew")
btn5 = Button(root,command=lambda:Click(5),padx=30,pady=30,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="5").grid(row=2,column=1, sticky="nsew")
btn6 = Button(root,command=lambda:Click(6),padx=30,pady=30,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="6").grid(row=2,column=2, sticky="nsew")
btn7 = Button(root,command=lambda:Click(7),padx=30,pady=30,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="7").grid(row=3,column=0, sticky="nsew")
btn8 = Button(root,command=lambda:Click(8),padx=30,pady=30,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="8").grid(row=3,column=1, sticky="nsew")
btn9 = Button(root,command=lambda:Click(9),padx=30,pady=30,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="9").grid(row=3,column=2, sticky="nsew")

clearbtn =Button(root,command=lambda:Clear(),padx=0,pady=0,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="CLR").grid(row=4, column=0, sticky="nsew")

submitbtn =Button(root,command=lambda:Submit(),padx=0,pady=0,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="ENT").grid(row=4,column=2, sticky="nsew")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)




root.mainloop()
