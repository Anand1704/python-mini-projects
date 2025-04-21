import tkinter as tk

# Unicode symbols for chess pieces
pieces = {
    "R": "♜", "N": "♞", "B": "♝", "Q": "♛", "K": "♚", "P": "♟",  # Black pieces
    "r": "♖", "n": "♘", "b": "♗", "q": "♕", "k": "♔", "p": "♙"   # White pieces
}

# Initial chessboard setup
chessboard = [
    ["R", "N", "B", "Q", "K", "B", "N", "R"],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["r", "n", "b", "q", "k", "b", "n", "r"]
]

def create_chessboard():
    root = tk.Tk()
    root.title("Chessboard")

    cell_size = 60  # Size of each square

    canvas = tk.Canvas(root, width=8 * cell_size, height=8 * cell_size)
    canvas.pack()

    for row in range(8):
        for col in range(8):
            # Alternate colors for chessboard squares
            color = "#DDB88C" if (row + col) % 2 == 0 else "#A66D4F"
            x1, y1 = col * cell_size, row * cell_size
            x2, y2 = x1 + cell_size, y1 + cell_size
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

            # Place chess pieces
            piece = chessboard[row][col]
            if piece:
                canvas.create_text(
                    x1 + cell_size / 2, y1 + cell_size / 2,
                    text=pieces[piece], font=("Arial", 30), fill="black" if piece.isupper() else "white"
                )

    root.mainloop()

create_chessboard()