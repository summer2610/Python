import requests,re,time,threading
from bs4 import BeautifulSoup

lock = threading.Lock()
file = open('rijis.txt','w')
cookies = {'cookies_are':''}

def getDatas(url):
	try:
		r = requests.get(url,cookies=cookies)
		s = BeautifulSoup(r.text,'lxml')
	except:
		pass
	else:
		rijiURLs = s.findAll('a',href=re.compile("http://www.to8to.com/riji/[0-9]+/"))
		for i in rijiURLs:
			i = i['href']
			lock.acquire()
			try:
				file.write('%s\n' %i)
			finally:
				lock.release()

text = ['http://www.to8to.com/trdn/scene2/live_decoration_adminview.php?page=%s' %x  for x in range(1,45933) ]
while text:
	lines = text[:5]
	text = text[5:]
	threads = []
	for url in lines:
		t = threading.Thread(target=getDatas,args=(url,))
		threads.append(t)
		t.start()

	for t in threads:
		t.join()

	time.sleep(3)

file.close()
