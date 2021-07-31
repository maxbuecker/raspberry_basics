#!/usr/bin/python3

#import libraries for GUI
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

#define GUI
class PushButton(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 Push button - pyblog.in'
        self.width = 400
        self.height = 300
        self.left = 10
        self.top = 10
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This is an example pyqt5 push button')
        button.move(150,100)
        button.clicked.connect(self.on_click)
        
        self.show()

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 pushbutton is clicked')
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    button = PushButton()
    sys.exit(app.exec_())
