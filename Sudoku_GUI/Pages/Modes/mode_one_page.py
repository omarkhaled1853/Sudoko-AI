import tkinter as tk
from Sudoku_GUI.Pages.base_page import BasePage
from Sudoku_GUI.utils import create_styled_label
from Sudoku_GUI.utils import create_styled_button
from Sudoku_logic.random_sudoku_board import RandomSudokuBoard
from Sudoku_logic.sudoku_solver import SudokuSolver

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
                self.grid_entries[row][col] = entry

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

    def create_action_buttons(self):
        """Creates the action buttons."""
        # Make a frame for action buttons
        frame = tk.Frame(self.container_frame, bg='#FFFFFF')
        frame.grid(row=1, column=0, columnspan=2, pady=10)

        # Create "Generate random board" button
        generate_randome_board_button = create_styled_button(frame, "Generate Random Board", self.generate_randome_board)
        generate_randome_board_button.grid(row=0, column=1, padx=10, pady=5)

        # todo
        # Create "Solve board" button
        solve_board_button = create_styled_button(frame, "Solve Board", self.solve_board)
        solve_board_button.grid(row=0, column=2, padx=10, pady=5)

    def update_grid_entries_before_solve(self):
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
                    self.grid_entries[i][j].config(foreground="#344861")
                else:
                    self.grid_entries[i][j].config(readonlybackground="#F6F9FC")
                    
                # Set back to readonly
                self.grid_entries[i][j].config(state="readonly")

    def update_grid_entries_after_solve(self):
        """Update board after solve board"""
        for i in range(9):
            for j in range(9):
                # Insert the selected number
                if (i, j) not in self.generated_cells:
                    # Temporarily enable editing to update cell
                    self.grid_entries[i][j].config(state="normal")
                    # Delete the existing value if any
                    self.grid_entries[i][j].delete(0, tk.END)
                    self.grid_entries[i][j].insert(0, str(self.board[i][j]))
                    self.grid_entries[i][j].config(foreground="#E55C6C")
                    
                # Set back to readonly
                self.grid_entries[i][j].config(state="readonly")

    def generate_randome_board(self):
        """Generate randome board"""
        # Initialize randome board generator class
        random_sudoku = RandomSudokuBoard(9, 30)
        self.board = random_sudoku.get_board_with_unique_solution()
        self.update_grid_entries_before_solve()

    def solve_board(self):
        sudoku_solver = SudokuSolver(self.board)
        self.board = sudoku_solver.solve()
        self.update_grid_entries_after_solve()
        # print(self.board)