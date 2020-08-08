from multiprocessing import Pool
# import multiprocessing as mp
import time
import os

def longTimeTask(i):
    print('task: {}, PID: {}'.format(i, os.getpid()))
    time.sleep(2)
    result = 10 ** 30
    return result

if __name__ == '__main__':
    start_time = time.time()
    print('母程序PID', os.getpid())

    p = Pool(4)
    # data is a list catch 每次遞迴的回傳值
    data = p.map(longTimeTask, iterable=[2, 4, 6, 8])   # iterable=range(4) 也可用 list 進行疊代
    p.close()
    p.join()

    print(data)

    end_time = time.time()
    print('花了 {} 秒'.format(end_time-start_time))



