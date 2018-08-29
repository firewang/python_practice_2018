# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2018/8/29 9:59
# @Author  :  wanghuodong  
# @note    :

import sys
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':

    '''所有的PyQt5应用必须创建一个应用（Application）对象。sys.argv参数是一个来自命令行的参数列表。Python脚本可以在shell中运行'''
    app = QApplication(sys.argv)

    '''Qwidget组件是PyQt5中所有用户界面类的基础类。我们给QWidget提供了默认的构造方法。默认构造方法没有父类。没有父类的widget组件将被作为窗口使用'''
    w = QWidget()
    '''resize()方法调整了widget组件的大小。它现在是250px宽，150px高。'''
    w.resize(500, 150)
    '''move()方法移动widget组件到一个位置，这个位置是屏幕上x=300,y=300的坐标。'''
    w.move(300, 300)
    '''setWindowTitle()设置了我们窗口的标题。这个标题显示在标题栏中。'''
    w.setWindowTitle('Simple')
    '''show()方法在屏幕上显示出widget。一个widget对象在内存中创建'''
    w.show()

    '''sys.exit()方法确保一个不留垃圾的退出'''
    sys.exit(app.exec_())