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

    mp_list = []
    for p in range(4):
        mp_list.append(mp.Process(target=longTimeTask, args=(p+1, )))

    for i in range(4):
        mp_list[i].start()

    for i in range(4):
        mp_list[i].join()


    end_time = time.time()
    print('花了 {} 秒'.format(end_time-start_time))












