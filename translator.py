import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, END, WORD
from googletrans import LANGUAGES, Translator


def translate_text():
    translator = Translator()
    translated = translator.translate(
        text=input_text_entry.get("1.0", END), dest=target_lang_entry.get()
    )
    output_text.delete("1.0", END)
    output_text.insert("1.0", translated.text)


# Set up the main application window
root = tk.Tk()
root.geometry("1100x320")
root.resizable(0, 0)
root.title("Language Translator")
root.configure(bg="cadetblue3")
p1 = tk.PhotoImage(file = 'logo.png') 
root.iconphoto(False, p1) 

# Create and place widgets
tk.Label(
    root, text="Translator Tool", font="Georgia 20 bold", bg="cadetblue4"
).place(relx=0.35,y=10)

tk.Label(root, text="Enter text:", bg="white smoke", font="bold").place(x=30, y=100)
input_text_entry = tk.Text(root, height=5, width=50, wrap=WORD, padx=5, pady=5)
input_text_entry.place(x=30, y=130)

tk.Label(root, text="Target language:", bg="white smoke").place(x=50, y=230)
language_options = list(LANGUAGES.values())
target_lang_entry = ttk.Combobox(root, values=language_options, width=22)
target_lang_entry.place(x=150, y=230)

tk.Button(
    root,
    text="Translate",
    command=translate_text,
    bg="DarkGoldenrod1",
    pady=5,
    activebackground="green3",
).place(x=490, y=150)

tk.Label(root, text="Translated text:", bg="white smoke", font="bold").place(x=600, y=100)
output_text = tk.Text(root, height=5, width=50, wrap=WORD, padx=5, pady=5)
output_text.place(x=600, y=130)

# Run the application
root.mainloop()
