import requests
from fake_useragent import UserAgent
import re


url = 'https://www.qiushibaike.com/text/'
headers = {"User-Agent": UserAgent().chrome}
resp = requests.get(url, headers=headers)
# print(resp.text)

contents = re.findall(r'<div class="content">\s*<span>\s*(.+)', resp.text)
with open('duanzi.txt', 'a', encoding='utf-8') as f:
    for info in contents:
        f.write(info+"\n\n")
