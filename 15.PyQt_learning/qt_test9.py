# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2018/8/29 11:26
# @Author  :  wanghuodong  
# @note    : 布局管理（QGridLayout 网格布局， 计算器，文本审阅窗口）

import sys
# QtWidgets包含创造经典桌面风格的用户界面提供了一套UI元素的类。
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox,QDesktopWidget,QMainWindow
from PyQt5.QtWidgets import QAction, qApp,  QTextEdit,QHBoxLayout, QVBoxLayout,QGridLayout,QLabel, QLineEdit
# QtGui包含类窗口系统集成、事件处理、二维图形、基本成像、字体和文本。
from PyQt5.QtGui import QIcon,QFont
#QtCore:包含了核心的非GUI功能。此模块用于处理时间、文件和目录、各种数据类型、流、URL、MIME类型、线程或进程。
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):
    def __init__(self):
        # Example类调用父类的构造方法
        super().__init__()
        # 界面绘制交给InitUI 方法
        self.initUI()

    def initUI(self):
        #setFont()这个静态方法设置了用于提示框的字体。我们使用10px大小的SansSerif字体。
        QToolTip.setFont(QFont('SansSerif', 10))

        #创建提示框，我们调用了setTooltip() ， 为QWidget设置提示框，相当于对整个应用的一个提示
        self.setToolTip('This is a <b>QWidget</b> widget')


        '''三个方法都继承自QWidgets类。
        setGeometry()方法的前两个参数定位了窗口的x轴和y轴位置。第三个参数是定义窗口的宽度，第四个参数是定义窗口的高度。
        setWindowTitle() 设置了窗口的标题
        我们创建了一个QIcon对象。QIcon对象接收一个我们要显示的图片路径作为参数。'''
        # self.setGeometry(300, 300, 300, 220)  #(x,y, width,height)
        self.resize(300,220)
        self.center()

        # 布局管理,网格布局,计算器按键布局示例
        # grid = QGridLayout()
        # self.setLayout(grid)
        # names = ['Cls', 'Bck', '', 'Close',
        #          '7', '8', '9', '/',
        #          '4', '5', '6', '*',
        #          '1', '2', '3', '-',
        #          '0', '.', '=', '+']
        #
        # positions = [(i, j) for i in range(5) for j in range(4)]
        #
        # for position, name in zip(positions, names):
        #
        #     if name == '':
        #         continue
        #     button = QPushButton(name)
        #     print(position)
        #     print(*position)
        #     grid.addWidget(button, *position)


        # 网格布局，文本审阅窗口示例
        # 创建了包含三个标签，两个单行编辑框和一个文本编辑框组件的窗口。布局使用了QGridLayout布局。
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        # 设置组件之间的间距
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        # row: int, column: int, rowSpan: int, columnSpan: int
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)


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