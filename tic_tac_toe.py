
import tkinter as tk
from engine import EngineInterface
import tkinter.messagebox

class Board():
    """The squares on the board are numbered as in the diagram:
     --- --- ---
    | 0 | 1 | 2 |
     --- --- ---
    | 3 | 4 | 5 |
     --- --- ---
    | 6 | 7 | 8 |
     --- --- ---
    """    
    def __init__(self, parent, side_length):

        self.canvas = tk.Canvas(parent, width=side_length, height=side_length,
                         highlightthickness=0)
        self.canvas.bind("<Button-1>", mouse_click)
        self.XO_list = [None for i in range(9)]

        self.padding = 20
        self.grid_side = side_length - 2 * self.padding
        p = self.padding
        s = self.grid_side
        self.square_center_coordinates = [(p + s // 6, p + s // 6),
                                          (p + s // 2, p + s // 6),
                                          (p + 5 * s // 6, p + s // 6),
                                          (p + s // 6, p + s // 2),
                                          (p + s // 2, p + s // 2),
                                          (p + 5 * s // 6, p + s // 2),
                                          (p + s // 6, p + 5 * s // 6),
                                          (p + s // 2, p + 5 * s // 6),
                                          (p + 5 * s // 6, p + 5 * s // 6)]

        # Draw grid.
        self.canvas.create_line(p, p + s // 3, p + s, p + s // 3, width=2)
        self.canvas.create_line(p, p + 2 * s // 3, p + s, p + 2 * s // 3, width=2)
        self.canvas.create_line(p + s // 3, p, p + s // 3, p + s, width=2)
        self.canvas.create_line(p + 2 * s // 3, p, p + 2 * s // 3, p + s, width=2)        

    def add_O(self, square):
        (x, y) = self.square_center_coordinates[square]
        radius = self.grid_side // 9
        o = O(self.canvas, x, y, radius)
        self.XO_list[square] = o

    def add_X(self, square):
        half_side_length = self.grid_side // 9
        (x, y) = self.square_center_coordinates[square]
        x = X(self.canvas, x, y, half_side_length)
        self.XO_list[square] = x

    def clear(self):
        """Remove all X and O's."""
        del self.XO_list
        self.XO_list = [None for i in range(9)]

    def highlight_three_in_a_row(self):
        squares = engine.three_in_a_row_squares(game_state)
        for square in squares:
            self.XO_list[square].color("blue")

    def pack(self):
        self.canvas.pack()

    def resize(self, side_length):
        self.canvas.config(width=side_length, height=side_length)
        self.canvas.delete("all")
        self.grid_side = side_length - 2 * self.padding
        p = self.padding
        s = self.grid_side
        self.square_center_coordinates = [(p + s // 6, p + s // 6),
                                          (p + s // 2, p + s // 6),
                                          (p + 5 * s // 6, p + s // 6),
                                          (p + s // 6, p + s // 2),
                                          (p + s // 2, p + s // 2),
                                          (p + 5 * s // 6, p + s // 2),
                                          (p + s // 6, p + 5 * s // 6),
                                          (p + s // 2, p + 5 * s // 6),
                                          (p + 5 * s // 6, p + 5 * s // 6)]

        # Draw grid.
        self.canvas.create_line(p, p + s // 3, p + s, p + s // 3, width=2)
        self.canvas.create_line(p, p + 2 * s // 3, p + s, p + 2 * s // 3, width=2)
        self.canvas.create_line(p + s // 3, p, p + s // 3, p + s, width=2)
        self.canvas.create_line(p + 2 * s // 3, p, p + 2 * s // 3, p + s, width=2)

        # Draw X's and O's.
        for square in range(9):
            if game_state[square] == "O":
                self.add_O(square)        
            if game_state[square] == "X":
                self.add_X(square)

    def update(self):
        self.canvas.update()

    def unbind_mouse(self):
        self.canvas.unbind("<Button-1>")

    def rebind_mouse(self):
        self.canvas.bind("<Button-1>", mouse_click)


class O():

    def __init__(self, canvas, x, y, radius, color="black"):
        self.canvas = canvas
        # The circle is drawn in a box of odd length in order to look good.      
        self.circle = self.canvas.create_oval(1 + x - radius, 1 + y - radius, x + radius, y + radius,
                                         width=2, outline=color)
    def __del__(self):
        self.canvas.delete(self.circle)

    def color(self, color):
        """Change the color of the O."""
        self.canvas.itemconfig(self.circle, outline=color)


class X():

    def __init__(self, canvas, x, y, half_side_length, color="black"):
        self.canvas = canvas
        h = half_side_length
        self.line_1 = self.canvas.create_line(x - h, y - h, x + h, y + h, width=2, fill=color)
        self.line_2 = self.canvas.create_line(x - h, y + h, x + h, y - h, width=2, fill=color)

    def __del__(self):
        self.canvas.delete(self.line_1)
        self.canvas.delete(self.line_2)

    def color(self, color):
        """Change the color of the X."""
        self.canvas.itemconfig(self.line_1, fill=color)
        self.canvas.itemconfig(self.line_2, fill=color)


def square_clicked(x, y):
    """Return the square 0-8 clicked given the coordinates x and y.
    The squares numbering are as described in the engine module.
    """    
    x = x - board.padding
    y = y - board.padding
    side = board.grid_side
    if 0 <= y <= side // 3:
        if 0 <= x <= side // 3:
            return 0
        elif side // 3 <= x <= 2 * side // 3:
            return 1 
        elif 2 * side // 3 <= x <= side:
            return 2

    elif side // 3 <= y <= 2 * side // 3:
        if 0 <= x <= side // 3:
            return 3
        elif side // 3 <= x <= 2 * side // 3:
            return 4
        elif 2 * side // 3 <= x <= side:
            return 5

    elif 2 * side // 3 <= y <= side:
        if 0 <= x <= side // 3:
            return 6
        elif side // 3 <= x <= 2 * side // 3:
            return 7
        elif 2 * side // 3 <= x <= side:
            return 8

def dialog_box(parent, text):
    """Return 'play' or 'quit'."""

    def play(event=None):
        box.destroy()
        update_difficulty_level()
        new_game()

    box = tk.Toplevel(parent)
    box.grab_set()
    box.focus_set()
    box.transient(parent)
    box.title("Tic Tac Toe")
    box_width = 300
    box_height = 120

    parent_width = parent.winfo_width()
    parent_height = parent.winfo_height()

    if box_width >= parent_width:
        x_offset = parent.winfo_rootx()
    else:
        x_offset = parent.winfo_rootx() + (parent_width - box_width) // 2

    y_offset = parent.winfo_rooty() + (parent_height - box_height - 40) // 2
    if y_offset < parent.winfo_rooty():
        y_offset = parent.winfo_rooty()

    box.geometry("%dx%d+%d+%d" % (box_width, box_height, x_offset, y_offset))

    text = tk.Label(box, text=text, font=("", 11, "bold"), borderwidth=10)
    text.pack()

    radio_button_frame = tk.Frame(master=box)
    tk.Radiobutton(radio_button_frame, text="Easy", font=("", 10),
                   variable=difficulty_level, value="Easy").pack(side=tk.LEFT)
    tk.Radiobutton(radio_button_frame, text="Medium", font=("", 10),
                   variable=difficulty_level, value="Medium").pack(side=tk.LEFT)
    tk.Radiobutton(radio_button_frame, text="Hard", font=("", 10),
                   variable=difficulty_level, value="Hard").pack()
    radio_button_frame.pack()

    button_frame = tk.Frame(master=box, pady=10)
    button_frame.pack()
    tk.Button(button_frame, text="Play", font=("", 10), width=8, command=play).pack(side=tk.LEFT)
    tk.Button(button_frame, text="Quit", font=("", 10), width=8, command=quit).pack()    
    box.bind("<Return>", play)
    box.bind("<Escape>", quit)

    # Call quit if the dialog box is closed.
    box.protocol("WM_DELETE_WINDOW", quit)

    parent.wait_window(window=box) # Wait for the dialog box to be destroyed.

def mouse_click(event):

    global score
    global game_state

    def update_and_rebind_mouse():
        board.update() # Handle mouse events before the rebind.
        board.rebind_mouse()

    board.unbind_mouse()
    square = square_clicked(event.x, event.y)
    if square == None:
        update_and_rebind_mouse()
        return

    # Check if valid move.
    if game_state[square] != " ":
        update_and_rebind_mouse()
        return None

    # Make the move.
    if player_is_X:
        game_state[square] = "X"
        board.add_X(square)
    else:
        game_state[square] = "O"
        board.add_O(square)
    board.update()

    # If player win.
    if engine.three_in_a_row(game_state):
        score[0] += 1
        title_update()
        board.highlight_three_in_a_row()
        board.update()
        root.after(1000)
        dialog_box(root, "You win! Congratulations!")     
        return

    # If draw.
    if " " not in game_state:
        root.after(600)
        dialog_box(root, "Draw")
        return

    # Engine makes a move.
    if " " in game_state:
        root.after(300)
        square = engine.engine_move(game_state)
        if player_is_X:
            game_state[square] = "O"
            board.add_O(square)
        else:
            game_state[square] = "X"
            board.add_X(square)
        board.update()

    # If computer win.
    if engine.three_in_a_row(game_state):
        score[1] += 1
        title_update()    
        board.highlight_three_in_a_row()
        board.update()
        root.after(1000)
        dialog_box(root, "Computer win!")
        return

    # If draw.
    if " " not in game_state:
        root.after(600)
        dialog_box(root, "Draw")
        return

    # Else.
    update_and_rebind_mouse()

def new_game():
    board.clear()
    global player_is_X
    player_is_X = not player_is_X
    global game_state
    game_state = [" ", " ", " ",
                  " ", " ", " ",
                  " ", " ", " "]   
    board.update()

    if not player_is_X:
        root.after(300)
        square = engine.engine_move(game_state)
        game_state[square] = "X"
        board.add_X(square)

    board.update() # Handle events before mouse rebind.
    board.rebind_mouse()

def title_update():
    root.title("Tic Tac Toe: " + str(score[0]) + " - " + str(score[1]))

def update_difficulty_level():
    """Update the difficulty level in the engine and reset score if
    the level is changed."""
    current_level = engine.difficulty_level
    if difficulty_level.get() == "Easy":
        engine.difficulty_level = 1
    elif difficulty_level.get() == "Medium":
        engine.difficulty_level = 2
    elif difficulty_level.get() == "Hard":
        engine.difficulty_level = 3
    if engine.difficulty_level != current_level:
        global score
        score = [0, 0]
        title_update()

def quit(event=None):
    board.clear()
    root.destroy()

engine = EngineInterface(2)

game_state = [" ", " ", " ",
              " ", " ", " ",
              " ", " ", " "]

root = tk.Tk()
root.resizable(False, False)

# Call quit if the dialog box is closed.   
root.protocol("WM_DELETE_WINDOW", quit)

score = [0, 0]
title_update()

difficulty_level = tk.StringVar()
difficulty_level.set("Medium")

board = Board(root, 500)
board.pack()

# A variable to keep track of when player is X.
player_is_X = False

root.update()
dialog_box(root, "New game")

root.mainloop()
