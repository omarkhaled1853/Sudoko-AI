import tkinter as tk

class BasePage:
    """Base class for all pages."""
    def __init__(self, parent, controller):
        self.frame = tk.Frame(parent, bg="#FFFFFF")
        self.controller = controller

    def show(self):
        """Display the frame."""
        self.frame.pack(fill="both", expand=True)

    def hide(self):
        """Hide the frame."""
        self.frame.pack_forget()