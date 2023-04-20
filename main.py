from tkinter import *
from tkinter import messagebox
import base64

screen = Tk()

screen.geometry("420x420")
screen.title("Encryption and Decryption")
screen.configure(background="light gray")

#function for encryption
def encrypt():
    password = code.get()
    if password =="1234":
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("300x200")
        screen1.configure(background="light gray")

        #usertext
        message = textbox.get(1.0,END) #first line zero char
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen1,text="Encrypted message",font="arial 10 bold",bg="light gray").place(x=5,y=6)

        textbox2 = Text(screen1,bd=0,font="20",wrap=WORD)
        textbox2.place(x=5, y=30, width=290, height=120)
        textbox2.insert(END,encrypt)

    elif(password==""):
        messagebox.showerror("Error","Please enter the secret key")

    elif(password!="1234"):
        messagebox.showerror("Invalid","Invalid secret key")


#function for decryption
def decrypt():
    password = code.get()
    if password =="1234":
        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("300x200")
        screen2.configure(background="light gray")

        #usertext
        message = textbox.get(1.0,END) #first line zero char
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(encode_message)
        decrypt = base64_bytes.decode("ascii")

        Label(screen2,text="Decrypted message",font="arial 10 bold",bg="light gray").place(x=5,y=6)

        textbox2 = Text(screen2,bd=0,font="20",wrap=WORD)
        textbox2.place(x=5, y=30, width=290, height=120)
        textbox2.insert(END,decrypt)

    elif(password==""):
        messagebox.showerror("Error","Please enter the secret key")

    elif(password!="1234"):
        messagebox.showerror("Invalid","Invalid secret key")


#function for reset button
def reset():
    textbox.delete(1.0,END)
    code.set("")

#Heading
Label(screen,text="Write a message",font="arial 10 bold",bg="light gray").place(x=10,y=6)

#Textbox
textbox = Text(screen,bd=0,font="20")
textbox.place(x=10,y=40,width=400,height=120)

#Key
Label(screen,text="Enter Secret Key",font="arial 10 bold",bg="light gray").place(x=10,y=180)

#keyentry
code=StringVar()
Entry(textvariable=code,bd=0,font="15",show="*").place(x=130,y=180)

#buttons
Button(screen,bd=0,text="ENCRYPT",font="arial 15 bold",bg="green",fg="white",command=encrypt).place(x=40,y=280,width=140)
Button(screen,bd=0,text="DECRYPT",font="arial 15 bold",bg="red",fg="white",command=decrypt).place(x=240,y=280,width=140)
Button(screen,bd=0,text="RESET",font="arial 15 bold",bg="sky blue",fg="white",command=reset).place(x=140,y=350,width=140)

mainloop()