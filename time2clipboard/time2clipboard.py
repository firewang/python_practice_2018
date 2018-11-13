# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2018/11/13 9:28
# @Author  :  wanghuodong  
# @note    :

import time

import win32clipboard as wincb
import win32con

while True:
    s = input()
    nowtime =time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())

    wincb.OpenClipboard()
    #清空粘贴板
    wincb.EmptyClipboard()
    wincb.SetClipboardData(win32con.CF_UNICODETEXT, nowtime)  # 复制文本内容到剪贴板，（CF_TEXT系统后台会返回内存地址)
    print(wincb.GetClipboardData(win32con.CF_UNICODETEXT))
    wincb.CloseClipboard()


