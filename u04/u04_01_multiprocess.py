import multiprocessing as mp
import time
import os

def longTimeTask(i):
    print('task: {}, PID: {}'.format(i, os.getpid()))
    time.sleep(2)
    result = 10 ** 30
    print('result:', result)

if __name__ == '__main__':
    start_time = time.time()
    print('母程序PID', os.getpid())

    # target 函數不括號, 引述型態為 tuple Ex: (a, )
    work1 = mp.Process(target=longTimeTask, args=(1, ))
    work2 = mp.Process(target=longTimeTask, args=(2, ))
    work3 = mp.Process(target=longTimeTask, args=(3, ))
    work4 = mp.Process(target=longTimeTask, args=(4, ))

    work1.start()       # 同時執行
    work2.start()
    work3.start()
    work4.start()

    work1.join()         # 互相等待
    work2.join()
    work3.join()
    work4.join()

    end_time = time.time()
    print('花了 {} 秒'.format(end_time-start_time))















