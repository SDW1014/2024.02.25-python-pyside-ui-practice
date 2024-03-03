import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton

class ConsoleApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.outputArea = QTextEdit()  # 출력 영역
        self.outputArea.setReadOnly(True)  # 읽기 전용으로 설정
        
        self.inputLine = QLineEdit()  # 입력 필드
        self.inputLine.returnPressed.connect(self.executeCommand)
        
        self.executeBtn = QPushButton('Execute')  # 실행 버튼
        self.executeBtn.clicked.connect(self.executeCommand)

        layout.addWidget(self.outputArea)
        layout.addWidget(self.inputLine)
        layout.addWidget(self.executeBtn)

        self.setLayout(layout)
        self.setWindowTitle('Console Example')
        self.setGeometry(100, 100, 600, 400)

    def executeCommand(self):
        command = self.inputLine.text()
        self.outputArea.append(f"> {command}")  # 입력된 명령을 출력 영역에 표시
        # TODO: 여기에서 실제 명령 처리 로직을 구현할 수 있습니다.
        self.inputLine.clear()  # 입력 필드 초기화

def main():
    app = QApplication(sys.argv)
    ex = ConsoleApp()
    ex.show()
    sys.exit(app.exec_())
    
main()