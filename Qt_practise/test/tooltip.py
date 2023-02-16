import sys
from PySide6.QtWidgets import (QWidget,QToolTip,QPushButton,QApplication)
from PySide6.QtGui import QFont

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        #设置字体
        QToolTip.setFont(QFont("SansSerif",10))
        #创建气泡提示框
        self.setToolTip("This is a <b>QWidget</b> widget")
        #创建按钮大小位置,设置气泡提示框
        button=QPushButton("Button",self)
        button.setToolTip("This is a <b>QPushButton</b> widget")
        button.resize(button.sizeHint())
        button.move(50,50)
        #设置窗口位置和大小
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("Tooltips")
        self.show()

def main():
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
