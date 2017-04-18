# -*- coding: utf-8 -*-

import time,sys,os
from selenium import webdriver
from bs4 import BeautifulSoup
from multiprocessing import Process,Lock


def getPrice(url,brower):
    rstr = url
    try:
        brower.get(url)
        r = brower.page_source
    except:
        #print('请求失败')
        rstr = url
    else:
        s = BeautifulSoup(r,'html.parser')
        try:
            good = s.find('div','tb-detail-hd').h1.getText().strip()
            prices = sorted([float(x.getText()) for x in s.findAll('span','tm-price')])
        except:
            #print('获取价格失败')
            rstr = url
        else:
            rstr = '%s\t%s' %(prices[0],good)
    finally:
        return rstr


if __name__ == '__main__':
    
    urls = open(sys.argv[1],'r').readlines()
    result = open('result.txt','w')
    fail = open('fail.txt','w')
    
    b = webdriver.PhantomJS(service_log_path=os.path.devnull)
    for i in urls:
        r = getPrice(i.strip(),b)
        if 'https' in r:
            fail.write('%s\n' %r)
        else:
            result.write('%s\n' %r)
        time.sleep(0.5)
            
    b.close()
    b.quit()
    
    result.close()
    fail.close()
    
    
    #多进程模式代码，服务器均为单核，无法启用多进程
    # cpus = 1    #CPU数量
    # browers = []
    # for i in range(cpus):
        # browers.append(webdriver.PhantomJS())
    # result = open('result.txt','w')
    # fail = open('fail.txt','w')
    
    # urls = open('tm_urls.txt','r').readlines()[:5]
    #lock = Lock()
    
    # while len(urls) != 0:
        # lines = urls[:cpus]
        # urls = urls[cpus:]
        # ps = []
        # for i in lines:
            # p = Process(target=getPrice,args=(i.strip(),browers[lines.index(i)]))                
            # ps.append(p)
            # p.start()

        # for p in ps:
            # p.join()


    # for i in browers:
        # i.close()
        # i.quit()

    # result.close()
    # fail.close()
