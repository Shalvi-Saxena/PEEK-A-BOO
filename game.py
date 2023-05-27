from grid import MyGrid
import sys
import time
import os

class MyGame:

    # size - size of the grid
    # inputEnabled - enable input for user
    # isGameFinished - check if all elements are visible or not
    myGrid = None
    choice = None
    size = None
    inputEnabled = True
    isGameFinished = False

    # Method to display game name
    def displayGameName(self):
        os.system("clear")
        print("––––––––––––––––––")
        print("|   PEEK-A-BOO   |")
        print("––––––––––––––––––")

    # Method to initialize Game
    def __init__(self):
        self.size = int(sys.argv[1])
        self.myGrid = MyGrid(self.size)
        if not self.myGrid.isValidSize:
            sys.exit()
        self.gameLogic(None)

    # Method to display Game grid, score and menu relevant to the use case
    def gameLogic(self, str):
        # os.system("clear")
        self.displayGameName()
        score = self.myGrid.calcScore()
        self.myGrid.displayGrid()

        # print("score  ", score)

        if str != None:
            print(str)

        if self.myGrid.areAllElementsVisible() and score >= 0:
            print('\n Your score is {0:.3g} \n'.format(score))
            self.isGameFinished = True
        elif score == -2:
            print('\nYour score is {}\n'.format(0))
        elif score == -1:
            print('\nYou cheated - Loser!. Your score is 0!\n')

        if self.myGrid.areAllElementsVisible():
            print("\nAll elements are uncovered! Only choice 4 and 5 are eligible\n")

        self.displayMenu()

    # Method to display Menu
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
                return self.gameLogic("\nInvalid input - Please enter a valid choice\n")

    # Method to run choice1
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

    # Method to run choice2
    def choice2(self):
        if self.myGrid.areAllElementsVisible():
            return self.gameLogic(None)
        isRandom = input("\nEnter 1 if you want to pass cell coordinates: ")
        if isRandom == "1":
            coOrd1 = self.getValidCellEntry()
            self.myGrid.changeVisibilityRandom(coOrd1)
        else:
            self.myGrid.changeVisibilityRandom(None)
        return self.gameLogic(None)

    # Method to run choice3
    def choice3(self):
        if self.myGrid.areAllElementsVisible():
            return self.gameLogic(None)
        self.myGrid.changeVisibilityOfAll()
        return self.gameLogic(None)

    # Method to choice4
    def choice4(self):
        score = self.myGrid.calcScore()
        if (score > -1) and not self.isGameFinished:
            print('\nYour Score is {0:.3g} \n'.format(score))
            time.sleep(2)
        elif not self.myGrid.areAllElementsVisible():
            print("\nScore not available as game was not finished!")
            time.sleep(2)
        self.myGrid = MyGrid(self.size)
        return self.gameLogic(None)

    # Method to run choice5
    def choice5(self):
        if self.myGrid.score >= 0:
            score = self.myGrid.calcScore()
            if(score > -1) and not self.isGameFinished:
                print('\n Your Score is {0:.3g} \n'.format(score))
            elif not self.myGrid.areAllElementsVisible():
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