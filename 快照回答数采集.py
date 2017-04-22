#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests,json,random,sys,os,re
from bs4 import BeautifulSoup
from proxypool import chProxy
from UA import makeHeaders

def getCacheURL(keyword):
    r = requests.get('http://www.baidu.com/s?wd=%s' %keyword,proxies=chProxy(),headers=makeHeaders())
    s = BeautifulSoup(r.text,'html.parser')
    return s.find('a',href=re.complie('http://cache.baiducontent.com.*'))

def getAnsNum(cacheurl):
    r = requests.get(url,proxies=chProxy(),headers=makeHeaders())
    s = BeautifulSoup(r.text,'html.parser')
    return s.findAll('div','title title2')[0].span.getText()

if __name__ == '__main__':
    keywords = open(sys.argv[1],'r').readlines()
    rst = open('result.txt','w')

    for i in keywords:
        i = i.strip()
        url = getCacheURL(i)
        ansNum=getAnsNum(url)
        rst.write('%s\t%s\n' %(i,ansNum))
        rst.flush()

    rst.close()
