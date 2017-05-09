import scrapy
import time
import json
from bs4 import BeautifulSoup
import pymongo
from souhunews.items import SouhunewsContentItem
import logging




class souhu2(scrapy.Spider):
    name = 'spider2'

    client=pymongo.MongoClient('localhost',27017)
    COL=client['souhunews']
    DOC=COL['newscontent']
    DOCID=COL['indexnews']


    ids=DOCID.find({},{'id':1,'_id':0})
    urls=[]
    for i in ids:
        urls.append('https://m.sohu.com/n/'+str(i['id'])+'/')
    # print urls[1:10]
    start_urls= urls


    def parse2(self,response):
        logging.getLogger('one').setLevel(logging.WARNING)


        print 'in parse2========'
        ownnernews=response.url

        if '404_auto' not in ownnernews:
            datasoup=BeautifulSoup(response.body,'lxml')

            thisclass=SouhunewsContentItem()
            title=datasoup.select('body > section.article-wrapper > article > h1')
            publishtime=datasoup.select('body > section.article-wrapper > article > div.article-info.clearfix > span')
            content=datasoup.select('body > section.article-wrapper > article > p')

            contenttext=''
            for i in content:
                contenttext+=i.text
            print contenttext
            print title[0].text
            print publishtime[0].text
            print ownnernews
            if title:
                thisclass['title']=title[0].text
            thisclass['content']=contenttext
            if publishtime:
                thisclass['publishtime']=publishtime[0].text
            thisclass['ownnernews']=ownnernews
            yield thisclass

        else:
            print 'news has been deleted'
