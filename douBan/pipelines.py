# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from douBan.Movie_scratcher import MovieScrathcer as mc
from scrapy.conf import settings
import pymongo

class DoubanPipeline(object):
    def process_item(self, item, spider):
        return item


class Top250Pipeline(object):
    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DBNAME']
        sheetname = settings['MONGODB_SHEETNAME']

        # 创建Mongo数据库的连接
        client = pymongo.MongoClient(host=host,port=port)
        # 指定数据库的库名
        mydb = client[dbname]
        # 存放数据的表明
        self.mysheet = mydb[sheetname]

    def process_item(self, item, spider):
        play_urls = item['play_urls']
        if play_urls:
            movie_urls, download_load = self.vlink(play_urls)
            item['movie_urls'] = movie_urls
            if download_load:
                item['m3u8_url'] = download_load
        del item['play_urls']
        data = dict(item)
        print(data)
        self.mysheet.insert(data)
        return item

    def vlink(self, play_urls):
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        }
        movie_urls = []
        download_urls = []
        for play_url in play_urls:
            # 提取出播放器名称
            source_name = play_url.xpath('./text()').extract()[0].strip()
            # 从豆瓣的播放地址中提取出源视频地址，并和api拼接组成新的url
            source_url = play_url.xpath('./@href').re('url=(.*)')
            if source_url:
                movie_urls.append({'title': source_name, 'url': mc.movie_watch_on_url(source_url[0])})
                download_urls.append({'title': source_name, 'url': mc.movie_download_on_url(source_url[0], header=header)})
        return movie_urls, download_urls


