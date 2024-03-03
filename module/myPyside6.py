import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QStackedWidget, QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PySide6.QtGui import QPixmap

class PageWidget(QWidget):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.initUI()

    def initUI(self):
        layout = QGridLayout(self)
        for i, item in enumerate(self.data):
            button = QPushButton()
            pixmap = QPixmap(f"images/{item}.jpg")  # 예시 이미지 경로
            button.setIcon(pixmap)
            button.setIconSize(pixmap.size())
            layout.addWidget(button, i // 5, i % 5)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.data = list(range(1, 101))  # 예시 데이터: 1부터 100까지의 숫자
        self.page_size = 20  # 페이지당 아이템 개수
        self.current_page = 0  # 현재 페이지
        self.initializeUI()

    def initializeUI(self):
        self.setWindowTitle("Dynamic Paging Example")
        self.setGeometry(300, 300, 600, 400)
        self.createPageWidgets()
        self.createNavigationButtons()
        self.showPage(self.current_page)

    def createPageWidgets(self):
        self.mainWidget = QWidget()
        self.setCentralWidget(self.mainWidget)

        self.stackedLayout = QStackedWidget()
        self.mainLayout = QVBoxLayout(self.mainWidget)
        self.mainLayout.addWidget(self.stackedLayout)

        for i in range(len(self.data) // self.page_size + 1):
            page_data = self.data[i*self.page_size : (i+1)*self.page_size]
            page_widget = PageWidget(page_data)
            self.stackedLayout.addWidget(page_widget)

        self.pageLabel = QLabel()
        self.updatePageLabel()
        self.mainLayout.addWidget(self.pageLabel)

    def createNavigationButtons(self):
        self.nextButton = QPushButton("Next")
        self.nextButton.clicked.connect(self.nextPage)

        self.prevButton = QPushButton("Previous")
        self.prevButton.clicked.connect(self.prevPage)

        self.navLayout = QHBoxLayout()
        self.navLayout.addWidget(self.prevButton)
        self.navLayout.addStretch(1)
        self.navLayout.addWidget(self.nextButton)
        self.mainLayout.addLayout(self.navLayout)

    def nextPage(self):
        if self.current_page < self.stackedLayout.count() - 1:
            self.current_page += 1
            self.showPage(self.current_page)

    def prevPage(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.showPage(self.current_page)

    def showPage(self, page_index):
        self.stackedLayout.setCurrentIndex(page_index)
        self.updatePageLabel()

    def updatePageLabel(self):
        total_pages = self.stackedLayout.count()
        current_page = self.current_page + 1
        self.pageLabel.setText(f"Page {current_page}/{total_pages}")

def start():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    start()
