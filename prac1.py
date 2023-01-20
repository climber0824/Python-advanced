from multiprocessing import Process, Pool
import multiprocessing
import os, time

def main(i):
    res = i * i
    print(res)
    return res


def main_map(I):
    result = I * I
    print("子處理程序 ID: {}, 運送結果: {}".format(os.getpid(), result))
    return result
 
 
def show(get_result):
    print('Callback: {} PID: {}'.format(get_result, os.getpid()))
 


if __name__ == '__main__':
    """
    cpus1 = multiprocessing.cpu_count()
    cpus2 = os.cpu_count()
    print(cpus1, cpus2)
    """
    inputs = [x for x in range(10)]
    
    # 設定處理程序數量
    #pool = Pool(4)

    
    ############# W/O _async 範例：#############
    """
    # wihout async
    pool_outputs = pool.map(main, inputs)
    print('將會阻塞並於 pool.map 子程序結束後觸發')
    """
    # with async
    # 運行多處理程序
    #pool_outputs = pool.map_async(main, inputs)
    #print('將不會阻塞並和 pool.map_async 並行觸發')
 
    # close 和 join 是確保主程序結束後，子程序仍然繼續進行
    #pool.close()
    #pool.join()

    """
    pool.map_async 和 pool.map 的差異在於，主處理程序是否同步並行，
    而 pool.map 會阻塞主程序，待所有子程序結束後，才會繼續運行主程序。
    而 pool.map_async 反之，所以最後要寫 close 和 join 來避免主程序結束後，子程序被迫關閉。
    """



    ############# 使用 map_async 寫 callback 範例：#############
    """
    從 print 結果可以看到此次啟動了 4 個子處理程序，最後子處理程序都運送完後，由主程序處理啟動 callback 的函式 show，最後結束主處理程序。
    """
    """
    print('主處理程序 ID:', os.getpid())
    pool = Pool(4)
 
    results = pool.map_async(main_map, [3, 5, 7, 9, 11, 13, 15], callback=show)
    pool.close()
    pool.join()
    """
    


    ############# 取得回傳資料 #############
    ### pool.map_async 和 pool.starmap_async 要取的回傳資料需要使用 .get() 方法 ###
    pool = Pool(4)
    results = pool.map_async(main_map, [3, 5, 7, 9, 11, 13, 15])
    print(results.get())

    ### pool.map 和 pool.starmap 可直接調用即可 ###
    results = pool.map(main_map, [3, 5, 7, 9, 11, 13, 15])
    print(results)