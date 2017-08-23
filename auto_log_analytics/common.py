#!/usr/bin/env python3

import datetime
import os
import re
import time
import socket
import requests
from ftplib import FTP
from bs4 import BeautifulSoup


def get_yesterday():
    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    return yesterday.strftime('%Y-%m-%d')

def download_log(date=get_yesterday()):
    log_file = 'baidusearch-%s.tar.gz' %date
    if os.path.isfile(log_file):
        print('''>>> 日志文件已存在，解压''')
        os.system('tar -xzvf %s to8to_baidu.log' %log_file)
    else:    
        ftp = FTP()
        ftp.connect('192.168.3.4',port=11211)
        ftp.login('ftpuser_baidu','''ftpuser_baidu@@)!%''')
        
        print('''>>> 下载日志文件"%s"''' %log_file)
        ftp.retrbinary('RETR ' + log_file,open(log_file,'wb').write)

        print('''>>> 解压日志文件''')
        os.system('tar -xzvf %s to8to_baidu.log' %log_file)    



def extract_ip(log_file):
    ips = []
    for line in open(log_file,'r'):
        ip = re.findall(r'\d+\.\d+\.\d+\.\d+',line)[1]
        if ip not in ips:
            ips.append(ip)
    return ips

def verify_ip(ip):
    try:
        result = socket.gethostbyaddr(ip)
    except:
        r = requests.get('http://ip.t086.com/?ip=%s' %ip)
        s = BeautifulSoup(r.content.decode('gbk'),'lxml')
        if '百度' in s.find('div','bar2 f16').getText():
            return True
        else:
            return False
    else:
        if 'crawl.baidu.com' in result[0]:
            return True
        else:
            return False

if __name__ == '__main__':
    download_log()
    ips = extract_ip('to8to_baidu.log')
    fake_ips = []
    for ip in ips:
        if not verify_ip(ip):
            fake_ips.append(ip)
    print(fake_ips)