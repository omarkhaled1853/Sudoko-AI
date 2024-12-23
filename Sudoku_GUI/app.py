import tkinter as tk
from Sudoku_GUI.Pages.menu_page import MenuPage
from Sudoku_GUI.Pages.Modes.mode_one_page import ModeOnePage
from Sudoku_GUI.Pages.Modes.mode_two_page import ModeTwoPage
from Sudoku_GUI.Pages.Modes.mode_three_page import ModeThreePage

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

        # Initialize pages and pass the container frame as a parent 
        # and App instance as a controller for that pages  
        self.menu_page = MenuPage(container, self)
        self.mode_one_page = ModeOnePage(container, self)
        self.mode_two_page = ModeTwoPage(container, self)
        self.mode_three_page = ModeThreePage(container, self)

        # Show the menu page initially
        self.menu_page.show()


    def center_window(self, width, height):
        """Center the application window on the screen."""
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.geometry(f"{width}x{height}+{x}+{y}")
    
    def show_menu(self):
        """Show menu page and hide all other pages"""
        self.mode_one_page.hide()
        self.mode_two_page.hide()
        self.mode_three_page.hide()
        self.menu_page.show()
    
    def show_mode_one(self):
        """Show mode one page and hide menu page"""
        self.menu_page.hide()
        self.mode_one_page.show()

    def show_mode_two(self):
        """Show mode two page and hide menu page"""
        self.menu_page.hide()
        self.mode_two_page.show()

    def show_mode_three(self):
        """Show mode three page and hide menu page"""
        self.menu_page.hide()
        self.mode_three_page.show()