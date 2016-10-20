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

IMAGE_PATH = os.path.join(ASSET_PATH, "neutral.jpg")
QUESTION_PATH = os.path.join(ASSET_PATH, "math.xlsx")

AUDIO_PATH = os.path.join(ASSET_PATH, 'audio')

COUNTDOWN_EASY = 20
COUNTDOWN_MEDIUM = 30
COUNTDOWN_HARD = 40


TOTAL_SCORE = 760
EACH_SCORE = 20

 
class Window(QtGui.QWidget):
    
    def __init__(self):
        
        self.initUI()
        
        self.readXls(QUESTION_PATH)
        
        self.setTimers()



    def initUI(self):
        super(Window, self).__init__()
        
        self.setWindowTitle('Trivia')
        self.resize(800, 600)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        
        self.imagelbl = QtGui.QLabel(self)
        self.imagelbl.setAlignment(QtCore.Qt.AlignCenter)
        facePixmap = QtGui.QPixmap(IMAGE_PATH)
        self.imagelbl.setPixmap(facePixmap)
        #self.imagelbl.hide()
        
        
        self.clock = QtGui.QLabel(self)
        self.clock.setStyleSheet('color: red; font-size: 24pt')
        self.clock.setFixedHeight(50)
        self.clock.hide()
        
        self.scorelblTxt = 'Highest Score: {highScore}<br>Your Score: {userScore}'.format(highScore=str(TOTAL_SCORE), userScore=str(TOTAL_SCORE))
        self.scorelbl = QtGui.QLabel(self.scorelblTxt)
        self.scorelbl.setStyleSheet('color: red; font-size: 18pt')
        self.scorelbl.setFixedHeight(50)
        self.scorelbl.hide()
        
        infoLayout = QtGui.QHBoxLayout()
        infoLayout.addWidget(self.scorelbl)
        infoLayout.addStretch(1)
        infoLayout.addWidget(self.clock)
       
        upper = QtGui.QVBoxLayout()
        upper.addLayout(infoLayout)
        upper.addWidget(self.imagelbl)

          
#         self.questionlbl = QtGui.QLabel()
#         self.questionlbl.setWordWrap(True)              
        self.questionlbl = QTextEdit(self)
        self.questionlbl.setReadOnly(True)
        self.questionlbl.hide()
        self.questionlbl.setTextColor(QColor(0, 0, 255))
        self.questionlbl.setFixedHeight(50)
        
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
        self.btn = QtGui.QPushButton("Next")
        self.btn.clicked.connect(self.btnClicked)  
        self.btn.hide()
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
        self.qCount = 0
        
        book = xlrd.open_workbook(path)
        sh = book.sheet_by_index(0)
        self.numquestions = sh.nrows
        
        print 'num of questions:'
        print sh.nrows
        
        for rx in range(sh.nrows):
            row = sh.row_values(rx)
            #print row
            self.questions.append(row)

    def setTimers(self):
        # timer for conversation (simulate hand typing)
        self.cnvsTimer = QtCore.QTimer()  
        self.cnvsTimer.timeout.connect(self.converse)
        
        # timer for the clock (each questionlbl has count down time)
        self.cntdTimer = QtCore.QTimer()
        self.cntdTimer.timeout.connect(self.countdown)
        
        # timer for fade out
        self.fdTimer = QtCore.QTimer()
        self.fdTimer.timeout.connect(self.fade)
        
        self.cmtTimer = QtCore.QTimer()
        self.cmtTimer.timeout.connect(self.comment)

    def converse(self): 
   
        if self.wdCount < 1:     
            self.wdCount += 1
        else:   
            #time.sleep(3)  

            #lines = self.questions[self.current][0]
            #voiceCmd = 'say ' + lines
            print self.current
            
            voiceCmd = r'say "Hello"'
          
#             audioFile = 'Lauren' + str(int(lines)) + '.wav'
#             voiceCmd = r'afplay "%s"' % os.path.join(AUDIO_PATH, audioFile)
            
            os.system(voiceCmd)
                   
            self.cnvsTimer.stop()
            self.next(self.current+1)

                
                 
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

    def comment(self):
        
        if self.cmtCount < 1:
            self.cmtCount += 1
        else:
            #time.sleep(2)
            
#             if self.imagelbl.isHidden():
#                 self.imagelbl.show()
            
            
            print '-----'
            print self.current
            rightAns = int(self.questions[self.current][6])
            print rightAns
            
            userAns = 0
            if self.btn1.isChecked():
                userAns = 1
            elif self.btn2.isChecked():
                userAns = 2
            elif self.btn3.isChecked():
                userAns = 3
            elif self.btn4.isChecked():
                userAns = 4
    
            if userAns == rightAns:
                voiceCmd = r'say "Good Job!"' 
            else:
                voiceCmd = r'say "Wrong!"' 
            
            os.system(voiceCmd)
            print voiceCmd
            
            self.cmtTimer.stop()
            
            self.next(self.current+1)

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Space:
            print 'space pressed'

            self.next(0) 

    def next(self, next): 
        

        self.current = next
        

        # not the end of session  
        if self.current < self.numquestions:
            # clear the questionlbl window before display lines
            self.questionlbl.setText('')
            # display lines
            if not self.questions[self.current][1]:
                #print str(self.current) + ' lines'
                
                self.btn1.hide()
                self.btn2.hide()
                self.btn3.hide()
                self.btn4.hide()
                self.btn.hide()
                
                self.clock.hide()
                self.scorelbl.hide()
                self.questionlbl.hide()
        
                
#                 lines = self.questions[self.current][0]
#                 voiceCmd = 'say ' + lines
#                 print voiceCmd
#                 os.system(voiceCmd)
                
                #time.sleep(3)

                self.wdCount = 0
                self.cnvsTimer.start(100)
           
                
            # display questionlbl
            else:   
                
                self.imagelbl.hide()
                
                if self.questionlbl.isHidden():
                    self.questionlbl.show()
         
                      
                self.questionlbl.setText('What is ' + str(self.questions[self.current][0]) + '?')
                
                self.btn1.setText(str(int(self.questions[self.current][1])))
                self.btn1.setCheckable(False)
                self.btn1.setCheckable(True)
                self.btn1.show()
                
                self.btn2.setText(str(int(self.questions[self.current][2])))
                self.btn2.setCheckable(False)
                self.btn2.setCheckable(True)
                self.btn2.show()
                
                self.btn3.setText(str(int(self.questions[self.current][3])))
                self.btn3.setCheckable(False)
                self.btn3.setCheckable(True)
                self.btn3.show()
                
                self.btn4.setText(str(int(self.questions[self.current][4])))
                self.btn4.setCheckable(False)
                self.btn4.setCheckable(True)
                self.btn4.show()
                
                self.btn.setText("Next")
                self.btn.show()
                
                self.clock.show()
                if self.questions[self.current][5] == 'E':
                    self.cntdCount = COUNTDOWN_EASY
                elif self.questions[self.current][5] == 'M':
                    self.cntdCount = COUNTDOWN_MEDIUM
                    self.qCount += 1
                elif self.questions[self.current][5] == 'H':
                    self.cntdCount = COUNTDOWN_HARD
                    self.qCount += 1
                
                
                currentScore = TOTAL_SCORE - EACH_SCORE*(self.qCount)
                self.scorelblTxt = 'Highest Score: {highScore}<br>Your Score: {userScore}'.format(highScore=str(TOTAL_SCORE), userScore=str(currentScore))
                self.scorelbl.setText(self.scorelblTxt)
                self.scorelbl.show()
                
                
                self.cntdTimer.start(500)
                
                
                
                
        # end of session
#         elif self.current == self.numquestions :
#             self.questionlbl.setText(str(self.questions[self.current][0]) )
#             self.btn1.hide()
#             self.btn2.hide()
#             self.btn3.hide()
#             self.btn4.hide()
#             self.btn.hide()
#             self.clock.hide()

    def btnClicked(self): 
        

        if self.btn1.isChecked() or self.btn2.isChecked() or self.btn3.isChecked() or self.btn4.isChecked():
            # stop fade timer and countdown timer
            if self.fdTimer.isActive():
                self.fdTimer.stop()
            if self.cntdTimer.isActive():
                self.cntdTimer.stop()
            
            #self.next(self.current+1)
            
            self.btn1.hide()
            self.btn2.hide()
            self.btn3.hide()
            self.btn4.hide()
            self.btn.hide()
            
            self.clock.hide()
            self.scorelbl.hide()
            self.questionlbl.hide()
            
            self.cmtCount = 0
            self.cmtTimer.start(100)
        else:
            QtGui.QMessageBox.about(self, "Message", "Please select one answer before going to the next question.")




       
def main():
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main() 