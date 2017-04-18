from jieba import analyse
from fuzzywuzzy import fuzz
import sys

def new(str):
	list = analyse.textrank(str)	#或者用 analyse.extract_tags函数
	list.sort()
	return ''.join(list)

def uniq(a,b,ratio=70):
	newa = new(a)
	newb = new(b)
	if fuzz.token_sort_ratio(newa,newb) >= ratio:
		return '重复'
	else:
		return '不重复'

if __name__ == "__main__":
	city_words = open(sys.argv[1],'r').readlines()
	tmp = city_words[:]
	
	for a in city_words:
		for b in tmp:
			if a != b and uniq(a,b) == '重复':
				city_words.pop(city_words.index(b))
				tmp.pop(tmp.index(b))

	rst = open('rst.txt','w')
	for c in tmp:
		rst.write('%s\n' %c)
	
	rst.close()