import json,requests,random

def chProxy():
    proxypool = json.loads(requests.get('http://127.0.0.1:8000/?count=50',timeout=3).text)
    proxy = random.choice(proxypool)
    proxies = {'http':'http://%s:%s' %(proxy[0],proxy[1])}
    try:
        requests.get('http://httpbin.org/ip',proxies=proxies,timeout=5)
    except:
        chProxy()
    else:
        return proxies
