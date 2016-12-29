import requests,re,time
from bs4 import BeautifulSoup

result = open('result.txt','w')	#以写模式打开文件result.txt

for keyword in open('起始词.txt','r'):	#for 循环逐个提取关键词
	keyword = keyword.strip().lower()	#把关键词尾部换行符去掉，同时将英文字母转为小写，因为下拉框词默认是小写，防止匹配失败
	xlkurl='http://suggestion.baidu.com/su?wd=%s&sugmode=3&json=1' %keyword	#生成获取下拉框的URL
	askurl='http://www.to8to.com/ask/search.php?keyword=%s' %keyword	#生成获取问答标题的URL

	r = requests.get(xlkurl).text	#访问下拉框URL，获取数据
	rlist = r.split('"')	#把返回的结果以“分隔为列表rlist，方便操作
	clist = []	#建一个空列表准备放下拉框关键词
	for ci in rlist:	#逐个提取rlist的元素
		if (keyword in ci) and (ci not in clist) and (ci != keyword):	#判断是否完全包含、是否重复
			clist.append(ci)	#符合条件则加进clist列表
		else:
			continue	#不符合条件则跳过
	xlkci = ','.join(clist)	#将整个列表转换为字符串

	#下拉框关键词获取完毕
	#time.sleep(1) #暂停1秒

	a = requests.get(askurl).text	#访问问答URL获取数据
	asoup = BeautifulSoup(a,'html.parser')	#将源代码转为BS对象
	thtml = asoup.find('a','ect')	#提取第一个问题标题的HTML代码
	title = re.sub(r'\[.*\]','',thtml.get_text())	#从HTML代码中提取标题，替换掉分类

	#title获取完毕
	#time.sleep(1)	#暂停1秒

	result.write('%s\t%s\t%s\n' %(keyword,xlkci,title))	#将全部结果写入文件

result.close()	#循环结束后关闭文件
