#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
通用的文本匹配脚本

传入需匹配的文本及配置项（代码第66行，分隔符，匹配因子所在列）
传入映射关系及配置项（代码第69行，分隔符，匹配模式）
'''

#import argparse
import sys

def match(map_dict,text,keyword_column,separator,mode):
    '''
    map，表示映射关系的dict，key为词根，值为所属阶段，如 {'公积金':'买房'}
    text，匹配内容的文本list，如
        ['关键词,搜索量,跳出率',
        '公积金怎么查,120,,0.1',
        '公积金如何使用,300,0.5']
    keyword_column，数值，整型，匹配文本中关键词所在的列,如1;
    separator，分隔符字符串，如',';
    mode，匹配模式
    '''
    matched_list = []
    for i in text:
        i = i.strip().split(separator)
        keyword = i[keyword_column-1]
        matched_flag = 0
        for key in list(map_dict.keys()):
            if match_mode(key,keyword,mode):
                matched_list.append('%s%s%s'%(map_dict[key],separator,separator.join(i)))
                print('%s%s%s'%(map_dict[key],separator,separator.join(i)))
                matched_flag = 1
                break
            else:
                matched_flag = 2
        if matched_flag == 2:
            matched_list.append('无匹配项%s%s'%(separator,separator.join(i)))
    return matched_list

def match_mode(a,b,mode):
    '''
    文本匹配模式控制
    0：相等
    1：完全匹配包含，如'客厅' in '客厅装修'
    2：完全包含，如'客厅装修' in '装修客厅图片'
    '''
    if mode == 0:
        return a == b
    elif mode == 1:
        return a in b
    elif mode == 2:
        return set(a) - set(b) == set()
    else:
        return False


#parser = argparse.ArgumentParser()

#parser.add_argument('text_file')
#parser.add_argument('map_file')
#parser.add_argument('keyword_column',type=int)
#parser.add_argument('separator')

#args = parser.parse_args()


if __name__ == '__main__': 
    
    text_file = sys.argv[1]
    map_file = sys.argv[2]
    
    #构建映射字典
    map_dict = {}
    for i in open(map_file,'r').readlines():
        i = i.strip().split(' ')    #分隔符
        map_dict[i[0]] = i[1]

    data = match(map_dict,open(text_file,'r').readlines(),2,'\t',0)    #分隔符、匹配因子所在列、匹配模式
    with open('文本匹配结果.txt','a+') as f:
        for i in data:
            f.write('%s\n' %i)
    
    print('匹配结果输出完毕')