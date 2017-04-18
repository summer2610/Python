#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
查询关键词在问答的布局数
先读取问答总标题文件text
然后逐个读取关键词，用text的count方法计算关键词出现次数，得到布局数

有单进程和多进程版本，默认为单进程
多进程版效率可提升1倍以上，但会导致电脑卡顿，可酌情选择

使用方法
命令行运行 python3 关键词问答布局数查询.py 问答标题文件 需查询的关键词文件
如：python3 关键词问答布局数查询.py ask_title.txt keywords.txt 
'''

#多进程版
#from multiprocessing import Process
#import os,sys
#
#def getBJS(word,titles):
#    rst.write('%s\t%s\n' %(word,titles.count(word)))
#    rst.flush()
#
#
#if __name__ == '__main__':
#
#    all_titles = open('ask_title.txt','r').read()
#    keywords = open('test.txt','r').readlines()
#    rst = open('result.txt','w')
#    
#    while keywords:
#        cpus = os.cpu_count()
#        lines = keywords[:cpus]
#        keywords = keywords[cpus:]
#        ps = []
#        
#        for k in lines:
#            k = k.strip()
#            p = Process(target=getBJS,args=(k,all_titles))
#            ps.append(p)
#            p.start()
#            
#        for p in ps:
#            p.join()
#
#    rst.close()

#单进程版    
file = open(sys.argv[1],'r',encoding="UTF-8")
text = file.read()
w = open('布局数.txt','w',encoding="UTF-8")

for k in open(sys.argv[2],'r',encoding="UTF-8"):
    k = k.strip()
    count = 0
    count = count + text.count(k)
    outputstr = '%s,%s\n' %(count,k)
    w.write(outputstr)
w.close()
