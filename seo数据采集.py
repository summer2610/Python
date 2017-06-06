#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests,json
from bs4 import BeautifulSoup
from UA import makeHeaders
from proxypool import chProxy

def get_indexed(url):
    url = 'http://%s' %url if 'http' not in url else url
    search_url = 'http://www.baidu.com/s?wd=%s&tn=json' %url
    r = reuqests.get(search_url,header=makeHeaders,proxies=chProxy())
    js_text = js.load(r.text)
    landurl = js_text['feed']['entry'][0]['url']
    if url == landurl:
        return 1
    else:
        return 0

def get_ztm(url):
    return requests.get(url).status_code

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

def get_ranks(keyword,url):
    r = requests.get('http://www.baidu.com/s?wd=%s' %keyword,header=makeHeaders(),proxies=chProxy())
    s = BeautifulSoup(r.text,'lxml')
    to8to_ranks = s.findAll(to8to_rank_filter)
    rank_datas = []
    if len(to8to_ranks) != 0:
        for div in to8to_ranks:
            rank_datas.append(get_rank_data(div,keyword))
    else:
        rank_datas.append([keyword,0,''])
    return rank_datas
        


def run(keyword=None,url=None,mode=None):
    if mode == 'ztm':
        return '%s\t%s' %(url,get_ztm(url))
    if mode == 'sl':
        return '%s\t%s' %(url,get_indexed(url))
    elif mode == 'pm':
        pass
        
