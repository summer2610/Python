#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep
import sys

def set_show(url,browser):
    browser.get(url)
    sleep(3)
    chrome.find_elements_by_xpath('//form[@id="form1"]/table//tr//input')[-1].click()
    sleep(0.5)
    chrome.find_element_by_link_text('删除').click()
    sleep(0.5)
    chrome.switch_to_alert().accept()
    sleep(3)
    chrome.switch_to_alert().accept()
    sleep(1)
    
if __name__ == '__main__':
    
    #sp,ep = int(sys.argv[2]),int(sys.argv[3])
    chrome = webdriver.Chrome()
    chrome.get('http://www.to8to.com/trdn/ask_gov.php')
    sleep(3)
    chrome.add_cookie({'name':'PHPSESSID','value':sys.argv[1]})
    chrome.get('http://www.to8to.com/trdn/ask_gov.php')
    sleep(3)
    #for url in ['http://www.to8to.com/trdn/ask_gov.php?page=%s' %x for x in range(sp,ep)]:
    #for i in range(32):
        #set_show(url,chrome)
        #set_show('http://www.to8to.com/trdn/ask_gov.php?atype=0&fValue=&stime=2017-06-05&ftime=2017-06-06&page=1',chrome)
