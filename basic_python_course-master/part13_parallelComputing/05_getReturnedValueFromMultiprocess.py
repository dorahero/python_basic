from multiprocessing import Pool
import os
import time

def longTime(i):
    print('PID: {}, Task: {} .'.format(os.getpid(), i))
    time.sleep(2)
    result = 10 ** 30
    print('Result: {}'.format(result))
    return result

if __name__ == '__main__':
    start_time = time.time()
    print('母程序PID: {}'.format(os.getpid()))

    p = Pool(4)
    data = p.map(longTime, iterable=range(0, 4))
    p.close()
    p.join()

    end_time = time.time()
    print('總共花費 {} 秒'.format(end_time - start_time))

    print(data)
    