import tkinter as tk

class BasePage:
    """Base class for all pages."""
    def __init__(self, parent, controller):
        self.base_page_frame = tk.Frame(parent)
        self.controller = controller

    def show(self):
        """Display the frame."""
        self.base_page_frame.pack(fill="both", expand=True)

    def hide(self):
        """Hide the frame."""
        self.base_page_frame.pack_forget()