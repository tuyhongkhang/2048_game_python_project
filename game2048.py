import random
import numpy as np

class Board():
    def __init__(self, size):
        self.size = size
        self.board = [[0 for _ in range(size)] for _ in range(size)]
        self.startGame()
    
    def addRandom(self):
        row, col = -1, -1
        while row == -1 or self.board[row][col] != 0:
            row = random.randint(0,self.size-1)
            col = random.randint(0,self.size-1)
        self.board[row][col] = 2
    
    def printBoard(self):

        for r in self.board:
            for c in r:
                print(c, end = " ")
            print()
        print()
    
    def startGame(self):
        # print out valid commands
        print("_______Welcome to 2048_______")
        print("Here are the valid commands:")
        print("\ta: swipe left")
        print("\td: swipe right")
        print("\tw: swipe up")
        print("\ts: swipe down")
        print("\tx: exit the game")
        print()
        
        # Init game, starting with 2 random squares
        self.addRandom()
        self.addRandom()

        self.printBoard()
        command = ''
        while command != 'x':
            command = input("Command: ")
            if command in ('a','d','w','s'):
                self.swipe(command)
                self.addRandom()
                self.printBoard()
            elif command == 'x':
                print("Game ends. See you again!")
            else:
                print('Invalid input!')
        

        
    def swipe(self, dir):
        if dir == 'a':
            mtx = self.shiftAndSum(self.board)
            self.board = mtx
        elif dir == 'd':
            mtx = self.shiftAndSum(np.fliplr(self.board))
            self.board = np.fliplr(mtx) # flip back
        elif dir == 'w':
            mtx = self.shiftAndSum(np.transpose(self.board))
            self.board = np.transpose(mtx)
        elif dir == 's':
            tmp = np.transpose(self.board)
            mtx = self.shiftAndSum(np.fliplr(tmp))
            mtx = np.fliplr(mtx)
            self.board = np.transpose(mtx)
            
    def shiftAndSum(self, mtx):
        for arr in mtx:
            i1 = None
            for i2 in range(self.size):
                if arr[i2] == 0:
                    continue
                if i1 is None or arr[i1] != arr[i2]:
                    try:
                        x = arr.index(0)
                    except:
                        x = i2
                    tmp = i2 if i2 <= x else x
                    val = arr[i2]
                    arr[i2] = 0
                    arr[tmp] = val
                    i1 = tmp
                else:
                    arr[i1] = arr[i1]*2
                    arr[i2] = 0
                    i1 = None
        print("*",mtx)
        return mtx
