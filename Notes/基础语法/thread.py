# -*- codeing = utf-8 -*-
# @Time : 2020/9/15 9:40 下午
import threading
import time
from queue import Queue

def thread_job():
    print('T1 srart\n')
    #print('进程的名字%s' % threading.current_thread()) --显示进程名字
    for i in range(10):
        time.sleep(0.1)
    print('T1 finish\n')

if __name__ == '__main__':
    # --显示当前所有进程
    # print(threading.active_count())
    # --将thread_job函数放入线程池，targer=函数，args=()参数
    t = threading.Thread(target=thread_job,name='t1')
    # --启动线程
    t.start()
    # --join让主线程等待子线程
    t.join()
    # --线程池的进程和以下for循环同时进行
    for i in range(100):
        time.sleep(1)
        print(i)
