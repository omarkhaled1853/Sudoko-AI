import tkinter as tk
from Sudoku_GUI.Pages.base_page import BasePage
from Sudoku_GUI.utils import create_styled_label
from Sudoku_GUI.utils import create_styled_button

class ModeOnePage(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        mode_one_label = create_styled_label(
            self.base_page_frame,
            "Agent Challenge Mode",
            16
        )
        mode_one_label.pack(pady=20)

        back_button = create_styled_button(
            self.base_page_frame,
            "<- Back to Menu",
            controller.show_menu
        )
        back_button.pack(pady=10)