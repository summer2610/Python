
import requests,re,time,threading
from bs4 import BeautifulSoup

lock = threading.Lock()
result = open('result.txt','w')


def xlk(keyword):
    xlkurl='http://suggestion.baidu.com/su?wd=%s&sugmode=3&json=1' %keyword
    try:
        r = requests.get(xlkurl)
    except:
        return ''
    else:
        #print(r.status_code)
        t = r.text
        rlist = t.split('"')    
        clist = []    
        for ci in rlist:    
            if (keyword in ci) and (ci not in clist) and (ci != keyword):    
                clist.append(ci)    
            else:
                continue    
        return ','.join(clist)    

    
def ask(keyword):
    askurl='http://www.to8to.com/ask/search.php?keyword=%s' %keyword
    try:
        a = requests.get(askurl).text
    except:
        return ''
    else:
        asoup = BeautifulSoup(a,'lxml')    
        thtml = asoup.find('a','ect')    
        try:
            return re.sub(r'\[.*\]','',thtml.get_text())
        except:
            return ''


def getData(keyword):
    xlkci = xlk(keyword)
    title = ask(keyword)
    
    lock.acquire()
    try:
        result.write('%s\t%s\t%s\n' %(keyword,xlkci,title))
    finally:
        lock.release()

        
text = open('起始词.txt','r').readlines()
while text:
    lines = text[:5]    #进程数量
    text = text[5:]
    threads = []
    for keyword in lines:
        keyword = keyword.strip().lower()
        t = threading.Thread(target=getData,args=(keyword,))
        threads.append(t)
        t.start()
        time.sleep(0.5)    #间隔时间，单位秒

    for t in threads:
        t.join()

result.close()
print('采集完毕')