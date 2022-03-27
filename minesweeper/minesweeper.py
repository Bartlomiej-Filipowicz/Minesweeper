from board import Board
import re
# the purpose of this function is to play the game

# Step 1: create the board and plant the bombs
# Step 2: show the user the board and ask for where they want to dig
# Step 3a: if location is a bomb, show 'game over' message
# Step 3b: if location is not a bomb, dig recursively until each square is at least next to a bomb
# Step 4: repeat steps 2 and 3a/b until there are no more places to dig

def play(b_size = 10, num_bombs = 10):   # b_size is a size of the board, num_bombs is a number of bombs on the board
    
    myboard = Board(b_size, num_bombs)

    safe = True

    while len(myboard.dug) < myboard.b_size ** 2 - num_bombs:
        print(myboard)  # \s means space
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col: ")) # it handles the input like 1,3 or 1, 3 or 1,   3
        row, col = int(user_input[0]), int(user_input[-1]) # -1 means the last element

        if row < 0 or row >= myboard.b_size or col < 0 or col >= myboard.b_size:
            print('Invalid location. Try again.')
            continue

        # if it's valid, I dig
        safe = myboard.dig(row, col)
        if not safe:
            # dug a bomb!!
            break # game over

    # 2 ways to end loop, I'll check which one
    if safe:
        print("Congrats!!! You won!")
    else:
        print('Sorry. You lost. Game over')
        # time to reveal the whole board
        myboard.dug = [ (r, c) for r in range(myboard.b_size) for c in range(myboard.b_size) ] # list comprehension
        # ^^^ I 'dug' everywhere in order to print the board
        print(myboard)


if __name__ == '__main__': # the function play() will be called only if minesweeper.py is run
    play(14,14)


    
    
    