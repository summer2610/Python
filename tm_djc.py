#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from bs4 import BeautifulSoup
from multiprocessing import Process,Lock


def getPrice(url,brower):
	try:
		brower.get(url)
		r = brower.page_source
	except:
		#print('请求失败')
		str = url
	else:
		s = BeautifulSoup(r,'lxml')
		good = s.find('div','tb-detail-hd').h1.getText().strip()
		prices = sorted([float(x.getText()) for x in s.findAll('span','tm-price')])
		try:
			str = '%s\t%s' %(prices[0],good)
		except IndexError:
			#print('获取价格失败')
			str = url
	finally:
		lock.acquire()
		if 'http' not in str:
			#print(str)
			result.write('%s\n' %str)
			result.flush()
		else:
			fail.write('%s\n' %str)
			fail.flush()
		lock.release()


if __name__ == '__main__':

	cpus = 3	#CPU数量
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