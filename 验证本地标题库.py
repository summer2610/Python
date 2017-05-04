 #!/usr/bin/env python3
 # -*- coding: utf-8 -*-
 
 
'''
作用
判断本地标题库中的数据与线上数据是否一致
 
用法
命令行运行 python3 checkASKtitles.py 总标题文件 判断数量（默认为20）
'''

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
        r = requests.get('http://www.to8to.com/ask/search.php?keyword=%s' %title,timeout=5)#,headers=makeHeaders(),proxies=proxies)
        s = BeautifulSoup(r.text,'lxml')
        all_titles = [ x.getText().split(']')[1] for x in s.find('div','question_list').findAll('a','ect')]
    except:
        print('%s 出错' %title)
    else:
        for t in all_titles:
            if title in t:
                return t
            else:
                continue
        return ''

if __name__ == '__main__': 
    
    print('打开问题总标题库')
    local_datas = open(sys.argv[1],'r').readlines()
    
    try:
        int(sys.argv[2])
    except:
        nums = 20
    else:
        nums = int(sys.argv[2])
    
    print('随机取%d条数据进行验证' %nums)
    random_data = choose(nums,local_datas)
    
    count = 0
    
    print('开始验证')
    for i in random_data:
        askid,*title = i.strip().split(',')
        title = ''.join(title)
        oltitle = ifOnline(title)
        
        print('%s %s' %(oltitle,title))
        
        if oltitle:
            count += 1
        print('数据正确率 %s%%' %(int(count/nums*100)))
        time.sleep(1)