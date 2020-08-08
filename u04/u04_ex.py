from multiprocessing.dummy import Pool   # 虛擬池化
import time
import os

class Test():
    a = []

    def longTimeTask(self, i):
        print('task: {}, PID: {}'.format(i, os.getpid()))
        time.sleep(2)
        result = 10 ** 30
        self.a.append(result)  # 多 thread 在同個 process 共用同一個記憶體 所以可以共享同一個全域變數 a
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