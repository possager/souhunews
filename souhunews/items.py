# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SouhunewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    comment_count=scrapy.Field()
    created_time=scrapy.Field()
    hotwords=scrapy.Field()
    id=scrapy.Field()
    image_count=scrapy.Field()
    images03=scrapy.Field()
    media=scrapy.Field()
    medium_title=scrapy.Field()
    participation_count=scrapy.Field()
    score=scrapy.Field()
    top_channel_id=scrapy.Field()
    type=scrapy.Field()
    video_count=scrapy.Field()
    view_count=scrapy.Field()

class SouhunewsContentItem(scrapy.Item):
    title=scrapy.Field()
    content=scrapy.Field()
    ownnernews=scrapy.Field()
    publishtime=scrapy.Field()


class SouhunewsCommentsItem(scrapy.Item):
    attachments=scrapy.Field()
    comment_id=scrapy.Field()
    comments=scrapy.Field()
    content=scrapy.Field()
    create_time=scrapy.Field()
    elite=scrapy.Field()
    floor_count=scrapy.Field()
    hide=scrapy.Field()
    hide_floor=scrapy.Field()
    highlight=scrapy.Field()
    ip=scrapy.Field()
    ip_location=scrapy.Field()
    medal=scrapy.Field()
    metadata=scrapy.Field()
    metadataAsJson=scrapy.Field()
    oppose_count=scrapy.Field()
    passport=scrapy.Field()
    quick=scrapy.Field()
    reply_count=scrapy.Field()
    reply_id=scrapy.Field()
    score=scrapy.Field()
    status=scrapy.Field()
    support_count=scrapy.Field()
    top=scrapy.Field()
    user_id=scrapy.Field()

    ownnernewsid=scrapy.Field()
    fromwhere=scrapy.Field()