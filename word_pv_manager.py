#/usr/bin/env python3

from get_keywords_by_query import *
import mysql.connector
import sys
import time

#连接数据库
conn = mysql.connector.connect(user='root',password='',database='spider_result')
cursor = conn.cursor()

def update_pv(query):
    cursor.execute('SELECT COUNT(*) FROM `seo_keywords` WHERE id > 0')
    count = cursor.fetchall()[0][0]
    
    #查询传入词日均
    #query = sys.argv[1].strip()
    cursor.execute('select pv from seo_keywords where keyword = %s',[query])
    sql_re = cursor.fetchall()
    if sql_re == [] or sql_re[0][0] == None:
        database_pv = 0
    else:
        database_pv = sql_re[0][0]
    
    #如果在数据库查询不到传入词 pv，则在线获取 pv
    if database_pv == 0:
        try:
            api_re = get_keywords(query)
        except:
            print('API 请求失败，等待重试')
            time.sleep(10)
        else:
            query_pv = api_re[0]['pv']
            print(query + '\t' + str(query_pv))
        
            #其他数据写入数据库
            for d in api_re:
                cursor.execute(
                    'INSERT INTO seo_keywords(keyword,pv) values(%s,%s) ON DUPLICATE KEY UPDATE pv = %s;',[d['word'],d['pv'],d['pv']])
            conn.commit()
            time.sleep(3)
            cursor.execute('SELECT COUNT(*) FROM `seo_keywords` WHERE id > 0')
            end_count = cursor.fetchall()[0][0]
            print('已更新 %s 个关键词日均；带日均关键词总数 %s' %(end_count - count,end_count))
    else:
        query_pv = database_pv
        print(query + '\t' + str(query_pv))
    
    

querys = [ x.strip() for x in open(sys.argv[1],'r') ]

for query in querys:
    update_pv(query)

conn.close()
