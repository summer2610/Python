#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests,json,random,sys,os,re
from bs4 import BeautifulSoup
from proxypool import chProxy
from UA import makeHeaders

def getCacheURL(keyword):
    r = requests.get('http://www.baidu.com/s?wd=%s' %keyword,proxies=chProxy(),headers=makeHeaders())
    s = BeautifulSoup(r.text,'html.parser')
    return s.find('a',href=re.compile('http://cache.baiducontent.com.*'))['href']

def getAnsNum(cacheURL):
    r = requests.get(cacheURL,proxies=chProxy(),headers=makeHeaders())
    s = BeautifulSoup(r.text,'html.parser')
    try:
        AnsNum = s.findAll('div','title title2')[0].span.getText()
    except AttributeError:
        return 0
    else:
        return AnsNum

if __name__ == '__main__':
    keywords = open(sys.argv[1],'r').readlines()#[:10]
    rst = open('result.txt','w')

    for i in keywords:
        i = i.strip()
        try:
            url = getCacheURL(i)
            ansNum=getAnsNum(url)
        except:
            continue
        else:
            print('%s\t%s' %(i,ansNum))
            #rst.write('%s\t%s\n' %(i,ansNum))
            #rst.flush()

    rst.close()