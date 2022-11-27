import random
import numpy as np

class Board():
    def __init__(self, size):
        self.status = 0 # 0 means still playing, -1 means lose, 1 means victory
        self.size = size
        self.board = [[0 for _ in range(size)] for _ in range(size)]
        self.startGame()
    
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
        
        # Init game, starting with 2 random squares of 2s
        self.addRandom()
        self.addRandom()
        self.printBoard()
        while True:
            command = input("Command: ")
            if command in ('a','d','w','s'):
                tmp = [x[:] for x in self.board]
                self.swipe(command)
                if tmp == self.board: # no more move in this direction
                    print("No possible move in this direction!")
                    print()
                else:
                    self.addRandom()
                self.printBoard()

                # Check output after swiping
                if self.status == 1:
                    print("Victory!Good game well play!")
                    break
                if self.gameOver() == True:
                    print("Game over! No more possible move!")
                    break
                

            elif command == 'x':
                print("Game ends. See you again!")
                quit()
            else:
                print('Invalid input!')
        self.restart()
        
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
                    if mtx[k][i1] == 2048:
                        self.status = 1 # victory
                    i1 = None       
        return mtx
    

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
    
    def restart(self):
        i = input('Do you want to play again (y/n)?')
        while i != 'y' and i!= 'n':
            print('Invalid input!')
            i = input('Do you want to play again (y/n)?')
        if i == 'y':
            self.__init__(self.size)
        else:
            print("Game ends. See you again!")
            quit() # Quit the program