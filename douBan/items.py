# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Top250(scrapy.Item):
    # 电影名称
    move_name = scrapy.Field()
    # 封面
    cover = scrapy.Field()
    # 导演
    dircetor = scrapy.Field()
    # 编剧
    scriptwriter = scrapy.Field()
    # 主演
    protagonist = scrapy.Field()
    # 电影类型
    move_type = scrapy.Field()
    # 制片国家
    move_region = scrapy.Field()
    # 语言
    language = scrapy.Field()
    # 上映时间
    release_date = scrapy.Field()
    # 片长
    run_time = scrapy.Field()
    # 简介
    brief_introduction = scrapy.Field()
    # 评分
    give_mark = scrapy.Field()
    # 播放地址
    movieurls = scrapy.Field()
    # m3u8地址
    m3u8 = scrapy.Field()
    # 评论数量
    number_reviews = scrapy.Field()
    # 播放地址
    play_urls = scrapy.Field()
