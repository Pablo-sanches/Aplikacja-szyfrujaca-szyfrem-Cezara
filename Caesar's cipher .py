import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Caesar's cipher")
window.geometry("320x640")
window.resizable(False, False)

ALPHABET = (
    "0123456789"
    "abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "!@#$%^&*()<>?|\\\"':;"
)

# index maps
char_to_index = {c: i for i, c in enumerate(ALPHABET)}
index_to_char = {i: c for i, c in enumerate(ALPHABET)}

text = ""
encryption_shift_factor = 3

def get_entry(entry):
    global text
    text = entry.get()

def on_focus_in(event, entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, tk.END)
        entry.config(fg="black")

def on_focus_out(event, entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.config(fg="gray")
    else:
        entry.config(fg="black")

def encrypt_decrypt(mode):
    shift = int(shift_factor_entry.get())
    result = ""
    n = len(ALPHABET)

    if mode == 1:
        for char in text:
            if char in char_to_index:
                i = char_to_index[char]
                i = (i + shift) % n
                result += index_to_char[i]
            else:
                result += char

        output_label.config(text=result)

    elif mode == 2:
        for char in text:
            if char in char_to_index:
                i = char_to_index[char]
                i = (i - shift) % n
                result += index_to_char[i]
            else:
                result += char

        output_label2.config(text=result)

background_image = Image.open("Background.png")
background = ImageTk.PhotoImage(background_image)
tk.Label(window, image=background).place(x=-2, y=-2)

title = tk.Label(window, text="Caesar's cipher", bg="white", font=("Arial", 24))
title.place(x=30, y=23)

encrypted_label = tk.Label(window, text="Encrypted text", bg="white", font=("Arial", 12, "bold"))
encrypted_label.place(x=102, y=98)

decrypted_label = tk.Label(window, text="Decrypted text", bg="white", font=("Arial", 12, "bold"))
decrypted_label.place(x=98, y=379)

output_label = tk.Label(window, text="", bg="white", wraplength=289, justify="left", font=("Arial", 10))
output_label.place(x=13, y=128)

output_label2 = tk.Label(window, text="", bg="white", wraplength=289, justify="left", font=("Arial", 10))
output_label2.place(x=13, y=409)

encrypt_entry = tk.Entry(window, fg="gray", font=("Arial", 16))
encrypt_entry.place(x=38, y=229, width=252, height=38)
encrypt_entry.insert(0, "Enter text to encrypt")

decrypt_entry = tk.Entry(window, fg="gray", font=("Arial", 16))
decrypt_entry.place(x=39, y=510, width=252, height=38)
decrypt_entry.insert(0, "Enter text to decrypt")

shift_factor_entry = tk.Entry(window, borderwidth=2, relief="solid", font=("Arial", 16))
shift_factor_entry.place(x=265, y=10, width=36, height=30)
shift_factor_entry.insert(0, "3")

encrypt_button = tk.Button(window, text="Encrypt", borderwidth=5, relief="solid", font=("Arial", 14), command=lambda: (get_entry(encrypt_entry), encrypt_decrypt(1)))
encrypt_button.place(x=114, y=291)

decrypt_button = tk.Button(window, text="Decrypt", borderwidth=5, relief="solid", font=("Arial", 14), command=lambda: (get_entry(decrypt_entry), encrypt_decrypt(2)))
decrypt_button.place(x=114, y=572)

enter_button = tk.Button(window, text="⏎", borderwidth=2, relief="solid", font=("Arial", 14), command=lambda: get_entry(shift_factor_entry))
enter_button.place(x=265, y=40)

encrypt_entry.bind("<FocusIn>", lambda e: on_focus_in(e, encrypt_entry, "Enter text to encrypt"))
encrypt_entry.bind("<FocusOut>", lambda e: on_focus_out(e, encrypt_entry, "Enter text to encrypt"))

decrypt_entry.bind("<FocusIn>", lambda e: on_focus_in(e, decrypt_entry, "Enter text to decrypt"))
decrypt_entry.bind("<FocusOut>", lambda e: on_focus_out(e, decrypt_entry, "Enter text to decrypt"))

window.mainloop()