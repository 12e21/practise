import sys
from PySide6.QtWidgets import QApplication,QWidget
#引入了必要的包，基础小组件位于 PyQt6.QtWidgets 模块

def main():
    #每个 PyQt6 应用程序都必须创建一个应用程序对象
    app = QApplication(sys.argv)
    #QWidget 小部件是 PyQt6 中所有用户界面对象的基类,没有父级的小部件称为窗口
    window = QWidget()
    #改变了小部件的尺寸
    window.resize(250,200)
    #把小部件移动到屏幕的指定坐标(300, 300)
    window.move(300,300)
    #给窗口设置标题
    window.setWindowTitle("Hello.out")
    #在屏幕上显示小部件
    window.show()
    #进入应用程序的主循环
    sys.exit(app.exec())

if __name__ == "__main__":
    main()