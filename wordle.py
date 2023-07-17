from Templates.MainWindow import Ui_Wordle, Ui_GameEnded
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from random import randint


class MainWindow(QtWidgets.QMainWindow, Ui_Wordle, Ui_GameEnded):
    def __init__(self, *args, obj=None, **kwargs,):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Wordle")

        with open('std_words.txt', 'r', encoding='utf-8') as f:
            self.wordlist = f.readlines()
            self.wordlist = [x.rstrip().upper() for x in self.wordlist]

        print(self.wordlist)

        self.hidden_word = self.wordlist[randint(0, len(self.wordlist)-1)]
        print(len(self.hidden_word))
        
        print("The hidden word is: ", self.hidden_word)


        self.row_1 = [self.element_11, self.element_12, self.element_13, self.element_14, self.element_15]
        self.row_2 = [self.element_21, self.element_22, self.element_23, self.element_24, self.element_25]
        self.row_3 = [self.element_31, self.element_32, self.element_33, self.element_34, self.element_35]
        self.row_4 = [self.element_41, self.element_42, self.element_43, self.element_44, self.element_45]
        self.row_5 = [self.element_51, self.element_52, self.element_53, self.element_54, self.element_55]
        self.row_6 = [self.element_61, self.element_62, self.element_63, self.element_64, self.element_65]

        self.rows = [self.row_1, self.row_2, self.row_3, self.row_4, self.row_5, self.row_6]

        self.actual_row = 1

        self.actualString = ''

        self.startButton.clicked.connect(self.newGame)


    def newGame(self):

        for element in self.rows:
            for i in range(len(element)):
                element[i].setText('')
                element[i].setStyleSheet("border: 2px solid rgb(58,58,60);\n"
                                                            "color: white;\n")
        
        self.actual_row = 1
        self.actualString = ''

        self.hidden_word = self.wordlist[randint(0, len(self.wordlist)-1)]

        print(self.hidden_word)




    def checkString(self):

        if not len(self.actualString) == 5:
            pass
        else:
            if self.isInWordlist():
                self.colorChars()
                if self.actualString == self.hidden_word:
                    print("Hai vinto!")
                    self.youWin()
                else:
                    if not self.actual_row == 6:
                        self.actual_row += 1
                        self.getActualString()
                    else:
                        self.gameEnded()
            else:
                pass
    
    def youWin(self):
        for element in self.rows[self.actual_row-1]:
                element.setStyleSheet("border: 2px solid rgb(83,141,78);\n"
                                                            "color: white;\n"
                                                            "background-color: rgb(83,141,78)")
    
    def gameEnded(self):
        dialog = QtWidgets.QDialog(self)
        ui_dialog = Ui_GameEnded()
        ui_dialog.setupUi(dialog)
        dialog.setWindowTitle("Game Ended")
        ui_dialog.hiddenWord.setText(self.hidden_word)
        ui_dialog.playAgain_Button.clicked.connect(self.newGame)
        ui_dialog.playAgain_Button.clicked.connect(dialog.close)

        dialog.exec_()


    def isInWordlist(self):

        if self.actualString in self.wordlist:
            for element in self.rows[self.actual_row-1]:

                element.setStyleSheet("border: 2px solid rgb(58,58,60);\n"
                                                            "color: white;\n"
                                                            "background-color: rgb(58,58,60)")
            return True
        else:
            for element in self.rows[self.actual_row-1]:

                element.setStyleSheet("border: 2px solid red;\n"
                                                            "color: white;\n"
                                                            "background-color: rgb(58,58,60)")
            return False
        
    def colorChars(self):
        chars = list(self.hidden_word)
        print(chars)
        for i in range(len(self.rows[self.actual_row-1])):
          
            if self.rows[self.actual_row-1][i].text() in chars[i]:
                # se l'elemento e' nella stessa posizione
                self.rows[self.actual_row-1][i].setStyleSheet("border: 2px solid rgb(83,141,78);\n"
                                                            "color: white;\n"
                                                            "background-color: rgb(83,141,78)")
            elif self.rows[self.actual_row-1][i].text() in chars:
                self.rows[self.actual_row-1][i].setStyleSheet("border: 2px solid rgb(181,112,59);\n"
                                                            "color: white;\n"
                                                            "background-color: rgb(181,112,59)")
    
    def getActualString(self):
         
        self.actualString = self.rows[self.actual_row - 1][0].text() + \
                            self.rows[self.actual_row - 1][1].text() + \
                            self.rows[self.actual_row - 1][2].text() + \
                            self.rows[self.actual_row - 1][3].text() + \
                            self.rows[self.actual_row - 1][4].text()


        #print(f"{self.actualString} - {len(self.actualString)}")
         
    def addChar(self, char):

        if not len(self.actualString) == 5:
            nextPos = len(self.actualString)
            self.rows[self.actual_row - 1][nextPos].setText(char)
            self.getActualString()

    def delChar(self):

        if not len(self.actualString) == 0:
            nextPos = len(self.actualString)
            self.rows[self.actual_row - 1][nextPos-1].setText('')
            self.rows[self.actual_row - 1][nextPos-1].setStyleSheet("border: 2px solid rgb(58,58,60);\n"
                                                            "color: white;\n"
                                                            )
            self.getActualString()


    def keyPressEvent(self, event):

        if event.key() == Qt.Key_A:
            self.addChar('A')

        elif event.key() == Qt.Key_B:
            self.addChar('B')

        elif event.key() == Qt.Key_C:
            self.addChar('C')

        elif event.key() == Qt.Key_D:
            self.addChar('D')

        elif event.key() == Qt.Key_E:
            self.addChar('E')

        elif event.key() == Qt.Key_F:
            self.addChar('F')

        elif event.key() == Qt.Key_G:
            self.addChar('G')

        elif event.key() == Qt.Key_H:
            self.addChar('H')

        elif event.key() == Qt.Key_I:
            self.addChar('I')

        elif event.key() == Qt.Key_J:
            self.addChar('J')

        elif event.key() == Qt.Key_K:
            self.addChar('K')

        elif event.key() == Qt.Key_L:
            self.addChar('L')

        elif event.key() == Qt.Key_M:
            self.addChar('M')

        elif event.key() == Qt.Key_N:
            self.addChar('N')

        elif event.key() == Qt.Key_O:
            self.addChar('O')

        elif event.key() == Qt.Key_P:
            self.addChar('P')

        elif event.key() == Qt.Key_Q:
            self.addChar('Q')

        elif event.key() == Qt.Key_R:
            self.addChar('R')

        elif event.key() == Qt.Key_S:
            self.addChar('S')

        elif event.key() == Qt.Key_T:
            self.addChar('T')

        elif event.key() == Qt.Key_U:
            self.addChar('U')

        elif event.key() == Qt.Key_V:
            self.addChar('V')

        elif event.key() == Qt.Key_W:
            self.addChar('W')

        elif event.key() == Qt.Key_X:
            self.addChar('X')

        elif event.key() == Qt.Key_Y:
            self.addChar('Y')

        elif event.key() == Qt.Key_Z:
            self.addChar('Z')      
        
        elif event.key() == Qt.Key_Backspace:
            self.delChar()

        elif event.key() == Qt.Key_Return:
            self.checkString()





        
    



app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()

