import tkinter as tk

root = tk.Tk()

root.title("Canvas")
root.geometry("400x400")

canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.create_rectangle(50, 50, 200, 200, fill="red")
canvas.create_oval(100, 100, 200, 200, fill="green")
canvas.create_line(0, 0, 300, 300, width=3, fill="blue")

# Pack the canvas widget
canvas.pack()

# Start the main loop
root.mainloop()