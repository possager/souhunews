#_*_coding:utf-8_*_



import scrapy
import time
import json
import pymongo
from souhunews.items import SouhunewsCommentsItem



class souhu3(scrapy.Spider):
    name = 'spider3'

    client = pymongo.MongoClient('localhost', 27017)
    COL = client['souhunews']
    DOC = COL['newscontent']
    DOCID = COL['indexnews']

    ids = DOCID.find({}, {'id': 1, '_id': 0})
    distinct=DOC.distinct(key='ownnernewsid')

    urls = []
    for i in ids:
        if i['id'] not in distinct:
            urls.append('https://m.sohu.com/reply/api/comment/list/cursor?newsId=' + str(i['id'])+'&pageSize=15&preCursor=0&isLogin=true')
    start_urls=urls


    def parse3(self,response):

        thisclass=SouhunewsCommentsItem()
        newsid = response.url.split('newsId=')[1].split('&')[0]

        dataunicode=unicode(response.body,encoding='GBK',errors='ignore')
        datajson=json.loads(dataunicode)
        thisid=None
        if datajson['data']['comments']:

            for i in datajson['data']['comments']:
                for j in i:
                    if j==u'from':
                        thisclass['fromwhere']=i['from']
                        pass
                    else:
                        thisclass[j]=i[j]
                thisid=i['comment_id']
                thisclass['ownnernewsid']=newsid

                print thisid
                yield thisclass

            print newsid,'------'
            yield scrapy.Request(url='https://m.sohu.com/reply/api/comment/list/cursor?newsId='+str(newsid)+'&pageSize=15&preCursor='+str(thisid)+'&isLogin=true')

