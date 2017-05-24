#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests,sys,re,time
from bs4 import BeautifulSoup
from UA import makeHeaders
from proxypool import chProxy

def to8to_rank_filter(tag):
    if tag.name != 'div' or not tag.has_attr('class'):
        return False
    elif 'resultc-container' not in ''.join(tag.attrs['class']):
        return False
    elif not tag.find('a','c-showurl',string=re.compile('to8to.com/ask/k')):
        return False
    else:
        return True

def getLocation(landurl):
    r2 = requests.get(landurl,allow_redirects=False)
    return r2.headers['Location']

def getRankdata(tag,keyword):
    rank = div.attrs['id']
    rankurl = div.find('a','c-showurl').attrs['href']
    landurl = getLocation(rankurl)
    return [keyword,rank,landurl]

if __name__ == "__main__":
    startURLs = open(sys.argv[1],'r').readlines()
    
    for url in startURLs:
        url = url.strip()
        keyword = re.split('[=&]',url)[-3]
        try:
            r = requests.get(url,headers=makeHeaders(),proxies=chProxy(),timeout=5)
        except:
            startURLs.append(url)
        else:
            s = BeautifulSoup(r.text,'lxml')
            to8toRanks = s.findAll(to8to_rank_filter)
            with open('result.txt','a+') as f:
                if len(to8toRanks) != 0:
                    for div in to8toRanks:
                        rankdata = getRankdata(div,keyword)       
                        f.write('%s\n' %'\t'.join(rankdata))
                        f.flush()
                        print('\t'.join(rankdata))
                else:
                    f.write('%s\t0\n' %keyword)
                    print('%s\t无排名' %keyword)
    
        time.sleep(1)
