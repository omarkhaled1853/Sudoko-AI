import tkinter as tk
from Sudoku_GUI.Pages.base_page import BasePage

class ModeTwoPage(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        mode1_label = tk.Label(self.frame, text="Mode 2: Basic Game", font=("Arial", 16))
        mode1_label.pack(pady=20)

        back_button = tk.Button(self.frame, text="Back to Menu", font=("Arial", 14), command=controller.show_menu)
        back_button.pack(pady=10)