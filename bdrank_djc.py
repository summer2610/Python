#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests,sys,re,os
from bs4 import BeautifulSoup
from UA import makeHeaders
from proxypool import chProxy
from multiprocessing import Process,Lock

def to8to_rank_filter(tag):
    if tag.name != 'div' or not tag.has_attr('class'):
        return False
    elif 'resultc-container' not in ''.join(tag.attrs['class']):
        return False
    elif not tag.find('a','c-showurl',string=re.compile('to8to.com')):
        return False
    else:
        return True

def get_location(landurl):
    r2 = requests.get(landurl,allow_redirects=False)
    return r2.headers['Location']

def get_rank_data(tag,keyword):
    rank = tag.attrs['id']
    rankurl = tag.find('a','c-showurl').attrs['href']
    landurl = get_location(rankurl)
    return [keyword,rank,landurl]

def run(url,filename,lock):
    keyword = re.split('[=&]',url)[1]
    try:
        r = requests.get(url,headers=makeHeaders(),proxies=chProxy(),timeout=10)
    except Exception as e:
        lock.acquire()
        with open('failed.log','a+') as log:
            log.write('%s\t%s\n' %(keyword,e))
        lock.release()
    else:
        s = BeautifulSoup(r.text,'lxml')
        to8toRanks = s.findAll(to8to_rank_filter)
        rankdatas = []
        if len(to8toRanks) != 0:
            for div in to8toRanks:
                rankdatas.append(get_rank_data(div,keyword))
        else:
            rankdatas.append([keyword,'0'])
        lock.acquire()
        with open(filename,'a+') as result:
            for line in rankdatas:
                result.write('%s\n' %'\t'.join(line))
                print('%s' %'\t'.join(line))
        lock.release()

if __name__ == "__main__":

    lock = Lock()
    keywords = open(sys.argv[1],'r').readlines()
    
    while keywords:
        team = keywords[:os.cpu_count()]
        keywords = keywords[os.cpu_count():]
        ps = []
        for searchWord in team:
            url = 'http://www.baidu.com/s?wd=%s&rn=50' %searchWord.strip()
            p = Process(target=run,args=(url,sys.argv[2],lock))
            ps.append(p)
            p.start()

        for p in ps:
            p.join()
