# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Top250Spider(CrawlSpider):
    name = 'top250'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250?start=0&filter=']

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+&filter=')),
        Rule(LinkExtractor(allow=r'/subject/\d+/', restrict_xpaths='//div[@class="hd"]/a'), callback='parse_item'),
    )

    def parse_item(self, response):
        item = scrapy.Field()
        info = response.xpath('//div[@id="info"]')
        # 电影名称
        item['move_name'] = info.xpath('//h1/span/text()').extract()[0]
        # 封面
        item['cover'] = info.xpath('//img[@rel="v:image"]/@src').extract()[0]
        # 导演
        item['dircetor'] = info.xpath('./span[1]/span[2]/a/text()').extract()[0]
        # 编剧
        item['scriptwriter'] = info.xpath('./span[2]/span[2]/a/text()').extract()
        # 主演
        item['protagonist'] = info.xpath('./span[3]/span[2]/a/text()').extract()
        # 电影类型
        item['move_type'] = info.xpath('./span[@property="v:genre"]/text()').extract()
        # 制片国家
        item['move_region'] = info.xpath('./span[1]/span[2]/a/text()').extract()[0]
        # 语言
        item['language'] = info.re(r'<span class="pl">制片国家/地区:</span>(.*)<br>')[0].strip()
        # 上映时间
        item['release_date'] = info.xpath('./span[@property="v:initialReleaseDate"]/text()').extract()[0]
        # 片长
        item['run_time'] = info.xpath('./span[@property="v:runtime"]/text()').extract()
        # 简介
        item['brief_introduction'] = "".join(response.xpath('//span[@property="v:summary"]/text()').extract()).replace(
            ' ', '')
        # 评分
        item['give_mark'] = response.xpath('//strong[@class="ll rating_num"]/text()').extract()[0]
        # 评论数量
        item['number_reviews'] = response.xpath('//div[@class="mod-hd"][1]/h2/span/a/text()').re('\d+')[0]
        # 播放地址
        item['play_urls'] = response.xpath('//div[@class="gray_ad"]//a[@class="playBtn"]')
        yield item
