''' import statements '''
from random import randint

''' declare global variables '''
# constants
BOARD_LENGTH = 8   # set row cell length 
TURN_COUNT = 5   # number of guesses a user gets

# parameter names
board = []   # 1D array
ship_row = 0   # default size
ship_col = 0   # default size

''' initialize board to all 0s ''' 
for x in range(BOARD_LENGTH):
    board.append(["O"] * BOARD_LENGTH)

def print_board(board):
    ''' print the entire board use
        0 for not guessed and x for already quessed space ''' 
    for row in board:
        print (" ".join(row))

''' Play the game and print the board ''' 
print ("\n\nLet's play Battleship!")
1
''' print the board to the screen '''
print_board(board)

def random_row(board):
    ''' select a random row '''
    return randint(0, len(board) - 1)

def random_col(board):
    ''' select a random column '''
    return randint(0, len(board[0]) - 1)
    
def set_ship_location():
    ''' computer sets the ship's location '''
    ship_row = random_row(board)
    ship_col = random_col(board)

set_ship_location()

# prompt user for row and column guess
for turn in range(TURN_COUNT):
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    # if the user's right, the game ends
    if guess_row == ship_row and guess_col == ship_col:
        print ("Congratulations! You sunk my battleship!")
        break
    else:
        # board boundary check
        if (guess_row < 0 or guess_row > (len(board)-1) or guess_col < 0 or guess_col > (len(board)-1)):
            # out of bounds warning
            print ("Oops, that's not even in the ocean. Please try again.")
         
        # warning if the guess was already made
        elif(board[guess_row][guess_col] == "X"):
            print ("You guessed that one already. Please try a new location.")

        # guess missed, mark location with an X, and continue play
        else:
            print ("Miss!")
            board[guess_row][guess_col] = "X"
            
        # print current turn number and board 
        print ("\nTurn " + str(turn+1) + " out of " + str(TURN_COUNT) + ".") 
        print_board(board)

# end game when player reaches allotted guess attemtps
if (turn+1) >= TURN_COUNT-1:
    print ("Game Over")