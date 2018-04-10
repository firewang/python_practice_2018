# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2018/4/10 12:02
# @Author  :  wanghuodong  
# @note    : 

import time, sched,os

# 周期性执行给定的任务
# 初始化sched模块的scheduler类
# 第一个参数是一个可以返回时间戳的函数，第二个参数可以在定时未到达之前阻塞。
s = sched.scheduler(time.time, time.sleep)

# 需要被周期性调度触发的函数


def event_func():
    print("func time:", time.time())
    os.system('python {}'.format('E:/pycharmProjectsHome/send_mail/t2.py'))

#周期性执行 方法， 执行 需要被周期性调度触发的函数
'''
sched.sheduler().enter(delay,priority,func,args)
delay：任务的间隔时间。
priority：如果几个任务被调度到相同的时间执行，将按照priority的增序执行这几个任务。
func：要执行的任务函数,触发的函数;
args：func的参数,函数参数
'''
def perform(inc,is_loop):
    event_func()
    if is_loop:
        s.enter(inc, 0, perform, (inc,is_loop))

#主方法，调用周期性执行方法
def mymain(func, inc=5,time_duration='s',is_loop=True):
    if time_duration=='m':
        s.enter(0, 0, func, (inc*60,is_loop))  # 每 inc 分钟执行perform
    elif time_duration=='h':
        s.enter(0, 0, func, (inc*3600, is_loop))  # 每inc 小时执行perform
    else:
        s.enter(0, 0, func, (inc, is_loop))  # 每5秒钟执行perform
if __name__ == "__main__":
    mymain(perform,is_loop=True)
    s.run()
