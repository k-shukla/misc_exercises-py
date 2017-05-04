# This section imports the random module (which is built-in into Python).
import random

# This section creates an empty board which will later be expanded to fill the specified board size, and also sets the parameters for board size and number of guesses.
board = []
board_size = 5
guesses = 4

# This section expands the board to the specified board size.
for x in xrange(board_size):
    board.append(["O"] * board_size)

# This section defines print_board, which prints the board so that it can be seen.
def print_board(board):
    for row in board:
        print " ".join(row)

# This section defines random_row, which generates the row where the battleship will be located.
def random_row(board):
    return random.randint(0, (board_size - 1))

# This section defines random_col, which generates the column where the battleship will be located.
def random_col(board):
    return random.randint(0, (board_size - 1))

# This section prints the opening.
print "Let's play Battleship! Four turns to sink the battleship."
print "Turn 1"
print_board(board)
	
# This section assigns the ship to the row and column just generated. For debugging, the values are printed; if you actually want to play this, comment the print statements out.
ship_row = random_row(board)
ship_col = random_col(board)
print ship_row + 1
print ship_col + 1

# This section handles the paths for each turn.
for turn in xrange(guesses):
    guess_row = (int(raw_input("Guess Row:")) - 1)
    guess_col = (int(raw_input("Guess Col:")) - 1)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row not in xrange(board_size)) or (guess_col not in xrange(board_size)):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        if turn == (guesses - 1):
            print "Game Over"
            break
    print "Turn", (turn + 2)
    print_board(board)