import sys
from PySide6.QtWidgets import QWidget,QPushButton,QApplication
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #设置按钮
        quit_button=QPushButton("退出",self)
        #点击按钮事件连接到程序退出
        quit_button.clicked.connect(QApplication.instance().quit)
        #修改按钮位置大小
        quit_button.resize(quit_button.sizeHint())
        quit_button.move(50,50)
        #修改窗口位置大小
        self.setGeometry(300,300,350,250)
        self.setWindowTitle("quit button example")
        self.show()

def main():
    app = QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()