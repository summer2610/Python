#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gzip,tarfile,os,sys,shutil

def un_tar(file_name):
    tar = tarfile.open(file_name)
    names = tar.getnames()
    os.mkdir(file_name + "_files")
    for name in names:
        tar.extract(name,file_name+ "_files/")
    tar.close()

un_tar(sys.argv[1])
log_dir = sys.argv[1] + "_files"
log_file = sys.argv[1] + "_files/to8to_baidu.log"

site_log = {}

#将日志记录构建为字典，key为抓取URL，值为状态码
for log_line in open(log_file,'r').readlines():
    line = log_line.split(' ')
    site_log[line[0]+line[7]] = line[9]

#通过URL提取记录并写入文件
for url in open(sys.argv[2],'r').readlines():
    url = url.strip()
    try:
        record = site_log[url]
    except KeyError:
        record = '未抓取'
    else:
        pass
    finally:
        with open('抓取记录.txt','a+') as f:
            f.write('%s\t%s\n' %(url,record))


#清理现场
comm = input('是否删除解压的日志文件?   y/n\n')
if comm in ['y','yes','Y']:
    shutil.rmtree(log_dir)