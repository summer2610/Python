#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import sys
from bs4 import BeautifulSoup
from CONFIG import getProxy,makeHeaders
from multiprocessing import Process,Lock

def count_contain(keyword,titles):
    count = [0,0]
    for t in titles:
        if keyword in t:
            count[0] += 1
        elif set(keyword) - set(t) == set():
            count[1] += 1
    return count


def run(url,filename):
    write_str = ''
    try:
        r = requests.get(url,proxies=getProxy(),headers=makeHeaders(),timeout=10)
    except Exception as e:
        write_str = '%s\t%s\n' %(url,e)
    else:
        s = BeautifulSoup(r.text,'lxml')
        try:
            keyword = s.find('div','xgt_search_select xgt_st_nh_new').span.em.getText()
            titles = [ x.img['alt'] for x in s.findAll('a','item_img')]
        except:
            write_str = '%s\t源码解析错误\n' %url
        else:
            count = count_contain(keyword,titles)
            write_str = '%s\t%s\t%s\n' %(url,count[0],count[1])
    finally:
        print(write_str.strip())
        lock.acquire()
        with open(filename,'a+') as f:
            f.write(write_str)
        lock.release()

if __name__ == "__main__":

    lock = Lock()

    urls = open(sys.argv[1],'r').readlines()
    
    while len(urls) != 0:
        team = urls[:3]
        urls = urls[3:]
        
        ps = []
        for url in team:
            p = Process(target=run,args=(url.strip(),sys.argv[2]))
            ps.append(p)
            p.start()
            
        for p in ps:
            p.join()
