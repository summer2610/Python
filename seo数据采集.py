#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests,json
from bs4 import BeautifulSoup
from UA import makeHeaders
from proxypool import chProxy

def get_indexed(url):
    search_url = 'http://www.baidu.com/s?wd=%s&tn=json' %url
    r = reuqests.get(search_url,header=makeHeaders,proxies=chProxy())
    js_text = js.load(r.text)
    landurl = js_text['feed']['entry'][0]['url']
