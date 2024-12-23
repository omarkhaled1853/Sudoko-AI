import tkinter as tk
from Sudoku_GUI.Pages.base_page import BasePage
from Sudoku_GUI.utils import create_styled_label
from Sudoku_GUI.utils import create_styled_button
from Sudoku_logic.random_sudoku_board import random_sudoku_board

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

        # Create a container frame to hold all frames
        self.container_frame = tk.Frame(self.base_page_frame, bg='#FFFFFF')
        self.container_frame.config(padx=10, pady=10, bg='#FFFFFF')
        self.container_frame.pack(fill=tk.BOTH, expand=True)

        # Initialize the suduko as 9x9 grid of entries 
        self.grid_entries: list[list[tk.Entry]] = [[None for _ in range(9)] for _ in range(9)]
        # To track the currently selected number from number pad
        self.selected_number: tk.StringVar = tk.StringVar(value="")
        # To track the currently selected cell
        self.selected_cell: tuple = None
        # Initialize board
        self.board: list[list] = []
        # Initialize generated cells
        self.generated_cells = set()

        # Initialize sudoku grid
        self.create_sudoku_grid()
        # Initialize number pad
        self.create_number_pad()
        # Initialize action buttons
        self.create_action_buttons()
        # generate randome board initialy
        self.generate_randome_board()  

    def create_sudoku_grid(self):
        """Creates the Sudoku grid."""
        # Make a frame for the suduko grid entries
        frame = tk.Frame(self.container_frame, bg='#FFFFFF')
        frame.grid(row=0, column=0, padx=20, pady=20)

        for row in range(9):
            for col in range(9):
                entry = tk.Entry(
                    frame,
                    width=2,
                    font=("Arial", 18, "bold"),
                    justify="center",
                    highlightthickness=2,
                    highlightbackground="#A0AFC4",
                    highlightcolor="#4A90E2",
                    state="readonly",
                    cursor="hand2",
                    readonlybackground="#F6F9FC",
                    foreground="#344861",
                    relief="flat",
                )
                entry.grid(
                    row=row,
                    column=col,
                    padx=(5 if col % 3 == 0 else 1, 0),
                    pady=(5 if row % 3 == 0 else 1, 0),
                )
                # Bind button action when select an entry 
                entry.bind("<Button-1>", lambda e, r=row, c=col: self.select_cell(r, c))
                self.grid_entries[row][col] = entry

    def select_cell(self, row: int, col: int):
        """Highlights the selected cell and stores its position."""
        # Save the currently selected cell
        self.selected_cell = (row, col)  
        if self.selected_cell not in self.generated_cells:
            self.highlight_related_cells(row, col)

    def highlight_related_cells(self, row, col):
        """Highlights the selected cell, its row, column, and 3x3 subgrid."""
        self.clear_highlighting()

        for i in range(9):
            # Highlight the row and column
            self.set_cell_highlight(self.grid_entries[row][i], "#E2EBF3")
            self.set_cell_highlight(self.grid_entries[i][col], "#E2EBF3")

        # Calculate the start row and start column of the 3x3 subgrid releted to selected cell
        start_row, start_col = (row // 3) * 3, (col // 3) * 3
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                # Highlight the 3x3 subgrid releted to selected cell
                self.set_cell_highlight(self.grid_entries[r][c], "#E2EBF3")

        # Highlight the selected cell
        self.set_cell_highlight(self.grid_entries[row][col], "#BBDEFB")

    def set_cell_highlight(self, cell: tk.Entry, color: str):
        """Set the background color of a cell, respecting the readonly state."""
        cell.config(readonlybackground=color)

    def clear_highlighting(self):
        """Clears all highlights from the grid with default color."""
        for row in range(9):
            for col in range(9):
                if (row, col) not in self.generated_cells:
                    self.set_cell_highlight(self.grid_entries[row][col], "white")
                else:
                    self.set_cell_highlight(self.grid_entries[row][col], "#D3D3D3")

    def create_number_pad(self):
        """Creates a stylish number pad."""
        # Create a frame for the number pad
        frame = tk.Frame(self.container_frame, bg='#FFFFFF')
        frame.grid(row=0, column=1, padx=20, pady=20)

        for i in range(1, 10):
            # Create a button with improved styling
            button = tk.Button(
                frame,
                text=str(i),
                font=("Arial", 18, "bold"),
                width=4,
                height=2,
                cursor="hand2",
                background="#EAEEF4",
                foreground="#325AAF",
                activebackground="#CFE2FF",
                activeforeground="#1D3F8B",
                bd=2,
                relief="raised",
                command=lambda n=i: self.set_selected_number(n),
            )

            # Bind hover effects to enhance interactivity
            button.bind("<Enter>", lambda event, b=button: b.config(background="#DDE6F8", foreground="#1D3F8B"))
            button.bind("<Leave>", lambda event, b=button: b.config(background="#EAEEF4", foreground="#325AAF"))

            # Place the button in a grid layout
            button.grid(row=(i - 1) // 3, column=(i - 1) % 3, padx=5, pady=5)


    def set_selected_number(self, number):
        """Sets the selected number from number pad in the selected cell in suduko grid entries."""
        if self.selected_cell and self.selected_cell not in self.generated_cells:
            self.selected_number.set(str(number))
            # Get the selected cell
            row, col = self.selected_cell
            # Temporarily enable editing to update cell
            self.grid_entries[row][col].config(state="normal")
            # Delete the existing value if any
            self.grid_entries[row][col].delete(0, tk.END)
            # Insert the selected number
            self.grid_entries[row][col].insert(0, str(number))  
            # Set back to readonly
            self.grid_entries[row][col].config(state="readonly")  

    def create_action_buttons(self):
        """Creates the action buttons."""
        # Make a frame for action buttons
        frame = tk.Frame(self.container_frame, bg='#FFFFFF')
        frame.grid(row=1, column=0, columnspan=2, pady=10)

        # Create "Erase" button
        erase_button = create_styled_button(frame, "Erase", self.erase_cell)
        erase_button.grid(row=0, column=1, padx=10, pady=5)

        # Create "Generate random board" button
        generate_randome_board_button = create_styled_button(frame, "Generate Random Board", self.generate_randome_board)
        generate_randome_board_button.grid(row=0, column=2, padx=10, pady=5)

        # todo
        # Create "Solve board" button
        solve_board_button = create_styled_button(frame, "Solve Board", self.solve_board)
        solve_board_button.grid(row=0, column=3, padx=10, pady=5)


    def erase_cell(self):
        """Erases the content of the focused cell."""
        if self.selected_cell and self.selected_cell not in self.generated_cells:
            # Get the selected cell
            row, col = self.selected_cell
            # Temporarily enable editing to update cell
            self.grid_entries[row][col].config(state="normal")
            # Delete the existing value if any
            self.grid_entries[row][col].delete(0, tk.END)
            # Set back to readonly
            self.grid_entries[row][col].config(state="readonly") 

    def update_grid_entries(self):
        """Update board with the new generated number"""
        self.generated_cells.clear()
        for i in range(9):
            for j in range(9):
                # Temporarily enable editing to update cell
                self.grid_entries[i][j].config(state="normal")
                # Delete the existing value if any
                self.grid_entries[i][j].delete(0, tk.END)
                # Insert the selected number
                if self.board[i][j] != '0':
                    self.generated_cells.add((i, j))
                    self.grid_entries[i][j].insert(0, str(self.board[i][j]))
                    self.grid_entries[i][j].config(readonlybackground="#D3D3D3")
                else:
                    self.grid_entries[i][j].config(readonlybackground="#F6F9FC")
                    
                # Set back to readonly
                self.grid_entries[i][j].config(state="readonly") 

    def generate_randome_board(self):
        """Generate randome board"""
        # Initialize randome board generator class
        random_sudoku = random_sudoku_board(9, 30)
        self.board = random_sudoku.get_board_with_unique_solutino()
        self.update_grid_entries()

    # todo
    def solve_board(self):
        pass