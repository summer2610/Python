#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import jieba.analyse
import sys

file = open('result.txt','w')

for i in open(sys.argv[1],'r'):
    i = i.strip().split()
    keys = jieba.analyse.textrank(i[0],topK=5)
    if len(keys) != 0:
        n = 0
        for key in keys:
            if key in i[1]:
                n += 1
            else:
                continue
        file.write('%s\t%s\t%s\n' %(i[0],i[1],n/len(keys)))
    else:
        continue

file.close()
