#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests,sys,os
from proxypool import chProxy
from multiprocessing import Process
from bs4 import BeautifulSoup

def manager(url,filename,mode):
    try:
        r = requests.get(url,proxies=chProxy(),timeout=5)
    except:
        print('%s\t失败' %url)
    else:
        if mode == 'ztm':
            ztm = get_ztm(r)
            with open(filename,'a+') as f:
                f.write('%s\t%s\n' %(url,ztm))
            print('%s\t%s' %(url,ztm))
        elif mode == 'title':
            title = get_title(r)
            with open(filename,'a+') as f:
                f.write('%s\t%s\n' %(url,title))
            print('%s\t%s' %(url,title))

def get_title(response):
    try:
        title = BeautifulSoup(response.text,'lxml').find('title').getText()
    except:
        title = ''
    else:
        title = title.split('_')[0]
    finally:
        return title

def get_ztm(response):
    return response.status_code


if __name__ == "__main__":

    urls = open(sys.argv[1],'r').readlines()
    outfile = sys.argv[2]
    mode = sys.argv[3]
    
    while urls:
        team = urls[:os.cpu_count()]
        urls = urls[os.cpu_count():]
        ps = []
        for i in team:
            i = i.strip()
            p = Process(target=manager,args=(i,outfile,mode))
            ps.append(p)
            p.start()
            
        for i in ps:
            p.join()