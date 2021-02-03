from threading import Thread
import requests
from lxml import etree
from fake_useragent import UserAgent
from queue import Queue

class Spider(Thread):
    def __init__(self,url_queue):
        Thread.__init__(self)
        self.url_queue = url_queue

    def run(self):
        while not self.url_queue.empty():
            url = self.url_queue.get()
            print(url)
            header = {"User-Agent": UserAgent().chrome}
            resp = requests.get(url, headers=header)
            e = etree.HTML(resp.text)
            contents = [div.xpath('string(.)').strip() for div in e.xpath("//div[@class='content']")]
            with open('duanzi.txt', 'a', encoding='utf-8') as f:
                for content in contents:
                    f.write(content + "\n")


if __name__ == "__main__":
    base_url = "https://www.qiushibaike.com/text/page/{}/"
    url_queue =Queue()
    for num in range(1,6):
        url_queue.put(base_url.format(num))
    
    for num in range(3):
        spider = Spider(url_queue)
        spider.start()
        