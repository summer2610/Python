#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def convert_to_builtin_type(obj):
    d = {}
    d.update(obj.__dict__)
    return d

class AuthHeader():
    
    def __init__(self, username=None,password=None,token=None,target=None,accessToken=None): 
        self.username=username
        self.password=password
        self.token=token
        self.target=target
        self.accessToken=accessToken
        self.action='API-SDK'
        
            
    def setUsername(self,username):
        self.username=username
    def setPassword(self,password):
        self.password=password
    def setToken(self,token):
        self.token=token
    def setTarget(self,target):
        self.target=target
    def setAccessToken(self,accessToken):
        self.accessToken=accessToken

class JsonEnvelop():
    header=None
    body=None
    
    def __init__(self,aheader=None,abody=None): 
        self.header=aheader
        self.body=abody
    def setHeader(self,header):
        self.header=header
    def setBody(self,body):
        self.body=body

def jsonstr_maker():
    


#记录开始时间，count作用是计数同时作为文件名增量
starttime = time.strftime('%Y/%m/%d %H:%M:%S')
count = 0

