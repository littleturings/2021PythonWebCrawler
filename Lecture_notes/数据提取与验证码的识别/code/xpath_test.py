from fake_useragent import UserAgent
import requests
from lxml import etree

url = "https://www.qidian.com/rank/yuepiao"

header = {"User-Agent": UserAgent().chrome}
resp = requests.get(url, headers=header)
# print(resp.text)

e = etree.HTML(resp.text)
names = e.xpath('//div[@class="book-mid-info"]/h4/a/text()')
authors = e.xpath("//p[@class='author']/a[1]/text()")

for name, author in zip(names, authors):
    print(name, ":", author)
