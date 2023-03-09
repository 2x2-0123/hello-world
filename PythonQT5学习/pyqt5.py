# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget


app = QApplication(sys.argv)            # 1. 创建应用实例
w = QWidget()                           # 2. 创建应用窗口
w.resize(900, 500)                      # 3. 设置窗口默认大小
w.setWindowTitle("第一个PyQt5程序")      # 4. 设置窗口标题
w.show()                                # 5. 显示窗口
sys.exit(app.exec_())                   # 6. 启动程序主循环
