from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

#to print board
def print_board(board):
    for row in board:
        print " ".join(row)


print "Let's play Battleship!"
print_board(board)

# to give random value
def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):
    print "turn :", turn + 1
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
# if u guessed right
    if (guess_row == ship_row and guess_col == ship_col):
        print "Congratulations! You sunk my battleship!"
        break;
    else: #if u guessed wrong
        print"You missed my battleship!"
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif (board[guess_row] == "X" and board[guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "Your guess is wrong!"
            board[guess_row][guess_col] = "X"
    print_board(board)
# to tell the game is over
if turn == 3:
    print "Game Over\n RESULT"

print "correct row: ",ship_row
print "correct column: ",ship_col