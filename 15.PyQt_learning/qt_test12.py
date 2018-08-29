# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2018/8/29 15:44
# @Author  :  wanghuodong  
# @note    : 对话框：文件对话框

import sys
# QtWidgets包含创造经典桌面风格的用户界面提供了一套UI元素的类。
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QInputDialog, QLineEdit, QMessageBox
from PyQt5.QtWidgets import QDesktopWidget, QFrame, QColorDialog, QVBoxLayout, QSizePolicy, QLabel, QFontDialog
from PyQt5.QtWidgets import QMainWindow, QTextEdit,QAction, QFileDialog

# QtGui包含类窗口系统集成、事件处理、二维图形、基本成像、字体和文本。
from PyQt5.QtGui import QIcon, QFont, QColor
#QtCore:包含了核心的非GUI功能。此模块用于处理时间、文件和目录、各种数据类型、流、URL、MIME类型、线程或进程。
from PyQt5.QtCore import QCoreApplication,Qt


class Example(QWidget):

    def __init__(self):
        # Example类继承自QWidget类,调用父类的构造方法
        super().__init__()
        # 界面绘制交给InitUI 方法
        self.initUI()

    def initUI(self):
        #创建输入对话框
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(120, 22)

        #颜色选择对话框
        # 初始化QtGui QFrame组件的背景颜色。
        col = QColor(0, 0, 0)
        self.btn = QPushButton('Color', self)
        self.btn.move(20, 50)
        self.btn.clicked.connect(self.showColor)

        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }"% col.name())
        self.frm.setGeometry(130, 52, 100, 100)

        #字体选择对话框
        # vbox = QVBoxLayout()

        fbtn = QPushButton('Font', self)
        fbtn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        fbtn.move(20, 170)

        fbtn.clicked.connect(self.showFont)

        self.lbl = QLabel('Knowledge only matters', self)
        self.lbl.move(130, 180)

        # 文件选择对话框
        openFile = QPushButton('File',self)
        openFile.move(20,200)
        openFile.clicked.connect(self.showFile)

        '''三个方法都继承自QWidgets类。
        setGeometry()方法的前两个参数定位了窗口的x轴和y轴位置。第三个参数是定义窗口的宽度，第四个参数是定义窗口的高度。
        setWindowTitle() 设置了窗口的标题
        我们创建了一个QIcon对象。QIcon对象接收一个我们要显示的图片路径作为参数。'''
        # self.setGeometry(300, 300, 300, 220)  #(x,y, width,height)
        self.resize(400,300)
        self.center()

        self.setWindowTitle('Signal & slot')
        self.setWindowIcon(QIcon('panda.png'))
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
        if ok:
            # 将对话框中文本发送到当行编辑框中
            self.le.setText(str(text))

    def showColor(self):
        # 弹出颜色选择框
        col = QColorDialog.getColor()

        # 选中一个颜色并且点了ok按钮，会返回一个有效的颜色值。如果我们点击了Cancel按钮，不会返回选中的颜色值。
        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())

    def showFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)

    def showFile(self):
        '''第一个字符串参数是getOpenFileName()方法的标题。第二个字符串参数指定了对话框的工作目录。默认的，文件过滤器设置成All files (*)。'''
        fname = QFileDialog.getOpenFileName(self, 'Open file', __file__)
        # print(fname)  # ('L:/pycharmProjectsHome/python_practice_2018/15.PyQt_learning/qt_test12.py', 'All Files (*)')

        # if fname[0]:
        #     f = open(fname[0], 'r')
        #
        #     with f:
        #         data = f.read()
        #         self.textEdit.setText(data)

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