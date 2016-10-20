import sys
import os
import random
from datetime import datetime
from PyQt4 import QtCore, QtGui



path = os.path.join("/Users", "sophiewang", "face", "all")
blackPath = os.path.join("/Users", "sophiewang", "face", "black.jpg")
height = 1200

       
class Window(QtGui.QWidget):
    
    def __init__(self):
        super(Window, self).__init__()
        
        # randomize all image files
        self.images = os.listdir(path)
        random.shuffle(self.images)
        #print self.images
        
        self.setWindowTitle('IAPS images')
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        
        self.lbl = QtGui.QLabel(self)
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.blackPixmap = QtGui.QPixmap(blackPath)

        #self.scaledBlackPixmap = self.blackPixmap.scaled(screen.width(), screen.height(), QtCore.Qt.KeepAspectRatio)
        self.scaledBlackPixmap = self.blackPixmap.scaledToHeight(height)
        self.lbl.setPixmap(self.scaledBlackPixmap)
        
        hbox = QtGui.QHBoxLayout()
        btn = QtGui.QPushButton("Start")
        btn.clicked.connect(self.btnClicked)  
        hbox.addStretch(1)
        hbox.addWidget(btn)
        hbox.addStretch(1)
        
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.lbl)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        
        self.timer = QtCore.QTimer()   
        self.counter = 1

   
    def update(self):
        if self.counter % 2 == 0:
            self.displayRandomImage()

        else:
            self.lbl.setPixmap(self.scaledBlackPixmap)
            print '------------'
            print 'display black'
            print datetime.now().time()
        self.counter += 1

    def displayRandomImage(self):
        if self.images:
            imgName = self.images.pop()
            imgPath = os.path.join(path, imgName)
            imgPixmap = QtGui.QPixmap(imgPath)
            scaledImgPixmap = imgPixmap.scaledToHeight(height)
            self.lbl.setPixmap(scaledImgPixmap)
            print '------'
            print 'display image' + ' ' + str(imgName)
            print datetime.now().time()
        else:
            self.timer.stop()
            sys.exit()
        
        
    def btnClicked(self):

        print 'btn clicked'
        print datetime.now().time()
        
        self.displayRandomImage()
            
        self.timer.timeout.connect(self.update)
        self.timer.start(3000)


def main():
    app = QtGui.QApplication(sys.argv)
    window = Window()
    #window.show()
    window.showMaximized()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main() 