#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from bs4 import BeautifulSoup
from multiprocessing import Process,Lock


def getPrice(url,brower):
    rstr = url
    try:
        brower.get(url)
        r = brower.page_source
    except:
        #print('请求失败')
        rstr = url
    else:
        s = BeautifulSoup(r,'html.parser')
        try:
            good = s.find('div','tb-detail-hd').h1.getText().strip()
            prices = sorted([float(x.getText().split('-')[0]) for x in s.findAll('span','tm-price')])
            rstr = '%s\t%s' %(prices[0],good)
        except:
            #print('获取价格失败')
            rstr = url
    finally:
        #lock.acquire()
        if 'http' not in rstr:
            print(rstr)
            #result.write('%s\n' %rstr)
            #result.flush()
        else:
            print(rstr)
            #fail.write('%s\n' %rstr)
            #fail.flush()
        #lock.release()


if __name__ == '__main__':

    cpus = 3    #CPU数量
    browers = []
    for i in range(cpus):
        browers.append(webdriver.PhantomJS())
    result = open('result.txt','w')
    fail = open('fail.txt','w')

    urls = open('tm_urls.txt','r').readlines()
    lock = Lock()

    while len(urls) != 0:
        lines = urls[:cpus]
        urls = urls[cpus:]
        ps = []
        for i in lines:
            p = Process(target=getPrice,args=(i.strip(),browers[lines.index(i)]))
            ps.append(p)
            p.start()

        for p in ps:
            p.join()


    for i in browers:
        i.close()
        i.quit()

    result.close()
    fail.close()
