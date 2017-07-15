import requests,random,time
from bs4 import BeautifulSoup

CITYS = ['bj','sh','gz','sz','nj','dg','tj','hz','zz','suzhou','cq','xa','wh',
        'cd','km','jn','wx','hf','fs','qd','sy','dl','nb','wz','cs','sjz','fz',
        'huizhou','sanya','yw','wf','jining','yt','nt','cz','xz','ny','ly','jz',
        'tz','jx','jh','ts','lf','as','xm','qz','nc','ganzhou','dq','heb','nn',
        'lz','cc','ty','gy','hhht','wlmq','lanzhou','fzlc','nf','zhongshan',
        'zhuhai','shantou','qingyuan','jiangmen','zhaoqing','lianyungang','kunshan',
        'suqian','yangzhou','zhenjiang','huaian','quzhou','huzhou','zhoushan',
        'shaoxing','wuhu','jiujiang','luzhou','zigong','deyang','mianyang','yulin',
        'yinchuan','baotou','zunyi','yancheng','yichang','ahsz','huangshan','haikou',
        'xianyang','kaili','zhuzhou','kaifeng','beihai','xinyang','jiangyin',
        'guilin','shiyan','xiangyang','xiangtan','yueyang','hengyang','chuzhou',
        'changshu','xinxiang','zhangzhou','yangjiang','bijie','qinhuangdao','wlcb',
        'ningde','zibo','tieling','huainan','linyi','anqing','liupanshui','heyuan',
        'sanming','taizhou','hanzhong','baoding','handan','cangzhou','yongzhou',
        'yunfu','zhanjiang','qujing','zhangjiakou','fuyang','liuan','bengbu','changde',
        'jingmen','xining','meishan','ziyang','huangshi','baoji','tongren','guangan',
        'heze','zaozhuang','lishui','yingtan','shaoguan','jilin','baise','maoming',
        'jieyang','weihai','dongying','puer','baoshan','xiaogan','datong','yingkou',
        'jinzhou','fushun','hengshui','benxi','putian','yiyang','chenzhou','huaihua',
        'loudi','zhaoyang','zhangjiajie','xianning','sanmenxia','tonghua','huanggang',
        'zhoukou','shangqiu','xingtai','nanchong','fcg','pds','longyan','chifeng',
        'yibin','yichun','suihua','guigang','linfen','jinzhong','suining','shanwei',
        'binzhou','rizhao','puyang','wuzhou','huludao','775','dandong','liaoyang',
        'chaoyang','maanshan','meizhou','chengde','jiamusi','guangyuan','liaocheng',
        'xuchang','bozhou','yuncheng','zhumadian','taian','jingzhou','fuzhou','yuxi',
        'dezhou','jian','leshan','changzhi','anshun','neijiang','shangrao','tianshui',
        'longnan','hechi','zhaotong','qionghai','laibin','qqhe','weinan','jingdezhen',
        'anyang','dazhou','puning','siping','ankang','ezhou','chongzuo','luohe',
        'nanping','dali','hebi','hegang','mudanjiang','shuangyashan','jixi','chuxiong','hulunbeiershi','xilinguolemeng','xishuangbanna'
]

def get_pages(city,list_type):
    r = requests.get('http://%s.to8to.com/%s/' %(city,list_type))
    s = BeautifulSoup(r.text,'html.parser')
    max_page = int(s.find('a','next').previous_element)
    random_page = 'http://%s.to8to.com/%s/list_%s.html' %(city,list_type,random.randint(1,max_page))
    
    time.sleep(1)
    
    r = requests.get(random_page)
    s = BeautifulSoup(r.text,'html.parser')
    if list_type == 'zwj':
        return [ 'http://%s.to8to.com' %city + x.a['href'] 
                for x in s.findAll('span','fmf_at_title') ]
    if list_type == 'company':
        return [ x['href'] for x in s.findAll('a','zgscl_name') ]

    time.sleep(1)

if __name__ == '__main__':
    for city in CITYS:
        try:
            zwj_urls = get_pages(city,'zwj')
            company_urls = get_pages(city,'company')
        except:
            continue
        else:
            with open('zwj.txt','a+') as z:
                for url in zwj_urls:
                    z.write('%s\n' %url)
            
            with open('company.txt','a+') as c:
                for url in company_urls:
                    c.write('%s\n' %url)
                    
        time.sleep(1)