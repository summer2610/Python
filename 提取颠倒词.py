'''脚本作用
删除源文件中的颠倒词，同时输出一个包含所有颠倒词的文件
由于是逐词对比，因此运行时间会随词量几何上升，不建议处理太多关键词
'''

import threading,sys

text = open(sys.argv[1],'r').readlines()
textbak = text[:]

file = open('不含颠倒词结果.txt','w')
ddc = open('颠倒词.txt','w')

lock = threading.Lock()

def ifddc(A):
    for B in open('xgt_words副本.txt','r'):
        if sorted(A) == sorted(B) and A != B:
            lock.acquire()
            try:
                textbak.pop(textbak.index(B))
                ddc.write(B)
            except:
                continue
            finally:
                lock.release()


while text:
    lines = text[:10]
    text = text[10:]
    threads = []
    for keyword in lines:
        t = threading.Thread(target=ifddc,args=(keyword,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()


for i in textbak:
    file.write(i)
print('颠倒词判断完毕,结果已写入文件')
file.close()
ddc.close()