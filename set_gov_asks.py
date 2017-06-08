#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep
import sys

def set_displayable(url,browser,mode):
    browser.get(url)
    sleep(3)
    browser.find_elements_by_xpath('//form[@id="form1"]/table//tr//input')[-1].click()
    sleep(0.5)
    if mode == 'show':
        browser.find_element_by_link_text('PC/H5同时显示').click()
    elif mode == 'hide':
        browser.find_element_by_link_text('PC/H5同时不显示').click()
    sleep(0.5)
    browser.switch_to_alert().accept()
    sleep(3)
    browser.switch_to_alert().accept()
    sleep(0.5)
    
if __name__ == '__main__':

    mode = sys.argv[1]
    cookies = sys.argv[2]
    sp,ep = int(sys.argv[3]),int(sys.argv[4])+1
    
    chrome = webdriver.Chrome()
    chrome.get('http://www.to8to.com/trdn/ask_gov.php')
    chrome.add_cookie({'name':'PHPSESSID','value':cookies})
    chrome.get('http://www.to8to.com/trdn/ask_gov.php')


    for url in ['http://www.to8to.com/trdn/ask_gov.php?page=%s' %x for x in range(sp,ep)]:
        set_displayable(url,chrome,mode)