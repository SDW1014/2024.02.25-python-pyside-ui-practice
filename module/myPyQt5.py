import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

class myPyQt5_window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.lbl = QLabel('myPyQt5 window Label', self)
        self.lbl.move(50, 50)
        
        btn = QPushButton('button', self)
        btn.move(50, 100)
        
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('myPyqt5')
        
def main():
    app = QApplication(sys.argv)
    ex = myPyQt5_window()
    ex.show()
    sys.exit(app.exec_())