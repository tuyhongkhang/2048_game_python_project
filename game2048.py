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
            mtx = self.shiftAndSum(np.fliplr(self.board).tolist())
            self.board = np.fliplr(mtx).tolist() # flip back
        elif dir == 'w':
            mtx = self.shiftAndSum(np.transpose(self.board).tolist())
            self.board = np.transpose(mtx).tolist()
        elif dir == 's':
            tmp = np.transpose(self.board)
            mtx = self.shiftAndSum(np.fliplr(tmp).tolist())
            mtx = np.fliplr(mtx)
            self.board = np.transpose(mtx).tolist()
            
    def shiftAndSum(self, mtx):
        for k in range(len(mtx)):
            i1 = None
            for i2 in range(len(mtx)):
                if mtx[k][i2] == 0:
                    continue
                if i1 is None or mtx[k][i1] != mtx[k][i2]:
                    try:
                        x = mtx[k].index(0)
                    except:
                        x = i2
                    tmp = i2 if i2 <= x else x
                    val = mtx[k][i2]
                    mtx[k][i2] = 0
                    mtx[k][tmp] = val
                    i1 = tmp
                else:
                    mtx[k][i1] = mtx[k][i1]*2
                    mtx[k][i2] = 0
                    i1 = None    
        return mtx
