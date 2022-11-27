import random
import numpy as np

class Board():
    def __init__(self):
        print("_______Welcome to 2048_______")
        # Choose board size (default 4) and handle bad input
        try:
            self.size = int(input("Enter size of your board (default 4): "))
        except:
            self.size = 4
        self.status = 0 # 0 means still playing, -1 means lose, 1 means victory
        self.board = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.startGame()
    
    # Add a 2 to a random, empty square
    def addRandom(self):
        # if no empty square left, then skip
        tmp = np.array(self.board).flatten()
        if 0 not in tmp.tolist():
            return

        row, col = -1, -1
        while row == -1 or self.board[row][col] != 0:
            row = random.randint(0,self.size-1)
            col = random.randint(0,self.size-1)
        self.board[row][col] = 2
    
    # Print out the board for players
    def printBoard(self):
        for r in self.board:
            for c in r:
                print(c, end = " ")
            print()
        print()
    
    # Main logic of the code
    def startGame(self):
        # print out valid commands
        print("Here are the valid commands:")
        print("\ta: swipe left")
        print("\td: swipe right")
        print("\tw: swipe up")
        print("\ts: swipe down")
        print("\tx: exit the game")
        print()
        
        # Init game, starting with 2 random squares of 2s
        self.addRandom()
        self.addRandom()
        self.printBoard()
        while True:
            command = input("Command: ")
            if command in ('a','d','w','s'):
                tmp = [x[:] for x in self.board] # copy self.board into tmp to compare
                self.swipe(command)
                # no more move in this direction
                if tmp == self.board: 
                    print("No possible move in this direction!")
                    print()
                else:
                    self.addRandom()
                self.printBoard()

                # Victory
                if self.status == 1:
                    print("Victory!Good game well play!")
                    break
                # Game over
                if self.gameOver() == True:
                    print("Game over! No more possible move!")
                    break
                
            # Quit mid game
            elif command == 'x':
                print("Game ends. See you again!")
                quit()
            # invalid input
            else:
                print('Invalid input!')
        # ask to restart game if victory or game over
        self.restart()
    
    # handle swiping commands in 4 directions
    # Call shiftAndSum() and pass in corresponding mtx
    def swipe(self, dir):
        # swipe left
        if dir == 'a':
            mtx = self.shiftAndSum(self.board)
            self.board = mtx
        # swipe right = swipe left of the flipped matrix
        elif dir == 'd':
            mtx = self.shiftAndSum(np.fliplr(self.board).tolist()) # flip
            self.board = np.fliplr(mtx).tolist() # flip back
        # swipe up = swipe left of the transpose
        elif dir == 'w':
            mtx = self.shiftAndSum(np.transpose(self.board).tolist()) # transpose
            self.board = np.transpose(mtx).tolist() # transpose back
        # swipe down = swipe left of the flipped transpose
        elif dir == 's':
            tmp = np.transpose(self.board) # transpose
            mtx = self.shiftAndSum(np.fliplr(tmp).tolist()) # flip
            mtx = np.fliplr(mtx) # flip back
            self.board = np.transpose(mtx).tolist() # transpose back
            
    # Given mtx, perform swiping left command
    # Handle both shifting and summing squares
    def shiftAndSum(self, mtx):
        for k in range(len(mtx)):
            i1 = None
            for i2 in range(len(mtx)):
                if mtx[k][i2] == 0:
                    continue # skip squares with 0
                if i1 is None or mtx[k][i1] != mtx[k][i2]:
                    try:
                        x = mtx[k].index(0) # find first 0s
                    except:
                        x = i2
                    # tmp is guaranteed to be the correct position to be shift
                    tmp = i2 if i2 <= x else x # either shift to index of 1st 0 or i2
                    val = mtx[k][i2]
                    mtx[k][i2] = 0
                    mtx[k][tmp] = val # shift
                    i1 = tmp
                else: # when found value equal to val at i1
                    # Don't need to shift b/c already take care when we found i1
                    mtx[k][i1] = mtx[k][i1]*2 # sum
                    mtx[k][i2] = 0
                    if mtx[k][i1] == 2048:
                        self.status = 1 # victory
                    i1 = None       
        return mtx
    
    # Check if the game is over. 
    # I.e., no zeros and no identical squares next to each other
    def gameOver(self):
        for r in range(self.size):
            for c in range(self.size):
                if (self.board[r][c] == 0 or
                   (r-1 >= 0 and self.board[r][c] == self.board[r-1][c]) or
                   (r+1 < self.size and self.board[r][c] == self.board[r+1][c]) or
                   (c-1 >= 0 and self.board[r][c] == self.board[r][c-1]) or
                   (c+1 < self.size and self.board[r][c] == self.board[r][c+1])):
                   return False # not over yet
        self.status = -1
        return True
    
    # Restart the game depending on input
    def restart(self):
        i = input('Do you want to play again (y/n)?')
        while i != 'y' and i!= 'n':
            print('Invalid input!')
            i = input('Do you want to play again (y/n)?')
        if i == 'y': # if yes, then init the game again
            self.__init__()
        else:
            print("Game ends. See you again!")
            quit() # Quit the program