# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from souhunews.items import SouhunewsItem
from souhunews.items import SouhunewsCommentsItem
from souhunews.items import SouhunewsContentItem



class SouhunewsPipeline(object):
    def __init__(self):
        self.client=pymongo.MongoClient('localhost',27017)
        self.COL=self.client['souhunews']
        self.DOC=self.COL['indexnews']
        self.DOC2=self.COL['comments']
        self.DOC3=self.COL['content']


    def process_item(self, item, spider):
        if isinstance(item,SouhunewsItem):
            distinct=self.DOC.distinct(key='id')
            if item['id'] not in distinct:
                self.DOC.insert(dict(item))

        elif isinstance(item,SouhunewsContentItem):
            distinct = self.DOC3.distinct(key='ownnernews')
            if item['ownnernews'] not in distinct:
                self.DOC3.insert(dict(item))

        elif isinstance(item, SouhunewsCommentsItem):
            distinct = self.DOC2.distinct(key='comment_id')
            if item['comment_id'] not in distinct:
                self.DOC2.insert(dict(item))

