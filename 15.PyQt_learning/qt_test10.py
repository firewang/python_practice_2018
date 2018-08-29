# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2018/8/29 14:49
# @Author  :  wanghuodong  
# @note    : 事件，信号与槽。 滑块条和数字显示，重写esc方法
# 在事件模型，有三个参与者
#
# 事件源
# 事件对象
# 事件目标
# 事件源是状态发生改变的对象。它产生了事件。事件对象(event)封装了事件源中的状态变化。事件目标是想要被通知的对象。事件源对象代表了处理一个事件直到事件目标做出响应的任务。
#
# PyQt5用信号和槽机制来处理事件。信号和槽用于对象之间的通信。当指定事件发生，一个事件信号会被发射。槽可以被任何Python脚本调用。当和槽连接的信号被发射时，槽会被调用。

import sys
# QtWidgets包含创造经典桌面风格的用户界面提供了一套UI元素的类。
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox,QDesktopWidget,QWidget, QLCDNumber, QSlider,QVBoxLayout, QApplication
# QtGui包含类窗口系统集成、事件处理、二维图形、基本成像、字体和文本。
from PyQt5.QtGui import QIcon,QFont
#QtCore:包含了核心的非GUI功能。此模块用于处理时间、文件和目录、各种数据类型、流、URL、MIME类型、线程或进程。
from PyQt5.QtCore import QCoreApplication,Qt


class Example(QWidget):

    def __init__(self):
        # Example类继承自QWidget类,调用父类的构造方法
        super().__init__()
        # 界面绘制交给InitUI 方法
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        # 将滑块条的valueChanged信号和lcd数字显示的display槽连接在一起。
        sld.valueChanged.connect(lcd.display)


        '''三个方法都继承自QWidgets类。
        setGeometry()方法的前两个参数定位了窗口的x轴和y轴位置。第三个参数是定义窗口的宽度，第四个参数是定义窗口的高度。
        setWindowTitle() 设置了窗口的标题
        我们创建了一个QIcon对象。QIcon对象接收一个我们要显示的图片路径作为参数。'''
        # self.setGeometry(300, 300, 300, 220)  #(x,y, width,height)
        self.resize(300,220)
        self.center()

        self.setWindowTitle('Signal & slot')
        self.setWindowIcon(QIcon('panda.png'))
        self.show()

    def closeEvent(self, event):
        '''第一个字符串的内容被显示在标题栏上。
        第二个字符串是对话框上显示的文本。
        第三个参数指定了显示在对话框上的按钮集合。
        最后一个参数是默认选中的按钮。这个按钮一开始就获得焦点。
        返回值被储存在reply变量中。'''
        reply = QMessageBox.question(self, 'Message退出提示框标题', "Are you sure to quit?退出提示", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        # 获得主窗口的一个矩形特定几何图形。这包含了窗口的框架(width,height),自己设定的大小。
        qr = self.frameGeometry()
        # print(qr)  #PyQt5.QtCore.QRect(0, 0, 299, 219)
        # 算出相对于显示器的绝对值。并且从这个绝对值中，我们获得了屏幕中心点。
        cp = QDesktopWidget().availableGeometry().center()
        # print(cp)     # PyQt5.QtCore.QPoint(959, 514)
        # 将矩形的中心设置到屏幕的中间去。矩形的大小并不会改变。
        qr.moveCenter(cp)
        # print(qr)  # PyQt5.QtCore.QRect(810, 405, 299, 219)
        # 移动了应用窗口的左上方的点到qr矩形的左上方的点，因此居中显示在我们的屏幕上。没有也没关系?
        self.move(qr.topLeft())

    def keyPressEvent(self,e):
        if e.key() == Qt.Key_Escape:
            self.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())