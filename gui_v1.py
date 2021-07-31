#!/usr/bin/python3

#import libraries for GUI
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

#define GUI
class GUI(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'WEATHER CHANNEL'
        self.width = 400
        self.height = 300
        self.left = 100
        self.top = 100
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        start-button = QPushButton('Start Recording', self)
        start-button.setToolTip('Start Button')
        start-button.move(150,100)
        start-button.clicked.connect(self.on_click)
        
        stop-button = QPushButton('Stop Recording', self)
        stop-button.setToolTip('Stop Button')
        stop-button.move(150,200)
        stop-button.clicked.connect(self.on_click)
        
        self.show()

    @pyqtSlot()
    def on_click(self):
        print('Recording started')
        START = True
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    sys.exit(app.exec_())
