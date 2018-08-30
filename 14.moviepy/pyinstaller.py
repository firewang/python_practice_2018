# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2018/8/30 9:58
# @Author  :  wanghuodong  
# @note    :

#! /usr/bin/env python
#-----------------------------------------------------------------------------
# Copyright (c) 2013, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------
"""
Main command-line interface to PyInstaller.
"""
# from  PyInstaller import  *
import  os

if __name__ == '__main__':
    from PyInstaller.__main__  import run
    opts=['-F','-w',
          '--path=M:\\Anaconda3\\Lib\\site-packages\\PyQt5\\Qt\\bin',
          '--path=M:\\Anaconda3\\Lib\\site-packages\\PyQt5\\Qt\\plugins',
          # '--upx-dir=M:\\softwareInstallers\\upx394w',
          '--clean',
          'moviepy_video_cut.spec']
    run(opts)

'''
-F, --onefile Py代码只有一个文件
-D, --onedir Py代码放在一个目录中（默认是这个）
-K, --tk 包含TCL/TK
-d, --debug 生成debug模式的exe文件
-w, --windowed, --noconsole 窗体exe文件(Windows Only)
-c, --nowindowed, --console 控制台exe文件(Windows Only)
-o DIR, --out=DIR 设置spec文件输出的目录，默认在PyInstaller同目录
--icon=<FILE.ICO> 加入图标（Windows Only）
-v FILE, --version=FILE 加入版本信息文件
--upx-dir, 压缩可执行程序
--clean：清理掉临时文件
'''