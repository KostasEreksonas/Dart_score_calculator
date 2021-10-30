#!/usr/bin/env python3

# Filename: Graphical_dart_scoreboard_v_0_2.py

# Dependencies: Python3, PyQt5.QtCore, PyQt5.QtWidgets

__version__ = "0.2"
__author__ = "Kostas Ereksonas"

#  ---------
# | Imports |
#  ---------

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QPushButton

#  ---------
# | Classes |
#  ---------
"""In this section I will define classes for the program"""

#  --------------
# | Calculations |
#  --------------
class calculateResults():
    def __init__(self, score):
        self.score = score

    def count100(self, c100):
        if (self.score >= 100) and (self.score < 140):
            c100 += 1
        return c100

    def count140(self, c140):
        if (self.score >= 140) and (self.score < 179):
            c140 += 1
        return c140

    def count180(self, c180):
        if (self.score == 180):
            c180 += 1
        return c180

    def countLeg(self, leg):
        if (self.score == 0):
            leg += 1
        return leg

    def countSet(legCurrent, legWin, sets):
        if (legCurrent == legWin):
            sets1 += 1
        return sets

    def pointsLeft(self, points):
        points -= self.score
        return points


#  ------------
# | User Input |
#  ------------
class userInput():
    def __init__(self):
        self.player1 = player1
        self.player2 = player2

    def namePlayer1(player1):
        player1 = input("Enter name of player 1:")
        return player1

    def namePlayer2(player2):
        player2 = input("Enter name of player 2:")
        return player2

    def legCount(legNumber):
        legNumber = input("Number of legs to play:")
        return legNumber

    def legCount(setNumber):
        setNumber = input("Number of sets to play:")
        return setNumber


#  -------------
# | Main Window |
#  -------------
class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createWindow()
        self.startButton()

    def createWindow(self):
        self.setWindowTitle("Dart Scoreboard")
        self.setFixedSize(400, 450)
        self.generalLayout = QVBoxLayout()
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.generalLayout)
        self.heading = QLineEdit()
        self.heading.setFixedHeight(35)
        self.heading.setAlignment(Qt.AlignCenter)
        self.heading.setText("Dart scoreboard")
        self.heading.setReadOnly(True)
        self.generalLayout.addWidget(self.heading)
        calc = calculateResults(101)
        displayText = ["", "Player1", "Player2", "Sets won", calc.countSet(0,0), calc.countSet(0,0), "Legs won", calc.countLeg(0), calc.countLeg(0), "Points left", calc.pointsLeft(0), calc.pointsLeft(0), "Points scored", "0", "0", "100+", calc.count100(0), calc.count100(0), "140+", calc.count140(0), calc.count140(0), "180s", calc.count180(0), calc.count180(0), "Max score", "0", "0","Average score", "0", "0"]
        displayBoxes = []
        for i in range(len(displayText)//3+1):
            for j in range(3):
                self.textBox = QLineEdit()
                self.boxLayout = QHBoxLayout()
                self.textBox.setFixedHeight(35)
                self.textBox.setReadOnly(True)
                if i == 1:
                    displayBoxes.append(self.textBox)
                    self.textBox.setText(displayText[j])
                    for l in range(len(displayBoxes)):
                        self.boxLayout.addWidget(displayBoxes[l])
                    self.generalLayout.addLayout(self.boxLayout)
                if i == 2:
                    displayBoxes.append(self.textBox)
                    self.textBox.setText(str(displayText[j+3]))
                    for l in range(len(displayBoxes)-3):
                        self.boxLayout.addWidget(displayBoxes[l+3])
                    self.generalLayout.addLayout(self.boxLayout)
                if i == 3:
                    displayBoxes.append(self.textBox)
                    self.textBox.setText(str(displayText[j+6]))
                    for l in range(len(displayBoxes)-6):
                        self.boxLayout.addWidget(displayBoxes[l+6])
                    self.generalLayout.addLayout(self.boxLayout)
                if i == 4:
                    displayBoxes.append(self.textBox)
                    self.textBox.setText(str(displayText[j+9]))
                    for l in range(len(displayBoxes)-9):
                        self.boxLayout.addWidget(displayBoxes[l+9])
                    self.generalLayout.addLayout(self.boxLayout)
                if i == 5:
                    displayBoxes.append(self.textBox)
                    self.textBox.setText(str(displayText[j+12]))
                    for l in range(len(displayBoxes)-12):
                        self.boxLayout.addWidget(displayBoxes[l+12])
                    self.generalLayout.addLayout(self.boxLayout)
                if i == 6:
                    displayBoxes.append(self.textBox)
                    self.textBox.setText(str(displayText[j+15]))
                    for l in range(len(displayBoxes)-15):
                        self.boxLayout.addWidget(displayBoxes[l+15])
                    self.generalLayout.addLayout(self.boxLayout)
                if i == 7:
                    displayBoxes.append(self.textBox)
                    self.textBox.setText(str(displayText[j+18]))
                    for l in range(len(displayBoxes)-18):
                        self.boxLayout.addWidget(displayBoxes[l+18])
                    self.generalLayout.addLayout(self.boxLayout)
                if i == 8:
                    displayBoxes.append(self.textBox)
                    self.textBox.setText(str(displayText[j+21]))
                    for l in range(len(displayBoxes)-21):
                        self.boxLayout.addWidget(displayBoxes[l+21])
                    self.generalLayout.addLayout(self.boxLayout)
                if i == 9:
                    displayBoxes.append(self.textBox)
                    self.textBox.setText(str(displayText[j+24]))
                    for l in range(len(displayBoxes)-24):
                        self.boxLayout.addWidget(displayBoxes[l+24])
                    self.generalLayout.addLayout(self.boxLayout)
                if i == 10:
                    displayBoxes.append(self.textBox)
                    self.textBox.setText(str(displayText[j+27]))
                    for l in range(len(displayBoxes)-27):
                        self.boxLayout.addWidget(displayBoxes[l+27])
                    self.generalLayout.addLayout(self.boxLayout)

    def startButton(self):
        self.dialogOpen = QPushButton()
        self.dialogOpen.setText("Start game")
        self.dialogOpen.clicked.connect(self.callDialog)
        self.generalLayout.addWidget(self.dialogOpen)

    def callDialog(self):
        self.Dialog = dialogWindow().exec_()


#  ---------------
# | Dialog window |
#  ---------------
class dialogWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Start of the game")
        self.setFixedSize(280,200)
        self.generalLayout = QVBoxLayout()
        self.centralWidget = QWidget(self)
        self.centralWidget.setLayout(self.generalLayout)
        self.inputFields()
        self.dialogButtons()

    def inputFields(self):
        Labels = ["First player name", "Second player name", "Number of sets to play", "Number of legs to play", "Number of points to score"]

        self.inputField1 = QHBoxLayout()
        self.inputField_Label_1 = QLabel()
        self.inputField_Label_1.setText(Labels[0])
        self.inputField_Data_1 = QLineEdit()
        self.inputField1.addWidget(self.inputField_Label_1)
        self.inputField1.addWidget(self.inputField_Data_1)
        self.generalLayout.addLayout(self.inputField1)

        self.inputField2 = QHBoxLayout()
        self.inputField_Label_2 = QLabel()
        self.inputField_Label_2.setText(Labels[1])
        self.inputField_Data_2 = QLineEdit()
        self.inputField2.addWidget(self.inputField_Label_2)
        self.inputField2.addWidget(self.inputField_Data_2)
        self.generalLayout.addLayout(self.inputField2)

        self.inputField3 = QHBoxLayout()
        self.inputField_Label_3 = QLabel()
        self.inputField_Label_3.setText(Labels[2])
        self.inputField_Data_3 = QLineEdit()
        self.inputField3.addWidget(self.inputField_Label_3)
        self.inputField3.addWidget(self.inputField_Data_3)
        self.generalLayout.addLayout(self.inputField3)

        self.inputField4 = QHBoxLayout()
        self.inputField_Label_4 = QLabel()
        self.inputField_Label_4.setText(Labels[3])
        self.inputField_Data_4 = QLineEdit()
        self.inputField4.addWidget(self.inputField_Label_4)
        self.inputField4.addWidget(self.inputField_Data_4)
        self.generalLayout.addLayout(self.inputField4)

        self.inputField5 = QHBoxLayout()
        self.inputField_Label_5 = QLabel()
        self.inputField_Data_5 = QLineEdit()
        self.inputField_Label_5.setText(Labels[4])
        self.inputField5.addWidget(self.inputField_Label_5)
        self.inputField5.addWidget(self.inputField_Data_5)
        self.generalLayout.addLayout(self.inputField5)

    def dialogButtons(self):
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.generalLayout.addWidget(self.buttonBox)


def main():
    """Main function."""
    scoreboard = QApplication(sys.argv)
    view = mainWindow()
    view.show()
    dialog = dialogWindow()
    sys.exit(scoreboard.exec_())

if __name__ == "__main__":
    main()
