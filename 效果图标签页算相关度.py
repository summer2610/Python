import re,requests
from bs4 import BeautifulSoup

def getxgd(keyword,url):
    html = requests.get(url)
    html_code = BeautifulSoup(html.content,'html.parser')
    #keyword = html_code.findAll(attrs={'name':'keywords'})[0]['content'].split(',')[0]
    titles = html_code.findAll('a',href=re.compile('/p.*.html'),title=True)
    count = 0
    pics = len(titles)
    for i in titles:
        title = i.string
        if set(keyword) - set(title) == set():
            count = count + 1
    if count == pics:
        return {'keyword':keyword,'url':url,'相关度':'100%'}
    else:
        return {'keyword':keyword,'url':url,'相关度':str(count/pics*100)[:2] + '%'}

#filepath = input('输入url文件路径，如E:\\urls.txt\n')
rst = open('相关度.txt','w')
for u in open('E:\\Studio\\Python\\urls.txt','r',encoding='utf-8'):
    u = u.split(',')
    try:
        rdict = getxgd(u[0],u[1].strip())
    except:
        continue
    else:
        keyword = rdict['keyword']
        url = rdict['url']
        xgd = rdict['相关度']
        rst.write('%s\t%s\t%s\n' %(keyword,url,xgd))
rst.close()
