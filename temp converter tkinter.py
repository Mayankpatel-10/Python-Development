import tkinter as tk

def celsius_to_fahrenheit():
    try:
        celsius = float(celsius_entry.get())
        fahrenheit = (celsius * 9/5) + 32
        result_label.config(text=f"{celsius:.2f}°C = {fahrenheit:.2f}°F")
    except ValueError:
        result_label.config(text="Invalid input")

def fahrenheit_to_celsius():
    try:
        fahrenheit = float(fahrenheit_entry.get())
        celsius = (fahrenheit - 32) * 5/9
        result_label.config(text=f"{fahrenheit:.2f}°F = {celsius:.2f}°C")
    except ValueError:
        result_label.config(text="Invalid input")

parent = tk.Tk()
parent.title("Temperature Converter")

# Celsius to Fahrenheit
celsius_label = tk.Label(parent, text="Input Celsius:")
celsius_label.grid(row=0, column=0)
celsius_entry = tk.Entry(parent)
celsius_entry.grid(row=0, column=1)
c_to_f_button = tk.Button(parent, text="Convert to Fahrenheit", command=celsius_to_fahrenheit)
c_to_f_button.grid(row=0, column=2)

# Fahrenheit to Celsius
fahrenheit_label = tk.Label(parent, text="Input Fahrenheit:")
fahrenheit_label.grid(row=1, column=0)
fahrenheit_entry = tk.Entry(parent)
fahrenheit_entry.grid(row=1, column=1)
f_to_c_button = tk.Button(parent, text="Convert to Celsius", command=fahrenheit_to_celsius)
f_to_c_button.grid(row=1, column=2)

result_label = tk.Label(parent, text="", font=("Helvetica", 14))
result_label.grid(row=2, columnspan=3)

parent.mainloop()
