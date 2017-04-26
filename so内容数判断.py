#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
以关键词为搜索词请求so.php，通过源码判断内容数量
'''

import requests,time,os,sys,json,random
from multiprocessing import Process,Lock
from bs4 import BeautifulSoup
from proxypool import chProxy
from UA import makeHeaders

def chnls(keyword,soup):
    return len(soup.findAll('h3','Seotitle-h3 clear'))

def pics(keyword,soup):
    n = 0
    for i in soup.findAll('span','picShowIntroduce'):
        i = i.getText()
        if set(keyword) - set(i) == set():
            n += 1
        else:
            continue
    return n

def arts(keyword,soup):
    n = 0
    for i in soup.findAll('a','contentTitle-a'):
        i = i.getText()
        if set(keyword) - set(i) == set():
            n += 1
        else:
            continue
    return n

def ques(keyword,soup):
    n = 0
    for i in soup.findAll(True,'Question-a-title'):
        i = i.getText()
        if set(keyword) - set(i) == set():
            n += 1
        else:
            continue
    return n

def run(keyword,text,result):
    try:
        headers = makeHeaders()
        #print('%s\t生成请求头 -- 完成' %os.getpid())
        proxies = chProxy()
        #print('%s\t获取代理IP -- 完成' %os.getpid())
        r = requests.get('http://so.to8to.com/so.php?keyword=%s' %keyword,headers=headers,proxies=proxies,timeout=10)
        #print('%s\t请求so页面 -- 完成' %os.getpid())
        soup = BeautifulSoup(r.text,'lxml')
        #print('%s\t获取源码 -- 完成' %os.getpid())
        channel = chnls(keyword,soup)
        picture = pics(keyword,soup)
        article = arts(keyword,soup)
        question = ques(keyword,soup)
        #print('%s\t提取频道数/内容数 -- 完成' %os.getpid())
    except:
        lock.acquire()
        text.append(keyword)
        #print('%s\t出错关键词放进循环尾部' %os.getpid())
        lock.release()
    else:
        lock.acquire()
        print('%s,%s,%s' %(keyword,channel,picture+article+question))
        result.write('%s\t%s\t%s\n' %(keyword,channel,picture + article + question))
        lock.release()
    finally:
        result.flush()


if __name__ == "__main__":

    lock = Lock()
    result = open(sys.argv[2],'a+')
    
    
    text = open(sys.argv[1],'r').readlines()[:10000]
    while text:
        lines = text[:os.cpu_count()]        #进程数量
        text = text[os.cpu_count():]
        ps = []
        for keyword in lines:
            keyword = keyword.strip()
            p = Process(target=run,args=(keyword,text,result))
            ps.append(p)
            p.start()
    
    
        for p in ps:
            p.join()
        
        time.sleep(1)
    
    result.close()
