from tkinter import *

def encrypt():
    plaintext = plaintext_entry.get()
    shift = int(shift_entry.get())
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    result_label.configure(text="Encrypted Text: " + encrypted_text)

def decrypt():
    ciphertext = ciphertext_entry.get()
    shift = int(shift_entry.get())
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                decrypted_char = chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                decrypted_char = chr((ord(char) - 97 - shift) % 26 + 97)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    result_label.configure(text="Decrypted Text: " + decrypted_text)

root = Tk()
root.title("Caesar Cipher")
root.geometry("450x300")

# Create labels and entries
plaintext_label = Label(root, text="Plaintext:")
plaintext_label.grid(row=0, column=0, padx=10, pady=10)
plaintext_entry = Entry(root,width=30)
plaintext_entry.grid(row=0, column=1, padx=10, pady=10)

ciphertext_label = Label(root, text="Ciphertext:")
ciphertext_label.grid(row=8, column=0, padx=10, pady=30)
ciphertext_entry = Entry(root,width=30)
ciphertext_entry.grid(row=8, column=1, padx=30, pady=30)

shift_label = Label(root, text="Key:")
shift_label.grid(row=20, column=0, padx=10, pady=10)
shift_entry = Entry(root,width=30)
shift_entry.grid(row=20, column=1, padx=10, pady=10)

result_label = Label(root, text="")
result_label.grid(row=25, column=1, columnspan=2)

encrypt_button = Button(root, text="Encrypt", bg="green" ,fg="white",command=encrypt)
encrypt_button.grid(row=50, column=0,padx=50, pady=50)

decrypt_button = Button(root, text="Decrypt", bg="red" ,fg="white",command=decrypt)
decrypt_button.grid(row=50, column=1)

root.mainloop()
