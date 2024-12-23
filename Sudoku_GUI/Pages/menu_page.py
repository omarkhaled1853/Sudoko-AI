import tkinter as tk
from Sudoku_GUI.Pages.base_page import BasePage
from Sudoku_GUI.utils import create_styled_button

class MenuPage(BasePage):
    """Class representing the menu page."""
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        # Initialize welcome label
        menu_label = tk.Label(
            self.frame, 
            text="Welcome to Sudoku!", 
            font=("Arial", 24, "bold"), 
            bg="#FFFFFF", 
            fg="#4A90E2"
        )
        menu_label.pack(pady=20)

        # create a mode one button that route to (agent generate sudoku board and agent solve the sudoku)
        mode_one_button = create_styled_button(
                self.frame, 
                "Agent Challenge Mode", 
                self.controller.show_mode_one
            )
        mode_one_button.pack(pady=10)

        # create a mode two button that route to (user generate the sudoku board and agent solve the sudoku)
        mode_two_button = create_styled_button(
                self.frame, 
                "Challenge Agent Mode", 
                self.controller.show_mode_two
            )
        mode_two_button.pack(pady=10)
        
        # create a mode three button that route to (agent generate the sudoku board and user solve the sudoku)
        mode_three_button = create_styled_button(
                self.frame, 
                "User Challenge Mode", 
                self.controller.show_mode_three
            )
        mode_three_button.pack(pady=10)

        exit_button = create_styled_button(
                self.frame, 
                "Exit", 
                self.controller.quit
            )
        exit_button.pack(pady=10)
