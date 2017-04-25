#
import json,requests,random

def chProxy():
    proxypool = json.loads(requests.get('http://127.0.0.1:8000/?count=50').text)
    proxy = random.choice(proxypool)
    proxies = {'http':'http://%s:%s' %(proxy[0],proxy[1])}
    try:
        requests.get('http://www.ip.cn',proxies=proxies)
    except:
        chProxy()
    else:
        return proxies