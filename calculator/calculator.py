import tkinter as tk
from tkinter import messagebox


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        # Input fields
        tk.Label(root, text="Enter First Number:").grid(row=0, column=0, pady=5, padx=5)
        self.num1_entry = tk.Entry(root)
        self.num1_entry.grid(row=0, column=1, pady=5, padx=5)

        tk.Label(root, text="Enter Second Number:").grid(row=1, column=0, pady=5, padx=5)
        self.num2_entry = tk.Entry(root)
        self.num2_entry.grid(row=1, column=1, pady=5, padx=5)

        # Operation buttons
        tk.Button(root, text="+", command=lambda: self.calculate('+')).grid(row=2, column=0, pady=5, padx=5)
        tk.Button(root, text="-", command=lambda: self.calculate('-')).grid(row=2, column=1, pady=5, padx=5)
        tk.Button(root, text="*", command=lambda: self.calculate('*')).grid(row=3, column=0, pady=5, padx=5)
        tk.Button(root, text="/", command=lambda: self.calculate('/')).grid(row=3, column=1, pady=5, padx=5)

        # Result label
        self.result_label = tk.Label(root, text="Result: ")
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)

    def calculate(self, operation):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            result = None

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    messagebox.showerror("Error", "Division by zero is not allowed!")
                    return
                result = num1 / num2

            self.result_label.config(text=f"Result: {result}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers!")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
