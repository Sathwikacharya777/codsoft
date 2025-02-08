import tkinter as tk
from tkinter import messagebox
import random
import string


class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        # Label and Entry for Password Length
        tk.Label(root, text="Enter Password Length:").grid(row=0, column=0, pady=5, padx=5)
        self.length_entry = tk.Entry(root)
        self.length_entry.grid(row=0, column=1, pady=5, padx=5)

        # Checkbox for Complexity
        self.include_upper = tk.BooleanVar()
        self.include_digits = tk.BooleanVar()
        self.include_special = tk.BooleanVar()

        tk.Checkbutton(root, text="Include Uppercase Letters", variable=self.include_upper).grid(row=1, column=0, columnspan=2, sticky="w")
        tk.Checkbutton(root, text="Include Digits", variable=self.include_digits).grid(row=2, column=0, columnspan=2, sticky="w")
        tk.Checkbutton(root, text="Include Special Characters", variable=self.include_special).grid(row=3, column=0, columnspan=2, sticky="w")

        # Generate Password Button
        tk.Button(root, text="Generate Password", command=self.generate_password).grid(row=4, column=0, columnspan=2, pady=10)

        # Label to Display Password
        self.password_label = tk.Label(root, text="Generated Password: ", font=("Arial", 12))
        self.password_label.grid(row=5, column=0, columnspan=2, pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError

            # Define character sets
            char_set = string.ascii_lowercase
            if self.include_upper.get():
                char_set += string.ascii_uppercase
            if self.include_digits.get():
                char_set += string.digits
            if self.include_special.get():
                char_set += string.punctuation

            if not char_set:
                messagebox.showwarning("Error", "Please select at least one character type!")
                return

            # Generate password
            password = ''.join(random.choice(char_set) for _ in range(length))
            self.password_label.config(text=f"Generated Password: {password}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive integer for the password length!")


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
