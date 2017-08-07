#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests,time,random
from CONFIG import makeHeaders,getProxy

url = 'https://ssl-api.720yun.com/api/pano/56fjk5mvzy4/like'

referers = [
    'http://720yun.com/t/56fjk5mvzy4?from=singlemessage&isappinstalled=0&pano_id=3536502',
    'http://720yun.com/t/56fjk5mvzy4?from=singlemessage&isappinstalled=0&pano_id=3536488',
    'http://720yun.com/t/56fjk5mvzy4?from=singlemessage&isappinstalled=0&pano_id=3536487',
    'http://720yun.com/t/56fjk5mvzy4?from=singlemessage&isappinstalled=0&pano_id=3536465',
    'http://720yun.com/t/56fjk5mvzy4?from=singlemessage&isappinstalled=0&pano_id=3536463'
    ]

mobile_UAs = [
    'Mozilla/5.0 (Linux; Android 6.0; HUAWEI CRR-UL00 Build/HUAWEICRR-UL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043220 Safari/537.36 MicroMessenger/6.5.7.1041 NetType/4G Language/zh_CN',
    'Mozilla/5.0 (Linux; Android 5.0.2; Redmi Note 2 Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043221 Safari/537.36 V1_AND_SQ_7.0.0_676_YYB_D QQ/7.0.0.3135 NetType/WIFI WebP/0.3.0 Pixel/1920',
    'Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; R7Plusm Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.2.942 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 7.0; LON-AL00 Build/HUAWEILON-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043221 Safari/537.36 V1_AND_SQ_7.0.0_676_YYB_D QQ/7.0.0.3135 NetType/4G WebP/0.3.0 Pixel/1440',
    'Mozilla/5.0 (Linux; Android 6.0.1; vivo X9Plus Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043221 Safari/537.36 V1_AND_SQ_7.0.0_676_YYB_D QQ/7.0.0.3135 NetType/4G WebP/0.3.0 Pixel/1080',
    'Mozilla/5.0 (iPhone 92; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.4.1 Mobile/14F89 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1',
    'Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-G9280 Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.9.941 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; OPPO R9s Plus Build/MMB29M) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.7.6) WindVane/8.0.0 1080X1920 GCanvas/1.4.2.21',
    'Mozilla/5.0 (iPhone 6; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.4.1 Mobile/14F89 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1',
    'Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; ZUK Z1 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.4 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 7.0; MHA-AL00 Build/HUAWEIMHA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baiduboxapp/8.6.1 (Baidu; P1 7.0)',
    'Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; MI MAX Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.7.8',
    'Mozilla/5.0 (iPhone 6p; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.4.1 Mobile/14F89 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1',
    'Mozilla/5.0 (Linux; Android 5.1.1; OPPO A53 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043220 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/4G Language/zh_CN',
    'Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; PRO 5 Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.2.942 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 MicroMessenger/6.5.8 NetType/4G Language/zh_CN',
    'Mozilla/5.0 (Linux; Android 7.0; MHA-AL00 Build/HUAWEIMHA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043220 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/4G Language/zh_CN',
    'Mozilla/5.0 (Linux; Android 4.2.2; NX403A Build/JDQ39; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baidubrowser/7.10.12.0 (Baidu; P1 4.2.2)',
    'Mozilla/5.0 (Linux; Android 5.1; OPPO A59m Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baiduboxapp/8.6.1 (Baidu; P1 5.1)',
    'Mozilla/5.0 (Linux; Android 5.1.1; OPPO A33 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043220 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN',
    'Mozilla/5.0 (Linux; Android 6.0; PE-TL10 Build/HuaweiPE-TL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/7.4 baiduboxapp/8.5 (Baidu; P1 6.0)',
    'Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; 2014813 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.5.7',
    'Mozilla/5.0 (Linux; Android 6.0; KNT-UL10 Build/HUAWEIKNT-UL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043220 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/3G Language/zh_CN',
    'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; 2014501 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.5.14',
    'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; SM-N9006 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.5 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; Le X820 Build/FEXCNFN5902303111S) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.1.0.870 U3/0.8.0 Mobile Safari/534.30',
    'Mozilla/5.0 (Linux; Android 6.0.1; OPPO R9s Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043220 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/4G Language/zh_CN',
    'Mozilla/5.0 (iPhone 6s; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.4.1 Mobile/14F89 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1',
    'Mozilla/5.0 (Linux; Android 6.0.1; vivo X9 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baiduboxapp/8.6.5 (Baidu; P1 6.0.1)',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B100 MicroMessenger/6.5.8 NetType/4G Language/zh_CN'
]
    
    
opt_headers = {
    'Host':'ssl-api.720yun.com',
    'Connection':'keep-alive',
    'Access-Control-Request-Method':'POST',
    'Origin':'http://720yun.com',
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
    'Access-Control-Request-Headers':'app-key',
    'Accept':'*/*',
    'Referer':'http//720yun.com/t/56fjk5mvzy4?from=singlemessage&isappinstalled=0&pano_id=3536487',
    'Accept-Encoding':'gzip, deflate, sdch, br',
    'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'}

def make_headers():
    return {
        'Host':'ssl-api.720yun.com',
        'Connection':'keep-alive',
        'Content-Length':'0',
        'Accept':'application/json,text/plain, */*',
        'Origin':'http://720yun.com',
        'App-Key':'eByjUyLDG2KtkdhuTsw2pY46Q3ceBPdT',
        'Referer':random.choice(referers),
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
        'User-Agent':random.choice(mobile_UAs)}

def do_like(s):
    proxy = getProxy()
    requests.options(url,headers=opt_headers,proxies=proxy)
    time.sleep(0.3)
    requests.post(url,headers=make_headers(),proxies=proxy)
    print('点赞+1')

if __name__ == '__main__':

    total_likes = 0

    while True:
        wait_time = random.randint(90,180)
        try:
            do_like(wait_time)
        except Exception as e:
            print(e)
            time.sleep(5)
        else:
            total_likes += 1
            print('已点赞 %s ' %total_likes)
        time.sleep(wait_time)
    
