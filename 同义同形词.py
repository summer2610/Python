from fuzzywuzzy import fuzz
import shutil,sys

shutil.copyfile('keywords.txt','副本')

rst = open('同义同形词.txt','w')
count = 0

for ci1 in open('keywords.txt','r',encoding='utf-8'):
    ci1 = ci1.strip()
    tytxc = [ci1]
    count = count + 1
    for ci2 in open('副本','r',encoding='utf-8'):
        ci2 = ci2.strip()
        if ci1 == ci2:
            continue
        elif fuzz.partial_token_set_ratio(ci1,ci2) == 100 and ci1[:2] == ci2[:2] and (set(ci2) - set(ci1)) - set('装修设计效果图大全0123456789图片欣赏') == set():
            tytxc.append(ci2)
    for i in tytxc:
        rst.write('%s\t%s\n' %(i,count))
    tytxc = []

rst.close()
