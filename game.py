from grid import MyGrid
import sys
import time
import os

class MyGame:

    myGrid = None
    choice = None
    size = None
    inputEnabled = True
    isScoreVisible = False
    def displayGameName(self):
        os.system("clear")
        print("––––––––––––––––––")
        print("|   PEEK-A-BOO   |")
        print("––––––––––––––––––")

    def __init__(self):
        self.size = int(sys.argv[1])
        self.myGrid = MyGrid(self.size)
        if not self.myGrid.isValidSize:
            sys.exit()
        self.displayGameName()
        self.gameLogic(None)

    def gameLogic(self, str):
        # os.system("clear")
        self.displayGameName()
        score = self.myGrid.calcScore()
        self.myGrid.displayGrid()

        if str != None:
            print(str)

        if self.myGrid.areAllElementsVisible() and score >= 0:
            print('\n Your score is {0:.3g} \n'.format(score))
            self.isScoreVisible = True
        elif score == -2:
            print('\nYour score is {}\n'.format(0))

        if self.myGrid.areAllElementsVisible():
            print("\nAll elements are uncovered! Only choice 4 and 5 are eligible\n")

        self.displayMenu()

    def displayMenu(self):
        print("1. Let me select two elements")
        print("2. Uncover one element for me")
        print("3. I give up - reveal the grid")
        print("4. New game")
        print("5. Exit")

        if not self.inputEnabled:
            return

        self.choice = input("\nSelect: ")

        match self.choice:
            case "1":
                return self.choice1()
            case "2":
                return self.choice2()
            case "3":
                return self.choice3()
            case "4":
                return self.choice4()
            case "5":
                return self.choice5()
            case _:
                return self.gameLogic("Invalid input")


    def choice1(self):
        if self.myGrid.areAllElementsVisible():
            return self.gameLogic(None)

        coOrd1 = self.getValidCellEntry()
        coOrd2 = self.getValidCellEntry()

        if coOrd1 == coOrd2:
            print("\nInput error: enter different cell coordinates\n")
            return self.choice1()

        col1, row1, col2, row2, flag = self.myGrid.changeVisibility(coOrd1, coOrd2)

        if self.myGrid.score < 0:
            return self.gameLogic(None)
        elif col1 == -1:
            return self.gameLogic("\nElements are already visible!\n")

        if not flag:
            self.inputEnabled = False
            self.gameLogic(None)
            time.sleep(2)

        self.inputEnabled = True
        return self.gameLogic(None)

    def choice2(self):
        if self.myGrid.areAllElementsVisible():
            return self.gameLogic(None)
        self.myGrid.changeVisibilityRandom()
        return self.gameLogic(None)

    def choice3(self):
        if self.myGrid.areAllElementsVisible():
            return self.gameLogic(None)
        self.myGrid.changeVisibilityOfAll()
        return self.gameLogic("\nYou cheated - Loser!. You're score is 0!\n")

    def choice4(self):
        score = self.myGrid.calcScore()
        if (score > -1) and not self.isScoreVisible:
            print('\nYour Score is {0:.3g} \n'.format(score))
            time.sleep(2)
        elif not self.myGrid.areAllElementsVisible():
            print("\nScore not available as game was not finished!")
            time.sleep(2)
        self.myGrid = MyGrid(self.size)
        return self.gameLogic(None)

    def choice5(self):
        if self.myGrid.score >= 0:
            score = self.myGrid.calcScore()
            if(score > -1) and not self.isScoreVisible:
                print('\n Your Score is {0:.3g} \n'.format(score))
            else:
                print("\nScore is not available as game was not finished!")
        print("Thank you for playing!")
        sys.exit()
        return

    def getValidCellEntry(self):
        coOrd1 = input("Enter cell coordinates (e.g., a0): ")
        if not self.myGrid.validateCell(coOrd1):
            return self.getValidCellEntry()
        return coOrd1


myGame = MyGame()