from tkinter import *
root = Tk()
root.title("Access Pad")
root.configure(bg="darkgrey")

display = Entry(root,bd=15,font=("times new roman",30,"bold"),bg="black",fg="white",justify="center",textvariable=Text).grid(columnspan=3)

btn1 = Button(root,padx=30,pady=30,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="1").grid(row=1,column=0)
btn2 = Button(root,padx=30,pady=30,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="2").grid(row=1,column=1)
btn3 = Button(root,padx=30,pady=30,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="3").grid(row=1,column=2)
btn4 = Button(root,padx=30,pady=30,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="4").grid(row=2,column=0)
btn5 = Button(root,padx=30,pady=30,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="5").grid(row=2,column=1)
btn6 = Button(root,padx=30,pady=30,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="6").grid(row=2,column=2)
btn7 = Button(root,padx=30,pady=30,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="7").grid(row=3,column=0)
btn8 = Button(root,padx=30,pady=30,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="8").grid(row=3,column=1)
btn9 = Button(root,padx=30,pady=30,bg="black",bd=30,fg="white",font=("times new roman",30,"bold"),text="9").grid(row=3,column=2)

root.mainloop()
