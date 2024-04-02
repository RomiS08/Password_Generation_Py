import tkinter as tk
from tkinter import ttk, messagebox  # Importing messagebox separately for Python versions where it's required
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
        self.mode = tk.StringVar(value="Generative")

        # GUI elements for mode selection
        self.mode_label = ttk.Label(master, text="Select Mode:")
        self.mode_combo = ttk.Combobox(master, values=["Generative", "Customized"], textvariable=self.mode,
                                        state="readonly")
        self.mode_combo.bind("<<ComboboxSelected>>", self.show_mode_frame)

        self.mode_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.mode_combo.grid(row=0, column=1, sticky="w", padx=10, pady=5)

        # Initialize mode-specific frames
        self.generative_frame = GenerativePasswordFrame(master)
        self.customized_frame = CustomizedPasswordFrame(master)

    def show_mode_frame(self, event=None):
        # Function to switch between generative and customized password frames based on user selection
        mode = self.mode.get()
        if mode == "Generative":
            self.generative_frame.show()
            self.customized_frame.hide()
        elif mode == "Customized":
            self.customized_frame.show()
            self.generative_frame.hide()


class GenerativePasswordFrame:
    def __init__(self, master):
        self.master = master

        # Variables to track user preferences
        self.include_lowercase = tk.BooleanVar()
        self.include_uppercase = tk.BooleanVar()
        self.include_digits = tk.BooleanVar()
        self.include_symbols = tk.BooleanVar()
        self.password_length = tk.StringVar(value="8")
        self.generated_password = tk.StringVar()

        # GUI elements for generative password
        self.check_lowercase = ttk.Checkbutton(master, text="Lowercase Letters", variable=self.include_lowercase)
        self.check_uppercase = ttk.Checkbutton(master, text="Uppercase Letters", variable=self.include_uppercase)
        self.check_digits = ttk.Checkbutton(master, text="Digits", variable=self.include_digits)
        self.check_symbols = ttk.Checkbutton(master, text="Symbols", variable=self.include_symbols)

        self.length_label = ttk.Label(master, text="Password Length:")
        self.length_combo = ttk.Combobox(master, values=["8", "12", "14", "16"], textvariable=self.password_length)

        self.generate_button = ttk.Button(master, text="Generate Password", command=self.generate_password)
        self.copy_button = ttk.Button(master, text="Copy Password", command=self.copy_password)
        self.generated_password_label = ttk.Label(master, textvariable=self.generated_password, wraplength=300)
        self.progress_bar = ttk.Progressbar(master, mode='indeterminate')

        self.show()

    def show(self):
        # Function to display GUI elements for generative password generation
        self.check_lowercase.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.check_uppercase.grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.check_digits.grid(row=3, column=0, sticky="w", padx=10, pady=5)
        self.check_symbols.grid(row=4, column=0, sticky="w", padx=10, pady=5)

        self.length_label.grid(row=5, column=0, sticky="w", padx=10, pady=5)
        self.length_combo.grid(row=5, column=1, sticky="w", padx=10, pady=5)

        self.generate_button.grid(row=6, column=0, columnspan=2, pady=10)  # Center-align button
        self.generated_password_label.grid(row=7, column=0, columnspan=2, padx=10, pady=5)
        self.copy_button.grid(row=8, column=0, columnspan=2, pady=5)  # Center-align button
        self.progress_bar.grid(row=9, column=0, columnspan=2, pady=5)  # Center-align progress bar

    def hide(self):
        # Function to hide GUI elements for generative password generation
        self.check_lowercase.grid_forget()
        self.check_uppercase.grid_forget()
        self.check_digits.grid_forget()
        self.check_symbols.grid_forget()
        self.length_label.grid_forget()
        self.length_combo.grid_forget()
        self.generate_button.grid_forget()
        self.generated_password_label.grid_forget()
        self.copy_button.grid_forget()
        self.progress_bar.grid_forget()

    def generate_password(self):
        # Function to generate password based on user preferences
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
        # Function to copy generated password to clipboard and show a message
        self.master.clipboard_clear()
        self.master.clipboard_append(self.generated_password.get())
        self.master.update()
        messagebox.showinfo("Password Copied", "Password copied to clipboard.")


class CustomizedPasswordFrame:
    def __init__(self, master):
        self.master = master

        # Variables to store user preferences for customized password generation
        self.name_string = tk.StringVar()
        self.favorite_numbers = tk.StringVar()
        self.favorite_colors = tk.StringVar()
        self.symbols = tk.StringVar()

        # GUI elements for customized password
        self.name_label = ttk.Label(master, text="Names as Strings:")
        self.name_entry = ttk.Entry(master, textvariable=self.name_string)

        self.numbers_label = ttk.Label(master, text="Fav Numbers as Numbers:")
        self.numbers_entry = ttk.Entry(master, textvariable=self.favorite_numbers)

        self.colors_label = ttk.Label(master, text="Fav Colors as Strings:")
        self.colors_entry = ttk.Entry(master, textvariable=self.favorite_colors)

        self.symbols_label = ttk.Label(master, text="Symbols as Symbols:")
        self.symbols_entry = ttk.Entry(master, textvariable=self.symbols)

        self.generate_button = ttk.Button(master, text="Generate Password", command=self.generate_password)
        self.copy_button = ttk.Button(master, text="Copy Password", command=self.copy_password)
        self.generated_password = tk.StringVar()
        self.password_label = ttk.Label(master, textvariable=self.generated_password, wraplength=300)

    def show(self):
        # Function to display GUI elements for customized password generation
        self.name_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)

        self.numbers_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.numbers_entry.grid(row=2, column=1, padx=10, pady=5)

        self.colors_label.grid(row=3, column=0, sticky="w", padx=10, pady=5)
        self.colors_entry.grid(row=3, column=1, padx=10, pady=5)

        self.symbols_label.grid(row=4, column=0, sticky="w", padx=10, pady=5)
        self.symbols_entry.grid(row=4, column=1, padx=10, pady=5)

        self.generate_button.grid(row=5, column=0, columnspan=2, pady=10)  # Center-align button
        self.password_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)
        self.copy_button.grid(row=7, column=0, columnspan=2, pady=5)  # Center-align button

    def hide(self):
        # Function to hide GUI elements for customized password generation
        self.name_label.grid_forget()
        self.name_entry.grid_forget()
        self.numbers_label.grid_forget()
        self.numbers_entry.grid_forget()
        self.colors_label.grid_forget()
        self.colors_entry.grid_forget()
        self.symbols_label.grid_forget()
        self.symbols_entry.grid_forget()
        self.generate_button.grid_forget()
        self.password_label.grid_forget()
        self.copy_button.grid_forget()

    def generate_password(self):
        # Function to generate customized password based on user preferences
        name = self.name_string.get()
        numbers = self.favorite_numbers.get()
        colors = self.favorite_colors.get()
        symbols = self.symbols.get()

        user_inputs = [name, numbers, colors, symbols]
        if not any(user_inputs):
            self.generated_password.set("Please enter at least one preference.")
            return

        combined_preferences = ''.join(user_inputs)
        generated_password = ''.join(secrets.choice(combined_preferences) for _ in range(12))
        self.generated_password.set(generated_password)

    def copy_password(self):
        # Function to copy generated password to clipboard and show a message
        self.master.clipboard_clear()
        self.master.clipboard_append(self.generated_password.get())
        self.master.update()
        messagebox.showinfo("Password Copied", "Password copied to clipboard.")


def main():
    root = tk.Tk()
    root.iconbitmap('icon1.ico')  # Set the icon for the Tkinter window
    app = PasswordGeneratorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
