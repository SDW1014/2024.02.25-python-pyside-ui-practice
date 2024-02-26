import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QLabel

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
            }
            QPushButton {
                background-color: #0088ff;
                color: white;
                border-radius: 10px;
                padding: 10px;
                font-size: 15px;
            }
            QPushButton:hover {
                background-color: #0055cc;
            }
            QListWidget {
                border: none;
                padding: 10px;
                font-size: 14px;
            }
            QLabel {
                color: #333;
                font-size: 14px;
                padding: 10px;
            }
        """)
        
        layout = QVBoxLayout()
        
        self.listWidget = QListWidget()
        self.addButton = QPushButton('항목 추가')
        self.infoLabel = QLabel('선택된 항목 정보를 여기에 표시합니다.')
        
        self.addButton.clicked.connect(self.addItem)
        self.listWidget.itemClicked.connect(self.showItemInfo)
        
        layout.addWidget(self.listWidget)
        layout.addWidget(self.addButton)
        layout.addWidget(self.infoLabel)
        
        self.setLayout(layout)
        self.setWindowTitle('깔끔한 동적 UI 예제')
        self.setGeometry(100, 100, 300, 400)
    
    def addItem(self):
        self.listWidget.addItem(f'항목 {self.listWidget.count() + 1}')
    
    def showItemInfo(self, item):
        self.infoLabel.setText(f'{item.text()}이(가) 선택되었습니다.')

def main():
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())