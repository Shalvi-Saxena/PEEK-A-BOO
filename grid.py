import sys
import time
import random

class MyGrid:
    # n - size of array
    # arr - grid
    # score
    # variables to maintain count of visible Elements and actual guesses
    size = None
    arr = None
    score = 0
    visibleElements = 0
    minimumPossibleGuesses = 0
    actualGuesses = 0
    isValidSize = True
    col1 = -1
    row1 = -1
    col2 = -1
    row2 = -1

    # Initializing Grid
    def __init__(self, n):
        self.isLenValid(n)
        if self.isValidSize:
            self.size = n
            self.arr = [[0*self.size]*self.size]
            self.arr = [[0 for x in range(self.size)] for y in range(self.size)]
            self.minimumPossibleGuesses = (self.size*self.size)/2
            self.actualGuesses = 0
            self.score = 0
            self.populateGrid()

    # Method to validate the input
    def isLenValid(self, n):
        if n != 2 and n != 4 and n != 6:
            print("Please enter 2, 4, or 6")
            self.isValidSize = False

    # Method to populate the grid randomly
    def populateGrid(self):
        rangeSeq = int((self.size * self.size)/2)

        rangeArr = [i for i in range(rangeSeq)]
        random.shuffle(rangeArr)

        sequenceCol = [i for i in range(self.size)]
        random.shuffle(sequenceCol)

        sequenceRow = [i for i in range(self.size)]
        random.shuffle(sequenceRow)
        x=0

        for i in sequenceRow:
            for j in sequenceCol:
                self.arr[i][j] = [False, rangeArr[x]]
                x += 1
                if x == rangeSeq:
                    x=0
                    random.shuffle(rangeArr)

    # Method to validate cell number passed in choice1
    def validateCell(self, cell):
        if len(cell) != 2:
            return False
        str = cell.upper()
        if ord(str[0]) < 65 or ord(str[0]) >= (65+self.size):
            print("Input error: column entry is out of range for this grid. Please try again")
            return False
        if ord(str[1]) < 48 or ord(str[1]) >= (48+self.size):
            print("Input error: row entry is out of range for this grid. Please try again")
            return False
        return True

    # Method to Display Grid
    def displayGrid(self):
        print("     ", end="")
        for x in range(self.size):
            print('[{}]'.format(chr(65+x)),end = "  ")
        print()
        visibleElements = 0
        for x in range(self.size):
            print('[{}]'.format(x), end="   ")
            for y in range(self.size):
                if self.arr[x][y][0]:
                     print(self.arr[x][y][1], end="    ")
                     visibleElements += 1
                elif (x == self.row1 and y == self.col1):
                    self.row1 = -1
                    self.col1 = -1
                    print(self.arr[x][y][1], end="    ")
                elif (x == self.row2 and y == self.col2):
                    self.row2 = -1
                    self.col2 = -1
                    print(self.arr[x][y][1], end="    ")
                else:
                    print("X", end="    ")
            print()
        self.visibleElements = visibleElements

    # Method to change the visibility of the cell
    def changeVisibility(self, coOrd1, coOrd2):
        coOrd1 = coOrd1.upper()
        col1 = ord(coOrd1[0])-65
        row1 = ord(coOrd1[1])-48
        coOrd2 = coOrd2.upper()
        col2 = ord(coOrd2[0]) - 65
        row2 = ord(coOrd2[1]) - 48

        if self.arr[row1][col1][0] and self.arr[row2][col2][0]:
            return -1, -1, col2, row2
        elif (self.arr[row1][col1][1] == self.arr[row2][col2][1]):
            if not self.arr[row1][col1][0]:
                self.visibleElements += 1
            if not self.arr[row2][col2][0]:
                self.visibleElements += 1
            self.arr[row1][col1][0] = True
            self.arr[row2][col2][0] = True


        self.col1 = col1
        self.row1 = row1
        self.col2 = col2
        self.row2 = row2

        self.actualGuesses += 1
        return col1, row1, col2, row2, (self.arr[row1][col1][1] == self.arr[row2][col2][1])

    # Method to change the visibility of the random cell
    def changeVisibilityRandom(self, coOrd1):
        self.actualGuesses += 2
        if coOrd1 != None:
            coOrd1 = coOrd1.upper()
            col1 = ord(coOrd1[0]) - 65
            row1 = ord(coOrd1[1]) - 48
            if not self.arr[row1][col1][0]:
                self.arr[row1][col1][0] = True
                self.visibleElements += 1
            return

        for x in range(self.size):
            for y in range(self.size):
                if not self.arr[x][y][0]:
                    self.arr[x][y][0] = True
                    self.visibleElements += 1
                    return
        return

    # Method to display all grid
    def changeVisibilityOfAll(self):
        for x in range(self.size):
            for y in range(self.size):
                self.arr[x][y][0] = True

        self.score = -1
        self.visibleElements = self.size * self.size

        return True

    def areAllElementsVisible(self):
        # print("visibleElements  ", self.visibleElements)
        return self.visibleElements == self.size * self.size

    # Method to calculate score
    def calcScore(self):
        if self.score == -1:
            return -1
        # if self.actualGuesses < self.minimumPossibleGuesses and self.visibleElements == self.size * self.size:
        #     return -2
        if self.visibleElements == 0 and self.actualGuesses == 0:
            return 0
        if self.visibleElements == self.size * self.size:
            return (self.minimumPossibleGuesses / self.actualGuesses) * 100
        return -100
