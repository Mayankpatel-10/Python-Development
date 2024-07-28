import tkinter as tk

# Function to perform the calculation
def calculate():
    try:
        result = eval(entry.get())
        label_result.config(text="Result: " + str(result))
    except:
        label_result.config(text="Error")

# Create the main window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("260x300")  

# Create an entry widget for user input
entry = tk.Entry(root, width=20)
entry.grid(row=0, column=0, columnspan=4)

# Create a label to display the result (increased height)
label_result = tk.Label(root, text="Result: ", height=3)  # Adjust the height as needed
label_result.grid(row=1, column=0, columnspan=4)

# Create buttons for the calculator (same as before)
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 2
col = 0
button_width = 8
button_height = 3
for button in buttons:
    action = lambda x=button: entry.insert(tk.END, x)
    if button == '=':
        action = calculate
    tk.Button(root, text=button, width=button_width, height=button_height, command=action).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the application
root.mainloop()
