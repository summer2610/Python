import codecs
import csv
cigen = open('C:/Users/ginson.wang/Downloads/词根.txt','r',encoding='UTF-8')
text = cigen.readlines()

yifenlei = open('C:/Users/ginson.wang/Downloads/py已分类.csv','w')

for q in open('C:/Users/ginson.wang/Downloads/问句.csv','r'):
    ques = q.strip('\n')
    for c in text:
        ci = c.strip().split(',')[0]
        dfl = c.strip().split(',')[1]
        xfl = c.strip().split(',')[2]
        if ques.find(ci) > -1:
            ostr = '%s,%s,%s\n' %(ques,dfl,xfl)
            yifenlei.write(ostr)
yifenlei.close()                                                       
