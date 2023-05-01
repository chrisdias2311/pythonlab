import tkinter as tk

# Create the root window
root = tk.Tk()

# Set the title and size of the window
root.title("Canvas Example")
root.geometry("400x400")

# Create a canvas widget
canvas = tk.Canvas(root, width=300, height=300, bg="white")

# Draw a rectangle
canvas.create_rectangle(50, 50, 150, 150, fill="red")

# Draw an oval
canvas.create_oval(100, 100, 200, 200, fill="green")

# Draw a line
canvas.create_line(0, 0, 300, 300, width=3, fill="blue")

# Pack the canvas widget
canvas.pack()

# Start the main loop
root.mainloop()
