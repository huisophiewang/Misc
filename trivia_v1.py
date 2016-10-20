import sys
import os
import time
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QTextEdit, QColor
import xlrd

if sys.platform == "win32":
    ASSET_PATH = os.path.join("C:/", "Users", "Sophie", "Google Drive", "Courses", "Affective Computing", "code")
else:
    ASSET_PATH = os.path.join("/Users", "sophiewang", "Google Drive", "Courses", "Affective Computing", "code")

FACE_PATH = os.path.join(ASSET_PATH, "iMadeFace.jpg")
questionlbl_PATH = os.path.join(ASSET_PATH, "questions.xlsx")

COUNTDOWN_EASY = 20
COUNTDOWN_MEDIUM = 15
COUNTDOWN_HARD = 10


                        
class Window(QtGui.QWidget):
    
    def __init__(self):
        
        self.initUI()
        
        self.readXls(questionlbl_PATH)
        
        self.setTimers()



    def initUI(self):
        super(Window, self).__init__()
        
        self.setWindowTitle('Trivia')
        self.resize(800, 600)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        
        self.imagelbl = QtGui.QLabel(self)
        self.imagelbl.setAlignment(QtCore.Qt.AlignCenter)
        facePixmap = QtGui.QPixmap(FACE_PATH)
        self.imagelbl.setPixmap(facePixmap)
        
        self.clock = QtGui.QLabel(self)
        self.clock.setStyleSheet('color: red; font-size: 24pt')
        self.clock.setFixedHeight(50)
        self.clock.hide()
        
        clockLayout = QtGui.QHBoxLayout()
        clockLayout.addStretch(1)
        clockLayout.addWidget(self.clock)
        clockLayout.addStretch(1)

        
        upper = QtGui.QVBoxLayout()
        upper.addLayout(clockLayout)
        upper.addWidget(self.imagelbl)

          
#         self.questionlbl = QtGui.QLabel()
#         self.questionlbl.setWordWrap(True)              
        self.questionlbl = QTextEdit(self)
        self.questionlbl.setReadOnly(True)
        self.questionlbl.hide()
        self.questionlbl.setTextColor(QColor(0, 0, 255))
        self.questionlbl.setFixedHeight(100)
        
        self.answers = QtGui.QGridLayout()
        self.btn1 = QtGui.QRadioButton()
        self.btn1.hide()
        self.btn2 = QtGui.QRadioButton()
        self.btn2.hide()
        self.btn3 = QtGui.QRadioButton()
        self.btn3.hide()
        self.btn4 = QtGui.QRadioButton()
        self.btn4.hide()
        self.answers.addWidget(self.btn1, 1, 1)
        self.answers.addWidget(self.btn2, 1, 2)
        self.answers.addWidget(self.btn3, 2, 1)
        self.answers.addWidget(self.btn4, 2, 2)
        
        middle = QtGui.QVBoxLayout()
        middle.addWidget(self.questionlbl)
        middle.addLayout(self.answers)

        bottom = QtGui.QHBoxLayout()
        self.btn = QtGui.QPushButton("Start")
        self.btn.clicked.connect(self.btnClicked)  
        bottom.addStretch(1)
        bottom.addWidget(self.btn)
        bottom.addStretch(1)
        
        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(upper)
        vbox.addLayout(middle)
        vbox.addLayout(bottom)
        self.setLayout(vbox)
        
              
    def readXls(self, path):
        self.questions = []
        self.current = 0
        
        book = xlrd.open_workbook(path)
        sh = book.sheet_by_index(0)
        self.numquestions = sh.nrows
        
        print 'num of questions:'
        print sh.nrows
        
        for rx in range(sh.nrows):
            row = sh.row_values(rx)
            print row
            self.questions.append(row)

    def setTimers(self):
        # timer for conversation (simulate hand typing)
        self.cnvsTimer = QtCore.QTimer()  
        self.cnvsTimer.timeout.connect(self.updateTxt)
        
        # timer for the clock (each questionlbl has count down time)
        self.cntdTimer = QtCore.QTimer()
        self.cntdTimer.timeout.connect(self.countdown)
        
        # timer for fade out
        self.fdTimer = QtCore.QTimer()
        self.fdTimer.timeout.connect(self.fade)

    def updateTxt(self): 
   
        if self.countWord == len(self.words):
            time.sleep(1)
            self.cnvsTimer.stop()
            self.next(self.current+1)
        else:            
            word = self.words[self.countWord]  
            display = ''
   
            # end of a line, pause longer
            if word[1] == 0 and word[0] != 0:
                time.sleep(0.4)
    
            self.countWord += 1
                
            words = self.words[:self.countWord]
            for word in words:
                display = display + ' ' + word[2]
            

            self.questionlbl.setText(display)

                
                 
    def countdown(self):
        if self.cntdCount > 0:
            
            self.clock.setText(str(self.cntdCount))
            self.cntdCount -= 1
        else:
            self.cntdTimer.stop()
            self.next(self.current+1)
            
    def fade(self):
        if self.fdCount < 11:
            newAlpha = 255-self.fdCount*25
            self.questionlbl.setTextColor(QColor(0, 0, 255, newAlpha))
            self.questionlbl.setText(self.questions[self.current][0])    
            self.fdCount += 1
        else:
            self.fdTimer.stop()



    def next(self, next): 
        
        
        if self.questionlbl.isHidden():
            self.questionlbl.show()

        if self.questionlbl.textColor().alpha() != 255:
            self.questionlbl.setTextColor(QColor(0, 0, 255, 255))
    
        self.current = next
        

        # not end of session  
        if self.current < self.numquestions:
            # clear the questionlbl window before display lines
            self.questionlbl.setText('')
            # display lines
            if not self.questions[self.current][1]:
                self.lines = self.questions[self.current][0].splitlines()
                #print self.lines
                self.words = []
                for i in range(len(self.lines)):
                    line = self.lines[i]
                    words = line.split()
                    for j in range(len(words)):
                        self.words.append((i, j, words[j]))
                
                self.clock.hide()
                self.btn1.hide()
                self.btn2.hide()
                self.btn3.hide()
                self.btn4.hide()
                self.btn.hide()
                
                self.countWord = 0
                self.counter = 0
                self.cnvsTimer.start(150)
            # display questionlbl
            else:                
                if self.questions[self.current][7] == 'fade':
                    self.fdCount = 0
                    self.fdTimer.start(200)
                else:

                    self.questionlbl.setText(self.questions[self.current][0])
                
                self.btn1.setText(self.questions[self.current][1])
                self.btn1.setCheckable(False)
                if not self.questions[self.current][6] == 'uncheckable':
                    self.btn1.setCheckable(True)
                self.btn1.show()
                
                self.btn2.setText(self.questions[self.current][2])
                self.btn2.setCheckable(False)
                if not self.questions[self.current][6] == 'uncheckable':
                    self.btn2.setCheckable(True)
                self.btn2.show()
                
                self.btn3.setText(self.questions[self.current][3])
                self.btn3.setCheckable(False)
                if not self.questions[self.current][6] == 'uncheckable':
                    self.btn3.setCheckable(True)
                self.btn3.show()
                
                self.btn4.setText(self.questions[self.current][4])
                self.btn4.setCheckable(False)
                if not self.questions[self.current][6] == 'uncheckable':
                    self.btn4.setCheckable(True)
                self.btn4.show()
                
                self.btn.setText("Next")
                self.btn.show()
                
                self.clock.show()
                if self.questions[self.current][5] == 'E':
                    self.cntdCount = COUNTDOWN_EASY
                elif self.questions[self.current][5] == 'M':
                    self.cntdCount = COUNTDOWN_MEDIUM
                elif self.questions[self.current][5] == 'H':
                    self.cntdCount = COUNTDOWN_HARD
                self.cntdTimer.start(500)
                
                
                
                
        # end of session
        elif self.current == self.numquestions:
            #self.questionlbl.setText("Oh, apparently you know nothing!")
            self.btn1.hide()
            self.btn2.hide()
            self.btn3.hide()
            self.btn4.hide()
            self.btn.hide()
            self.clock.hide()

    def btnClicked(self):
        
        if self.btn.text() == "Start":

            self.next(0)
                      
        else:
            if self.btn1.isChecked() or self.btn2.isChecked() or self.btn3.isChecked() or self.btn4.isChecked():
                # stop fade timer and countdown timer
                if self.fdTimer.isActive():
                    self.fdTimer.stop()
                if self.cntdTimer.isActive():
                    self.cntdTimer.stop()
                    
                self.next(self.current+1)
            else:
                QtGui.QMessageBox.about(self, "Message", "Please select one answer before going to the next question.")

       
def main():
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main() 