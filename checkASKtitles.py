 #!/usr/bin/env python3
 # -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests,time,random,sys
from UA import makeHeaders
from proxypool import chProxy

def choose(num,list):
    newlist = []
    for i in range(num):
        newlist.append(random.choice(list))
    return newlist

def ifOnline(title):
    proxies=chProxy()
    try:
        r = requests.get('http://www.to8to.com/ask/search.php?keyword=' %title,headers=makeHeaders(),proxies=proxies,timeout=5)
        s = BeautifulSoup(r.text,'lxml')
        oltitle = s.findAll('a','ect')[0].em.getText()
    except:
        return ''
    else:
        return oltitle


if __name__ == '__main__': 
    
    print('打开问题总标题库')
    local_datas = open(sys.argv[1],'r').readlines()
    print('随机取1000条数据')
    random_data = choose(1000,local_datas)
    count = 0
    
    print('开始判断')
    for i in random_data:
        askid,*title = i.strip().split(',')
        title = ''.join(title)
        if ifOnline(title) == title:
            count += 1

    print('数据正确率 %s%%' %(count/1000*100))
