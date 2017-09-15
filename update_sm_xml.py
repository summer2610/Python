#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import requests
from bs4 import BeautifulSoup
from CONFIG import *

#xml文件列表
files = ['new_new_new_hx1.xml','new_new_new_hx5.xml','new_new_new_hx6.xml','new_new_new_style4.xml','new_new_new_style9.xml','new_new_new_style12.xml','new_new_new_style13.xml','new_new_new_style20.xml']

#构建套图图片数字典
img_nums = {}
for x in open('img_nums.txt','r'):
    x = x.strip().split(',')
    img_nums['%s?to8to_from=diff_smtupianxiu' %x[0]] = x[1]

#读取图片数、插入imgsNum标签
for f in files:
    s = BeautifulSoup(open(f,'r'),'xml')
    
    #item列表
    items = s.findAll('item')
    
    img_items = []
    for t in items:
        if t.parent.name == 'datalist':
            img_items.append(t)
    
    #没有imgsNum的item列表
    nonum_items = []
    for t in img_items:
        if t.imgs.next_sibling.next_sibling == None:
            nonum_items.append(t)
    
    #匹配图片数
    for t in nonum_items:
        img_url = t.imgUrl.string
        img_count = img_nums[img_url]
        
        #如果匹配图片数为0，即时请求图片地址获取图片数
        if img_count == '0':
            try:
                img_count = requests.get(
                    img_url,headers=makeHeaders(device='H5'),timeout=5,
                    proxies=getProxy()
                    ).text.count('filename')
            except Exception as e:
                img_count = 0
            else:
                img_count = img_count
        
        #获取到图片后开始插入imgsNum标签
        imgsNum = s.new_tag('imgsNum')
        imgsNum.string = str(img_count)
        t.imgs.insert_after(imgsNum)
        t.imgs.insert_after('\n')
        print('%s\t%s\t' %(img_url,img_count))

    with open('new_%s' %f,'w') as f:
        f.write(str(s))

# BeautifulSoup解析xml时，解析器参数需传入'xml'，否则bs会将其作为html解析
#而html是大小写不敏感的，这会导致解析结果tag名称与原xml对不上
#如原xml tag名为 imgUrl，作为html解析后tag名会变为 imgurl


#BeautifulSoup在原文档插入新tag时，tag不可复用，每次插入都要新建一个tag
#否则只会更换插入tag的位置