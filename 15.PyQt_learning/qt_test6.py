# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2018/8/29 11:26
# @Author  :  wanghuodong  
# @note    : 窗口居中

import sys
# QtWidgets包含创造经典桌面风格的用户界面提供了一套UI元素的类。
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox,QDesktopWidget
# QtGui包含类窗口系统集成、事件处理、二维图形、基本成像、字体和文本。
from PyQt5.QtGui import QIcon,QFont
#QtCore:包含了核心的非GUI功能。此模块用于处理时间、文件和目录、各种数据类型、流、URL、MIME类型、线程或进程。
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):

    def __init__(self):
        # Example类继承自QWidget类,调用父类的构造方法
        super().__init__()
        # 界面绘制交给InitUI 方法
        self.initUI()

    def initUI(self):
        #setFont()这个静态方法设置了用于提示框的字体。我们使用10px大小的SansSerif字体。
        QToolTip.setFont(QFont('SansSerif', 10))

        #创建提示框，我们调用了setTooltip() ， 为QWidget设置提示框，相当于对整个应用的一个提示
        self.setToolTip('This is a <b>QWidget</b> widget')

        '''创建了一个按钮组件并且为它设置一个提示框。'''
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        '''设置按钮的大小，以及在窗口上的（相对）位置。setHint()方法给了按钮一个推荐的大小。'''
        btn.resize(btn.sizeHint())
        btn.move(20, 150)

        '''创建 退出按钮, 并放置在顶层QWidget下 '''
        quitbtn = QPushButton('Quit', self)
        #设置提示框
        quitbtn.setToolTip('This is a quit button 这是退出按键')
        '''事件处理系统由信号&槽机制建立。如果我们点击了按钮，信号clicked被发送。槽可以是Qt内置的槽或Python 的一个方法调用。
        QCoreApplication类包含了主事件循环；它处理和转发所有事件。instance()方法给我们返回一个实例化对象。
        点击信号连接到quit()方法，将结束应用。  事件通信在两个对象之间进行：发送者和接受者。发送者是按钮，接受者是应用对象。'''
        quitbtn.clicked.connect(QCoreApplication.instance().quit)

        '''设置按钮的大小，以及在窗口上的（相对）位置。setHint()方法给了按钮一个推荐的大小。'''
        quitbtn.resize(btn.sizeHint())    #width,height
        quitbtn.move(170, 150)     # x,y


        '''三个方法都继承自QWidgets类。
        setGeometry()方法的前两个参数定位了窗口的x轴和y轴位置。第三个参数是定义窗口的宽度，第四个参数是定义窗口的高度。
        setWindowTitle() 设置了窗口的标题
        我们创建了一个QIcon对象。QIcon对象接收一个我们要显示的图片路径作为参数。'''
        # self.setGeometry(300, 300, 300, 220)  #(x,y, width,height)
        self.resize(300,220)
        self.center()

        self.setWindowTitle('Tooltips')
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


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())