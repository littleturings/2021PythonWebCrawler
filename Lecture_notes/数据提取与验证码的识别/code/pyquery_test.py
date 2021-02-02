from fake_useragent import UserAgent
import requests
from pyquery import PyQuery as pq

url = "http://www.qidian.com/rank/yuepiao?month=01"
headers = {"User-Agent":UserAgent().chrome}
resp = requests.get(url,headers=headers)
#print(resp.text)

doc = pq(resp.text)
names=[a.text for a in doc("h4 a")]
authors_a = doc(".author a")
author_list = []

for num in range(len(authors_a)):
    if num % 2 ==0:
        author_list.append(authors_a[num].text)

for name,author in zip(names,author_list):
    print(name,":",author)

