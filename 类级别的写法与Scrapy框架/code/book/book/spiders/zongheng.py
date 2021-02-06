import scrapy

class ZonghengSpider(scrapy.Spider):
    name = 'zongheng'
    allowed_domains = ['zongheng.com']
    start_urls = ['http://www.zongheng.com/rank/details.html?rt=1&d=1&p=1']

    def parse(self, response):
        names = response.xpath("//div[@class='rank_d_b_name']/@title").extract()
        authors = response.xpath("//div[@class='rank_d_b_cate']/@title").extract()
        print(names)
        print(authors)
        books = []
        for name, author in zip(names,authors):
            books.append({
                "name":name,
                "author":author
            })
        return books
