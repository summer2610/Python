#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
将IP作为代理访问www.baidu.cn，如果返回状态码为200则代理IP有效
'''

import requests,sys
from multiprocessing import Process,Lock

def testProxies(ip):
    proxies = {'http':ip}
    try:
        r = requests.head('http://www.ip.cn',proxies=proxies,timeout=10)
    except:
        print('%s\t不可用' %proxies['http'])
    else:
        if r.status_code == 200:
            print('%s\t可用' %proxies['http'])
            lock.acquire()
            with open('代理IP验证结果.txt','a+') as f:
                f.write('%s\n' %ip)
            lock.release()
        else:
            print('%s\t不可用' %proxies['http'])


if __name__=="__main__":
    
    lock = Lock()
    ips = open(sys.argv[1],'r').readlines()
    
    while ips:
    
        t = ips[:4]
        ips = ips[4:]
        ps = []
        
        for ip in t:
            p = Process(target=testProxies,args=(ip.strip(),))
            ps.append(p)
            p.start()
            
        for p in ps:
            p.join()
