import time,threading

def loop():
    print('线程 %s 运行中' %threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('线程%s-%s' %(threading.current_thread().name,n))
        time.sleep(1)
    print('线程 %s 结束' %(threading.current_thread().name))

print('thread %s is running...' % threading.current_thread().name)
t1 = threading.Thread(target=loop,name='线程 A')
t2 = threading.Thread(target=loop,name='线程 B')
t1.start()
t2.start()
t1.join()
t2.join()
print('thread %s ended.' % threading.current_thread().name)
