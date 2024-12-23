import tkinter as tk
from Sudoku_game.Sudoku_GUI.Pages.menu_page import MenuPage
from Sudoku_game.Sudoku_GUI.Pages.Modes.mode_one_page import ModeOnePage
from Sudoku_game.Sudoku_GUI.Pages.Modes.mode_two_page import ModeTwoPage
from Sudoku_game.Sudoku_GUI.Pages.Modes.mode_three_page import ModeThreePage

class App(tk.Tk):
    """Main application controller with root frame."""
    def __init__(self):
        super().__init__()
        self.title("Sudoku Game")
        
        # Allow the window to be resizable
        self.resizable(True, True)

        # Create a container frame for all pages
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        # Initialize menu page 
        self.menu_page = MenuPage(self.container, self)

        # Show the menu page initially
        self.menu_page.show()
    
    def reinitialize_mode_page(self, mode_class):
        """Reinitialize the mode page."""
        # Destroy the existing mode page if it exists
        for widget in self.container.winfo_children():
            widget.destroy()

        # Create a new instance of the mode page
        mode_page = mode_class(self.container, self)
        mode_page.show()
        return mode_page

    def show_menu(self):
        """Show menu page and hide all other pages"""
        for widget in self.container.winfo_children():
            widget.destroy()

        self.menu_page = MenuPage(self.container, self)
        self.menu_page.show()

    def show_mode_one(self):
        """Show mode one page and hide menu page"""
        self.mode_one_page = self.reinitialize_mode_page(ModeOnePage)

    def show_mode_two(self):
        """Show mode two page and hide menu page"""
        self.mode_two_page = self.reinitialize_mode_page(ModeTwoPage)

    def show_mode_three(self):
        """Show mode three page and hide menu page"""
        self.mode_three_page = self.reinitialize_mode_page(ModeThreePage)