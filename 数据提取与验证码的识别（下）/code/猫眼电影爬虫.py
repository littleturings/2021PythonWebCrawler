from fake_useragent import UserAgent
import requests
from lxml import etree
from time import sleep
def get_html(url):
    headers = {"User-Agent": UserAgent().chrome,
               "Cookie": "_lxsdk_s=17765b19f80-26c-352-4f7%7C%7C5; __mta=140939917.1612271066247.1612271124211.1612319153850.4; _lxsdk=2C7AD660655711EBA4A23DEBA1CE97F94DB3D352BFF44E1F91689415EB2FC733; _lxsdk_cuid=17762d81bc0c8-0c1bb93a341b02-3f62694b-116d20-17762d81bc0c8; uuid=2C7AD660655711EBA4A23DEBA1CE97F94DB3D352BFF44E1F91689415EB2FC733; uuid_n_v=v1"
               }
    resp = requests.get(url, headers=headers)
    sleep(2)
    if resp.status_code == 200:
        resp.encoding = "utf-8"
        return resp.text
    else:
        print("error:",resp.status_code)
        return


def parse_html(html):
    e = etree.HTML(html)
    lst_url = ["http://maoyan.com{}".format(url) for url in e.xpath("//div[@class='movie-item film-channel']/a/@href")]
    return lst_url

def pares_html(html):
    e = etree.HTML(html)
    name = e.xpath("//h1[@class='name']/text()")
    type = e.xpath("//ul/li[@class='ellipsis'][1]/a[@class='text-link']/text()")
    actors = e.xpath('//div[@class="celebrity-group"]/ul[@class="celebrity-list clearfix"]/li/div/a/text()')
    actors = format_data(actors)
    return {"name":name,"type":type,"actors":actors}


def format_data(actors):
    actor_set = set()
    for actor in actors:
        actor_set.add(actor.strip())
    return actor_set

def main():
    num = int(input("请输入要获取多少页："))
    for page in range(num):
        url = "https://maoyan.com/films?showType=3&offset={}".format(page * 30)
        lst_html = get_html(url)
        lst_url = parse_html(lst_html)
        for url in lst_url:
            info_html = get_html(url)
            movie = pares_html(info_html)
            print(movie)

if __name__ == "__main__":
    main()
