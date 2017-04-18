'''
基于结巴分词
1.先进行搜索引擎分词，然后统计词频
2.再基于TF-IDF算法进行重点关键词抽取，排除停止词等
3.匹配重点关键词词频，排序后输出

用法
命令行运行：python3 [参数] 脚本文件 目标文件 
'''



import jieba.analyse
import jieba,argparse

def cut_for_search(content):
    return jieba.cut_for_search(content)

def cut(content):
    return jieba.cut(content)

def extract_tags(content,topK):
    return jieba.analyse.extract_tags(content,topK=topK)

def cipin(content,mode,top):
    if mode == "s":
        tags = cut_for_search(content)
    elif mode == "c":
        tags = cut(content)
    else:
        raise ValueError("参数错误:mode应该为s(搜索引擎模式分词)或c(精确模式分词)")
    ci_dict = {}
    for i in tags:
        i = i.strip()
        if i not in ci_dict.keys():
            ci_dict[i] = 1
        else:
            ci_dict[i] += 1
    core_ci = extract_tags(content,top)
    unsortdict = {}
    for i in core_ci:
        unsortdict[i] = ci_dict[i]
    for i in sorted(unsortdict.items(),key=lambda item:item[1],reverse=True):
        print('%s\t%d' %(i[0],i[1]))


parser = argparse.ArgumentParser()

parser.add_argument('file')
parser.add_argument('-k','--topK',type = int,default = 20)
parser.add_argument('-m','--mode',type = str,default="s")

args = parser.parse_args()

FILE = args.file
TOP = args.topK
MODE = args.mode

if __name__ == '__main__':
    content = open(FILE,'r').read()
    cipin(content,MODE,TOP)
