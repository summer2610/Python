#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#获取百度搜索结果真实URL

import requests,sys,time

def get_by_url(bdurl):
	return requests.head(bdurl,allow_redirects=False).headers['Location']

if __name__ == '__main__':
	for bdurl in open(sys.argv[1],'r'):
		url = get_by_url(bdurl.strip())
		print(url)
		with open('landpageurl.txt','a+') as f:
			f.write('%s\t%s\n' %(bdurl.strip(),url))