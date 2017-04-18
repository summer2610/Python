'''
用python标准库中的difflib库判断两个文本中各个字符串的相似度，结果以表格输出
'''

#-*- coding:utf-8 -*-
import difflib,codecs,csv

result = open('result.csv','w',newline='',encoding='gbk')
writer = csv.writer(result)

for a in open('a.txt','r',encoding='utf-8'):
    a = a.strip()
    o = (a,)
    bdata = ()
    cdata = ()
    for b in open('b.txt','r',encoding='utf-8'):
        b = b.strip()
        bdata = bdata + (b,)
        c = round(difflib.SequenceMatcher(None,a,b).ratio(),2)
        cdata = cdata + (c,)
    o = o + (max(cdata),) + (bdata[cdata.index(max(cdata))],)
    writer.writerow(o)
result.close()
