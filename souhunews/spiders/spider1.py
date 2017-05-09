import scrapy
import time
import json
from bs4 import BeautifulSoup
from souhunews.items import SouhunewsItem
import logging



class souhu1(scrapy.Spider):
    name = 'spider1'
    start_urls=['https://api.m.sohu.com/autonews/cpool/?n=%E6%96%B0%E9%97%BB&s=0&c=20&dc=1']

    def parse(self, response):
        logging.getLogger('one').setLevel(logging.WARNING)
        # print response.body
        thisclass=SouhunewsItem()

        datajson=json.loads(response.body)
        if datajson['data']:
            for i in datajson['data']['news']:
                for j in i:
                    thisclass[j]=i[j]
                    # print i[j]
                print dict(thisclass)
                # logging.log(level=logging.WARNING,msg=thisclass['medium_title'])
                yield thisclass
            url1=response.url.split('&s=')[0]+'&s='+str(int(response.url.split('&s=')[1].split('&',1)[0])+20)+'&'+response.url.split('&s=')[1].split('&',1)[1]

            # print '--------',url1

            yield scrapy.Request(url=url1)


