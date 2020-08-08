from multiprocessing import Pool
# import multiprocessing as mp
import time
import os

def longTimeTask(i):
    print('task: {}, PID: {}'.format(i, os.getpid()))
    time.sleep(2)
    result = 10 ** 30

if __name__ == '__main__':
    start_time = time.time()
    print('母程序PID', os.getpid())

    p = Pool(4)
    for i in range(8):           # 1 pool 上限為 4 人 有人結束才遞補
        p.apply_async(longTimeTask, args=(i+1, ))
    p.close()
    p.join()

    end_time = time.time()
    print('花了 {} 秒'.format(end_time-start_time))






