# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2018/8/29 10:16
# @Author  :  wanghuodong  
# @note    : pyqt5是面向对象编程，为窗口添加应用图标

import sys
# QtWidgets包含创造经典桌面风格的用户界面提供了一套UI元素的类。
from PyQt5.QtWidgets import QApplication, QWidget
# QtGui包含类窗口系统集成、事件处理、二维图形、基本成像、字体和文本。
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        # Example类继承自QWidget类,调用父类的构造方法
        super().__init__()
        # 界面绘制交给InitUI 方法
        self.initUI()

    def initUI(self):
        '''三个方法都继承自QWidgets类。
        setGeometry()方法的前两个参数定位了窗口的x轴和y轴位置。第三个参数是定义窗口的宽度，第四个参数是定义窗口的高度。
        setWindowTitle() 设置了窗口的标题
        我们创建了一个QIcon对象。QIcon对象接收一个我们要显示的图片路径作为参数。'''
        self.setGeometry(300, 300, 300, 220)  #(x,y, width,height)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('panda.png'))

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())
