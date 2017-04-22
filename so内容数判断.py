'''
以关键词为搜索词请求so.php，通过分析返回的html源码判断内容数量
'''


import requests,threading,time,os,sys,json,random
from bs4 import BeautifulSoup

def chnls(keyword,soup):
    return len(soup.findAll('h3','Seotitle-h3 clear'))

def pics(keyword,soup):
    n = 0
    for i in soup.findAll('span','picShowIntroduce'):
        i = i.getText()
        if set(keyword) - set(i) == set():
            n += 1
        else:
            continue
    return n

def arts(keyword,soup):
    n = 0
    for i in soup.findAll('a','contentTitle-a'):
        i = i.getText()
        if set(keyword) - set(i) == set():
            n += 1
        else:
            continue
    return n

def ques(keyword,soup):
    n = 0
    for i in soup.findAll(True,'Question-a-title'):
        i = i.getText()
        if set(keyword) - set(i) == set():
            n += 1
        else:
            continue
    return n

def run(keyword):
    r = requests.get('http://so.to8to.com/so.php?keyword=%s' %keyword,proxies=chooseproxy())
    soup = BeautifulSoup(r.text,'lxml')
    try:
        channel = chnls(keyword,soup)
        picture = pics(keyword,soup)
        article = arts(keyword,soup)
        question = ques(keyword,soup)
    except:
        print('关键词：%s 出错'%keyword)
    else:
        lock.acquire()
        try:
            result.write('%s\t%s\t%s\n' %(keyword,channel,picture + article + question))
        finally:
            lock.release()

#获取代理
def chooseproxy():
    proxypool = json.loads(requests.get('http://127.0.0.1:8000/?count=50').text)
    proxy = random.choice(proxypool)
    proxies = {'http':'http://%s:%s' %(proxy[0],proxy[1])}
    return proxies


lock = threading.Lock()
result = open('result.txt','w')
result.write('关键词\t频道数\t完全包含内容数\n')


text = open(sys.argv[1],'r').readlines()
while text:
    lines = text[:os.cpu_count()]        #进程数量
    text = text[os.cpu_count():]
    threads = []
    for keyword in lines:
        keyword = keyword.strip()
        t = threading.Thread(target=run,args=(keyword,))
        threads.append(t)
        t.start()


    for t in threads:
        t.join()

    time.sleep(1)

result.close()