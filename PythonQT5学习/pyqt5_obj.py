# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget

# 继承QWidget
class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(700, 300)                       # 调整窗口大小
        self.center()                               # 窗口居中
        self.setWindowTitle("PyQt5用面向对象实现")     # 窗口标题
        self.show()                                 # 窗口显示

    def center(self):
        f = self.frameGeometry()
        # QDesktopWidget().availableGeometry()获得显示器的屏幕分辨率
        # 用center()得到屏幕的中心点并赋值给frameGeometry()
        # 调用moveCenter()方法，将矩形的中心移动到屏幕中心点
        # 接着用QWidget的move()方法移动应用程序窗口的左上角到矩形的左上角
        # 从而使应用程序窗口显示在屏幕的中心
        c = QDesktopWidget().availableGeometry().center()
        f.moveCenter(c)
        self.move(f.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Widget()
    sys.exit(app.exec_())
