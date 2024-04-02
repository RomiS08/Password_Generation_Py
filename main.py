import tkinter as tk
from tkinter import ttk
import secrets
import string


class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")

        # Centering the window
        window_width = 400
        window_height = 300
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x = (screen_width / 2) - (window_width / 2)
        y = (screen_height / 2) - (window_height / 2)
        master.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

        # Define variables
        self.include_lowercase = tk.BooleanVar()
        self.include_uppercase = tk.BooleanVar()
        self.include_digits = tk.BooleanVar()
        self.include_symbols = tk.BooleanVar()

        self.password_length = tk.StringVar(value="8")
        self.generated_password = tk.StringVar()

        # GUI elements
        self.check_lowercase = ttk.Checkbutton(master, text="Lowercase Letters", variable=self.include_lowercase)
        self.check_uppercase = ttk.Checkbutton(master, text="Uppercase Letters", variable=self.include_uppercase)
        self.check_digits = ttk.Checkbutton(master, text="Digits", variable=self.include_digits)
        self.check_symbols = ttk.Checkbutton(master, text="Symbols", variable=self.include_symbols)

        self.length_label = ttk.Label(master, text="Password Length:")
        self.length_combo = ttk.Combobox(master, values=["8", "12", "14", "16"], textvariable=self.password_length)

        self.generate_button = ttk.Button(master, text="Generate Password", command=self.generate_password)
        self.copy_button = ttk.Button(master, text="Copy Password", command=self.copy_password)
        self.progress_bar = ttk.Progressbar(master, mode='indeterminate')
        self.password_label = ttk.Label(master, textvariable=self.generated_password, wraplength=300)

        # GUI layout
        self.check_lowercase.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.check_uppercase.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.check_digits.grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.check_symbols.grid(row=3, column=0, sticky="w", padx=10, pady=5)

        self.length_label.grid(row=4, column=0, sticky="w", padx=10, pady=5)
        self.length_combo.grid(row=4, column=1, sticky="w", padx=10, pady=5)

        self.generate_button.grid(row=5, column=0, columnspan=2, pady=10)
        self.progress_bar.grid(row=6, column=0, columnspan=2, pady=10)
        self.password_label.grid(row=7, column=0, columnspan=2, padx=10, pady=5)
        self.copy_button.grid(row=8, column=0, columnspan=2, pady=5)

    def generate_password(self):
        if not any([self.include_lowercase.get(), self.include_uppercase.get(), self.include_digits.get(),
                    self.include_symbols.get()]):
            self.generated_password.set("Please select at least 1 option.")
            return

        self.progress_bar.start()

        character_sets = []
        if self.include_lowercase.get():
            character_sets.append(string.ascii_lowercase)
        if self.include_uppercase.get():
            character_sets.append(string.ascii_uppercase)
        if self.include_digits.get():
            character_sets.append(string.digits)
        if self.include_symbols.get():
            character_sets.append(string.punctuation)

        password_length = int(self.password_length.get())
        if password_length < 8:
            self.generated_password.set("Password length must be at least 8 characters.")
            self.progress_bar.stop()
            return

        generated_password = ''.join(secrets.choice(char_set) for char_set in character_sets)
        while len(generated_password) < password_length:
            generated_password += secrets.choice(secrets.choice(character_sets))
        self.progress_bar.stop()
        self.generated_password.set(generated_password)

    def copy_password(self):
        self.master.clipboard_clear()
        self.master.clipboard_append(self.generated_password.get())
        self.master.update()


def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
