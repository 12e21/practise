import sys
from PySide6.QtWidgets import QMainWindow,QApplication

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.statusBar().showMessage("Ready")
        #该方法的创建了一个状态栏，并返回statusbar对象，再调用 showMessage 方法在状态栏上显示一条消息。
        self.setGeometry(300,300,350,250)
        self.setWindowTitle("Status Bar")
        self.show()

def main():
    app = QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()