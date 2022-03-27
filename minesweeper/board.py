import random

# a board object represents the minesweeper game
# it can handle the functionalities of the game like digging,
# building and displaying the board, assigning values to the board

class Board:
    def __init__(self, b_size, num_bombs):
        # I keep track of the below parameters, because they'll be useful
        self.b_size = b_size
        self.num_bombs = num_bombs

        # creating the board
        self.board = self.make_new_board() # plant the bombs
        self.assign_values_to_board()

        # initialize a set to keep track of which locations player has uncovered
        # I'll save (row,col) tuples into this set
        self.dug = set() # if player digs at 0,0 then self.dug = {(0,0)}

    def make_new_board(self):
        # construct a new board based on the b_size and num_bombs
        # I construct the list of lists here

        # generate a new board
        board = [[ None for _ in range(self.b_size)] for _ in range(self.b_size) ] # list comprehension
        # this creates an array like this:
        # [[None, None, ..., None],
        #  [None, None, ..., None],
        #  [...                  ],
        #  [None, None, ..., None]]
        # it looks like a board

        # plant the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.b_size ** 2 - 1) # random integer between a and b
            row = loc // self.b_size   # info which row it is
            col = loc % self.b_size    # info which column it is

            if board[row][col] == '*':
                # it means I've already planted a bomb there so I keep going
                continue

            board[row][col] = '*'  # plant the bomb
            bombs_planted += 1

        return board

    def assign_values_to_board(self):
        # now the bombs are planted, I'll assign a number 0-8 for all the empty spaces, which
        # represents how many neighboring bombs there are. I'll precompute these and it'll save me some
        # effort checking what's around the board later on
        for r in range(self.b_size):
            for c in range(self.b_size):
                if self.board[r][c] == '*':
                    # if this is already a bomb, I don't calculate anything
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):
         # I'll iterate through each of the neighboring positions and sum number of bombs
         # I make sure to not go out of bounds

         num_neighboring_bombs = 0
         for r in range(max(0, row-1), min(self.b_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.b_size-1, col+1)+1):
                if r == row and c == col:
                    # my original location, don't check
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1

         return num_neighboring_bombs

    def dig(self, row, col):
        # dig at that location
        # return True if successful, False if bomb dug

        # a few scenarios:
        # hit a bomb -> game over
        # dig at location with neighboring bombs -> finish dig
        # dig at location with no neighboring bombs -> recursively dig neighbors

        self.dug.add((row,col)) # keep track that player dug here

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True

        # self.board[row][col] == 0
        for r in range(max(0, row-1), min(self.b_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.b_size-1, col+1)+1):
                if (r, c) in self.dug:
                    continue  # I don't dig where I've already dug
                self.dig(r, c)

        # if my initial dig didn't hit a bomb, I shoudn't hit a bomb here
        return True

    def __str__(self):
        # this is a magic function where if I call print on this object,
        # it'll print out what this function returns!
        # return a string that shows the board to the player

        # first I create a new array that represents what the user would see
        visible_board = [ [ None for _ in range(self.b_size) ] for _ in range(self.b_size) ] # list comprehension
        for row in range(self.b_size):
            for col in range(self.b_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '

        # put the output in a string
        str_output = '...'
        for i in range(self.b_size):
            if i <= 9:
                str_output += f'{i}  '
            else:
                str_output += f'{i} '  # numbers >=10 take 2 spaces, so I removed one space between them so that a board is even
            

        str_output += '\n'

        for i in range(self.b_size + 1):
            str_output += '---'

        str_output += '\n'

        for row in range(self.b_size):
            if row <= 9:
                str_output += f'{row} |'
            else:
                str_output += f'{row}|'  # numbers >=10 take 2 spaces, so I removed one space between them so that a board is even
            
            for col in range(self.b_size):
                str_output += f' {visible_board[row][col]}|'

            str_output += '\n'

        for i in range(self.b_size + 1):
            str_output += '---'

        return str_output
                

        

