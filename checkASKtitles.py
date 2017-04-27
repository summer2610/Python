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

def getTitle(id):
    try:
        r = requests.get('http://www.to8to.com/ask/k%s.html' %id,headers=makeHeaders(),proxies=chProxy(),timeout=5)
        s = BeautifulSoup(r.text,'lxml')
        title = s.find('title').getText().split('_')[0]
    except:
        title = ''
        return title
    else:
        return title


if __name__ == '__main__': 
    
    print('打开问题总标题库')
    local_datas = open(sys.argv[1],'r').readlines()
    print('随机取1000条数据')
    random_data = choose(1000,local_datas)
    count = 0
    
    print('开始判断')
    for i in random_data:
        askid,*title = i.strip().split(',')
        title = ','.join(title)
        online_title = getTitle(askid)
        print('%s:%s' %(askid,online_title))
        time.sleep(0.5)
        if title == online_title:
            count += 1
    
    print('数据正确率 %s%%' %(count/1000*100))
