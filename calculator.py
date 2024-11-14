import tkinter as tk
from tkinter import messagebox

# Function to perform the calculation
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()
        
        # Perform the calculation
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = num1 / num2
        else:
            raise ValueError("Invalid operation")
        
        # Display the result
        result_var.set(f"Result: {result}")
        
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")
    except ZeroDivisionError as e:
        messagebox.showerror("Error", str(e))

# Initialize the main window
root = tk.Tk()
root.title("Simple Calculator")

# Input fields for numbers
tk.Label(root, text="Enter first number:").grid(row=0, column=0, padx=10, pady=10)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter second number:").grid(row=1, column=0, padx=10, pady=10)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

# Operation selection
tk.Label(root, text="Choose operation:").grid(row=2, column=0, padx=10, pady=10)
operation_var = tk.StringVar(root)
operation_var.set("+")  # default operation
operation_menu = tk.OptionMenu(root, operation_var, "+", "-", "*", "/")
operation_menu.grid(row=2, column=1, padx=10, pady=10)

# Button to calculate the result
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, pady=20)

# Label to display the result
result_var = tk.StringVar(root)
result_label = tk.Label(root, textvariable=result_var, font=("Helvetica", 14))
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
