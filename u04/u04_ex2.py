from multiprocessing import Pool
import time
import os

class Test:
    a = []

    def longTimeTask(self, i):
        print('task: {}, PID: {}'.format(i, os.getpid()))
        time.sleep(2)
        result = 10 ** 30
        self.a.append(result)     #  多 process 各自有獨立的記憶體空間 可以修該 a 但是是在自己的記憶體空間下做修改
        print(self.a)
        return result

if __name__ == '__main__':
    start_time = time.time()
    print('母程序PID', os.getpid())
    T = Test()
    # 觀察PID
    p = Pool(4)
    # data is a list catch 每次遞迴的回傳值
    data = p.map(T.longTimeTask, iterable=range(4))   # iterable=range(4) 也可用 list 進行疊代
    p.close()
    p.join()
    print(data)
    print(T.a)

    end_time = time.time()
    print('花了 {} 秒'.format(end_time-start_time))