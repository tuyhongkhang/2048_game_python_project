import random
import numpy

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
    
    def __str__(self):
        print(numpy.matrix(self.board))
    
    def startGame(self):
        # print out valid commands
        
        # Pick 2 random square to start the game
        self.addRandom()
        self.addRandom()
        
    def swipe(self, dir):
        r = 0
        c = 0
        while r < self.size:
            self.board[r]
            r += 1
            a = [0,2,0,2]
b = [4,2,0,2]
b = [4,4,2,2]

i1, i2 = -1,-1
for i in range(len(a)):
    if a[i] != 0:
        if i1 == -1:
            i1 = i
        elif a[i1] == a[i]:
            tmp = a.find(0)
            if tmp == -1:
                tmp = i1
            a[tmp] = 2*a[i1]
            a[i1] = 0
            a[i] = 0
            i1 = -1
            
        
        
        
