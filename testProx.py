'''
将IP作为代理访问www.ip.cn，如果能访问且返回的不是本地IP，说明此代理IP可用
'''

import requests,sys
from bs4 import BeautifulSoup

def testProxies(ip):
	proxies = {'http':ip}
	try:
		r = requests.get('http://www.ip.cn',proxies=proxies,timeout=4)
	except:
		print('%s\t不可用' %proxies['http'])
	else:
		try:
			rsoup = BeautifulSoup(r.text,'html.parser')
			info=rsoup.findAll('code')[0].get_text()
			location=rsoup.findAll('code')[1].get_text()
		except:
			print('%s get IP info error,%s' %(ip,r.status_code))
		else:
			print('%s\t%s' %(info,location))


if __name__=="__main__":
	testProxies(sys.argv[1])
