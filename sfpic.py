import requests,time
from bs4 import BeautifulSoup

def dlimg(imgurl):
    time.sleep(2)
    filename = imgurl.split('/')[-2]
    r = requests.get(imgurl)
    with open('/media/sf_E_DRIVE/sfpic/%s' %filename,'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
    print('%s 下载完毕' %filename)

#获取URL
URLS = []
for page in range(0,100):
	try:
		time.sleep(2)
		a = requests.get('http://newhouse.sz.fang.com/house/s/b9%s/' %page)
	except:
		continue
	else:
		ahtml = a.content.decode('gbk')
		asoup = BeautifulSoup(ahtml,'html.parser')	
		for div in asoup.findAll('div','nlcd_name'):
			if 'http' in div.a['href']:
				URLS.append(div.a['href'])
print('楼盘URL获取完毕')

#获取图片
for url in URLS:
	try:
		time.sleep(2)
		b = requests.get(url)
	except:
		continue
	else:
		bhtml = b.content.decode('gbk')
		bsoup = BeautifulSoup(bhtml,'html .parser')
		IMGS = [ div.img['src'] for div in bsoup.findAll('div','bannerbg_pos')]
		for imgurl in IMGS:
			try:
				dlimg(imgurl)
			except:
				continue

print('图片下载完成')
