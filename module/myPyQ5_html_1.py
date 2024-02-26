import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebChannel import QWebChannel  # 수정된 임포트
from PyQt5.QtCore import QObject, pyqtSlot

class CallHandler(QObject):
    @pyqtSlot()
    def buttonClicked(self):
        print("버튼이 클릭되었습니다.")

def main():
    app = QApplication(sys.argv)

    web = QWebEngineView()
    channel = QWebChannel()
    handler = CallHandler()

    channel.registerObject('backend', handler)
    web.page().setWebChannel(channel)

    html_string = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>PyQt5와 HTML 연동 예제</title>
    </head>
    <body>
        <h1>PyQt5와 HTML의 연동</h1>
        <button onclick="buttonClicked()">클릭하세요</button>
        <button onclick="buttonAlert()">클릭하세요</button>
        <script type="text/javascript">
            new QWebChannel(qt.webChannelTransport, function(channel) {
                window.backend = channel.objects.backend;
            });

            function buttonClicked() {
                window.backend.buttonClicked();
            }
            function buttonAlert()
            {
                alert("뭐시발");
            }
        </script>
    </body>
    </html>
    """

    web.setHtml(html_string)
    web.show()

    sys.exit(app.exec_())