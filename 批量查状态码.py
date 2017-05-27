import requests,sys,os
from proxypool import chProxy
from multiprocessing import Process

def ztm(url):
    try:
        r = requests.get(url,proxies=chProxy(),timeout=5)
    except:
        print('%s\t失败' %url)
    else:
        print('%s\t%s' %(url,r.status_code))
            

if __name__ == "__main__":
    urls = open(sys.argv[1],'r').readlines()
    while urls:
        team = urls[:os.cpu_count()]
        urls = urls[os.cpu_count():]
        ps = []
        for i in team:
            i = i.strip()
            p = Process(target=ztm,args=(i,))
            ps.append(p)
            p.start()
            
        for i in ps:
            p.join()