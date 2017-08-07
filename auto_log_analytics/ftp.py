#!/usr/bin/env python3

from ftplib import FTP
import time
import os

ftp = FTP(
    host='192.168.3.4:11211',
    user='ftpuser_baidu',
    passwd='''ftpuser_baidu@@)!%'''
)


yes_log_name = '%s.tar.gz' %time.strftime('%Y-%m-%d',time.localtime())

ftp.login()
ftp.retrbinary(yes_log_name,open(yes_log_name,'wb').write)

os.system('tar -xzvf %s baidu_to8to.log' %yes_log_name)



