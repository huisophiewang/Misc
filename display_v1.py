#!/usr/bin/env python

# embedding_in_qt4.py --- Simple Qt4 application embedding matplotlib canvases
#
# Copyright (C) 2005 Florent Rougon
#               2006 Darren Dale
#
# This file is an example program for matplotlib. It may be used and
# modified with no restriction; raw copies as well as modified versions
# may be distributed without limitation.

from __future__ import unicode_literals
import sys
import os
import random
import time
from datetime import datetime
from matplotlib.backends import qt4_compat
use_pyside = qt4_compat.QT_API == qt4_compat.QT_API_PYSIDE
if use_pyside:
    from PySide import QtGui, QtCore
else:
    from PyQt4 import QtGui, QtCore

from numpy import arange, sin, pi
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

progname = os.path.basename(sys.argv[0])
progversion = "0.1"


path = os.path.join("C:/", "Users", "Sophie", "face", "positive", "all")
files = os.listdir(path)


class MyDynamicMplCanvas(FigureCanvas):
    """A canvas that updates itself every second with a new plot."""
    def __init__(self, parent=None):
        #plt.rcParams['toolbar'] = 'None'

        self.fig = plt.figure()
        plt.axis('off')
        self.fig.frameon = False
        #subplot = fig.add_subplot(111)
        

        self.subplot = self.fig.add_subplot(111)
        
        # We want the axes cleared every time plot() is called
        #self.axes.hold(False)


        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        
        
        timer = QtCore.QTimer(self)
        self.black_image()
        
        timer.timeout.connect(self.update_image)
        timer.start(6000)



    def update_image(self):
        print 'start----------------------'
        print datetime.now().time()
        img_name = random.choice(files)
        print datetime.now().time()
        img_path = os.path.join(path, img_name)
        print datetime.now().time()
        img = mpimg.imread(img_path)
        print datetime.now().time()
        self.subplot.imshow(img)
        print datetime.now().time()
        self.draw()
        print datetime.now().time()
        time.sleep(3)
        print '--------------'
        print datetime.now().time()
        self.black_image()
        print datetime.now().time()
        print 'end-----------------------------'
        
    def black_image(self):
        img_path = os.path.join("C:/", "Users", "Sophie", "face", "black.jpg")
        print datetime.now().time()
        img = mpimg.imread(img_path)
        print datetime.now().time()
        self.subplot.imshow(img)
        print datetime.now().time()
        self.draw()

class ApplicationWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("application main window")

        self.file_menu = QtGui.QMenu('&File', self)
        self.file_menu.addAction('&Quit', self.fileQuit,
                                 QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu)

        self.help_menu = QtGui.QMenu('&Help', self)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)

        self.help_menu.addAction('&About', self.about)

        self.main_widget = QtGui.QWidget(self)

        l = QtGui.QVBoxLayout(self.main_widget)
        #sc = MyStaticMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        dc = MyDynamicMplCanvas(self.main_widget)
        #l.addWidget(sc)
        l.addWidget(dc)

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)
        #self.showFullScreen()
        self.showMaximized()


    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()

    def about(self):
        QtGui.QMessageBox.about(self, "About",
"""embedding_in_qt4.py example
Copyright 2005 Florent Rougon, 2006 Darren Dale

This program is a simple example of a Qt4 application embedding matplotlib
canvases.

It may be used and modified with no restriction; raw copies as well as
modified versions may be distributed without limitation."""
)


qApp = QtGui.QApplication(sys.argv)

aw = ApplicationWindow()
aw.setWindowTitle("%s" % progname)
aw.show()
sys.exit(qApp.exec_())
#qApp.exec_()