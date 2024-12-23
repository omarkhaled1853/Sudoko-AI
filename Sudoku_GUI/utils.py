import tkinter as tk

def create_styled_button(frame: tk.Frame, text: str, command) -> tk.Button:
    """Function to create styled buttons with hover and select effects"""
    button = tk.Button(
        frame,
        text=text,
        font=("Arial", 14, "bold"),
        cursor="hand2",
        background="#5A7BC0",
        foreground="#FFFFFF",
        activebackground="#3A5B88",
        activeforeground="#E0E0E0",
        bd=0,
        relief="flat",
        command=command,
    )
        
    button.bind("<Enter>", button.config(background="#3A5B88", foreground="#E0E0E0"))
    button.bind("<Leave>", button.config(background="#5A7BC0", foreground="#FFFFFF"))

    return button