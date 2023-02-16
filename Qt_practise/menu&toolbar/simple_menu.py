import sys
from PySide6.QtWidgets import QMainWindow,QApplication
from PySide6.QtGui import QIcon,QAction

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        exit_act=QAction(QIcon("exit.png"),"&Exit",self)
        #创建了一个带有特定图标和 'Exit' 标签的行为
        exit_act.setShortcut("Ctrl+Q")
        #定义了一个快捷键
        exit_act.setStatusTip("Exit application")
        #创建一个状态提示,将鼠标指针悬停在菜单项上时，状态栏中就会显示这个提示
        exit_act.triggered.connect(QApplication.instance().quit)
        #行为触发信号与程序退出相连
        self.statusBar()

        menubar = self.menuBar()
        #menuBar 方法创建了一个菜单栏
        file_menu=menubar.addMenu("&File")
        #然后使用 addMenu 创建一个文件菜单
        file_menu.addAction(exit_act)
        #使用 addAction 为菜单添加一个行为

        self.setGeometry(300,300,350,250)
        self.setWindowTitle("Simple Menu")
        self.show()

def main():
    app = QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

