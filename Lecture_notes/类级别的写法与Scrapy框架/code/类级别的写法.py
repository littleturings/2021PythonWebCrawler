from fake_useragent import UserAgent
import requests
from lxml import etree

#发送请求
class Downloader():
    def do_download(self,url):
        print(url)
        headers = {"User-Agent": UserAgent().chrome}
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            resp.encoding = "utf-8"
            return resp.text

#解析数据
class Parser():
    def do_parse(self,html):
        e = etree.HTML(html)
        contents = [div.xpath("string(.)").strip() for div in e.xpath("//div[@class='content']")]
        urls = ["https://www.qiushibaike.com{}".format(url) for url in e.xpath("//ul[@class='pagination']/li/a/@href")]
        return contents,urls

#数据保存
class DataOutPut():
    def do_save(self,datas):
        with open('duanzi1.txt',"a",encoding="utf-8") as f:
            for data in datas:
                f.write(data + "\n")

#URL管理器
class URLManager():
    def __init__(self):
        self.new_url = set()
        self.old_url = set()

    #加入一个URL
    def add_new_url(self,url):
        if url is not None and url != "" and url not in self.old_url:
            self.new_url.add(url)

    #加入多个URl
    def add_new_urls(self,urls):
        for url in urls:
            self.add_new_url(url)
    #获取一个URL
    def get_new_url(self):
        url = self.new_url.pop()
        self.old_url.add(url)
        return url
    #获取URL数量
    def get_new_url_size(self):
        return len(self.new_url)
    #获取是否还有URL
    def have_new_url(self):
        return self.get_new_url_size() > 0

#调度器
class Scheduler():
    def __init__(self):
        self.downloader = Downloader()
        self.parser = Parser()
        self.data_out_put = DataOutPut()
        self.url_manager = URLManager()

    def start(self,url):
        self.url_manager.add_new_url(url)
        while self.url_manager.have_new_url():
            url = self.url_manager.get_new_url()
            html = self.downloader.do_download(url)
            datas,urls = self.parser.do_parse(html)
            self.data_out_put.do_save(datas)
            self.url_manager.add_new_urls(urls)

if __name__ == '__main__':
    scheduler = Scheduler()
    url = "https://www.qiushibaike.com/text/"
    scheduler.start(url)

