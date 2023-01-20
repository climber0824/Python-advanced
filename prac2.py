import os
from multiprocessing import Pool
import time

def f(x):
    return x*x


if __name__ == '__main__':

    pool = Pool(4)
    """ ### map with different chunksize 
    pool = Pool(4)
    with pool as p:

        start = time.time() # 開始測量執行時間

        # 設定 chunksize 為 1
        result1 = p.map(f, range(10000), chunksize=1)

        end = time.time() # 結束測量執行時間
        print("chunksize 為 1，執行時間為 %f 秒" % (end - start))


        start = time.time() # 開始測量執行時間

        # 設定 chunksize 為 1000
        result2 = p.map(f, range(10000), chunksize=1000)

        end = time.time() # 結束測量執行時間
        print("chunksize 為 1000，執行時間為 %f 秒" % (end - start))

        if result1 == result2:
            print("結果相同")
    """
    inputs = [x for x in range(5)]
    with pool as p:
        for i in p.imap(f, inputs):
            print(i)
