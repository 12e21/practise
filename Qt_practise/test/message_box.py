import sys
from PySide6.QtWidgets import QWidget,QApplication,QMessageBox

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,350,200)
        self.setWindowTitle("Message Box")
        self.show()
    #关闭 QWidget 操作会产生 QCloseEvent 事件。重新实现 closeEvent 事件处理，替换部件的默认行为
    def closeEvent(self,event):
        '''这里创建了一个带有两个按钮的消息框：是和否。第一个参数是标题栏，
        第二个参数是对话框显示的消息文本，第三个参数是对话框中的按钮组合，
        最后一个参数是默认选中的按钮。返回值存储在变量reply中'''

        reply=QMessageBox.question(self,"Message",
                                   "Are you sure to quit?",QMessageBox.StandardButton.Yes |
                                   QMessageBox.StandardButton.No,QMessageBox.StandardButton.No)

        if reply ==QMessageBox.StandardButton.Yes:
            #执行关闭事件
            event.accept()
        else:
            #忽略关闭事件
            event.ignore()

def main():
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()