import tkinter as tk

class App(tk.Tk):
    """Main application controller with root frame."""
    def __init__(self):
        super().__init__()
        self.title("Sudoku Game")

        # Set the initial size of the window
        self.geometry("600x500")
        
        # Allow the window to be resizable
        self.resizable(True, True)

        # Center the window on the screen
        self.center_window(600, 500)

        # Create a container frame for all pages
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

    def center_window(self, width, height):
        """Center the application window on the screen."""
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.geometry(f"{width}x{height}+{x}+{y}")