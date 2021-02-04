# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']
    #start_urls = ['https://www.qiushibaike.com/text/page/{}/'.format(num) for num in range(1,14)]

    def parse(self, response):
        names = response.xpath('//div[@class="hd"]//span[@class="title"][1]/text()').extract()
        stars = response.xpath('//span[@class="rating_num"]/text()').extract()

        for name, star in zip(names, stars):
        yield {
            'name': name,
            'star': star
        }
        # item = DoubanItem()
        # for name, star in zip(names, stars):
        #     item['name'] = name
        #     item['star'] = star
        #     yield item
        # urls = response.xpath('//a/@href').extract()
    #     for url in urls:
    #         yield scrapy.Request(url,callback=self.parse_info)
    # def parse_info(self,response):
    #     pass