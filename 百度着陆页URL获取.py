#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
通过搜索结果地址获取着陆页真实URL
'''

import requests,sys,time

def get_by_url(bdurl):
    return requests.head(bdurl,allow_redirects=False).headers['Location']

if __name__ == '__main__':
    for bdurl in open(sys.argv[1],'r'):
        url = get_by_url(bdurl.strip())
        print(url)
        with open(sys.argv[2],'a+') as f:
            f.write('%s\t%s\n' %(bdurl.strip(),url))
