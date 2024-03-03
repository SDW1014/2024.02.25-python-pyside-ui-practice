import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMenuBar
from PySide6.QtGui import QAction
from PySide6.QtCore import QPropertyAnimation, QRect

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button_count = 0  # 동적으로 추가된 버튼의 개수를 추적
        self.initializeUI()

    def initializeUI(self):
        """Initializes the window's UI."""
        self.setWindowTitle("PySide6 Dynamic Widgets")
        self.setGeometry(300, 300, 1080, 600)
        self.createMenus()
        self.addDynamicButton()
        self.configureStyles()

    def configureStyles(self):
            """Sets the window's style."""
            self.setStyleSheet("""
                QMainWindow {
                    background-color: #2b2b2b;
                }
                QMenuBar {
                    background-color: #333;
                    color: #fff;
                }
                QMenuBar::item:selected {
                    background-color: #555;
                }
                QMenu {
                    background-color: #333;
                    color: #fff;
                }
                QMenu::item:selected {
                    background-color: #555;
                }
                QPushButton {
                    background-color: #5a5a5a;
                    color: #ffffff;
                    border: 2px solid #5a5a5a;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #787878;
                }
                QPushButton:pressed {
                    background-color: #505050;
                }
            """)

    def createMenus(self):
        """Creates the menu bar and dynamically adds menus."""
        self.dynamic_menu = self.menuBar().addMenu("동적 메뉴")
        self.addMenuAction(self.dynamic_menu, "새 버튼 추가", self.addDynamicPushButtonWithAnimation)

    def addMenuAction(self, menu, action_name, action_function):
        """Dynamically adds an action to a menu."""
        action = QAction(action_name, self)
        action.triggered.connect(action_function)
        menu.addAction(action)

    def addDynamicButton(self):
        """Adds a button that creates more buttons dynamically."""
        self.addDynamicPushButtonWithAnimation()

    def addDynamicPushButtonWithAnimation(self):
        """Adds a new push button to the window dynamically with animation."""
        self.button_count += 1
        new_button = QPushButton(f"버튼 {self.button_count}", self)
        y_position = 50 + (40 * self.button_count)
        new_button.setGeometry(50, y_position, 100, 30)
        new_button.clicked.connect(lambda: self.buttonClicked(self.button_count))
        new_button.show()  # 새로운 버튼을 보이게 합니다.
        self.animateButton(new_button)

    def animateButton(self, button):
        """Animates the button."""
        animation = QPropertyAnimation(button, b"geometry")
        animation.setDuration(1000)
        animation.setStartValue(button.geometry())
        animation.setEndValue(QRect(50, button.geometry().y(), 200, 50))  # 버튼 크기와 위치 조정
        animation.start()

    def buttonClicked(self, button_number):
        """Action to perform when a dynamic button is clicked."""
        print(f"버튼 {button_number} 클릭됨")

def start():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    start()
