import string
import random
from tkinter import*
def password_generate():
    n=int(e1.get())
    a=" "
    p=[*string.digits]+[*string.ascii_letters]
    while True:
        a+=random.choice(p)
        if len(a)==n+1:
            break
    return e2.insert(0,a)
def clear_values():
    e1.delete(0,END)
    e2.delete(0,END)
top=Tk()
top.title("password create")
top.configure(background="powder blue") 
length=Label(top,text=" length ",height=1,width=8)
length.grid(row=0,column=0)
e1=Entry(top)
e1.grid(row=0,column=1)

password=Label(top,text="password",height=1,width=8)
password.grid(row=2,column=0)
e2=Entry(top)
e2.grid(row=2,column=1)

generate=Button(top,text="generate",command=lambda:password_generate(),height=1,width=8)
generate.grid(row=3,column=1)
clear=Button(top,text="clear",command=lambda:clear_values(),height=1,width=8)
clear.grid(row=4,column=1)

mainloop()