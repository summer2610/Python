#
import json,requests,random

def chProxy():
    proxypool = json.loads(requests.get('http://127.0.0.1:8000/?count=50').text)
    proxy = random.choice(proxypool)
    proxies = {'http':'http://%s:%s' %(proxy[0],proxy[1])}
    return proxies