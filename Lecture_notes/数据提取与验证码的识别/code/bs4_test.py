from bs4 import BeautifulSoup
# from bs4.element import Comment

html = '''
#以以下代码为例子
<title id="someid">知乎</title>
<div class='info' float='left'>Welcome to Zhihu</div>
<div class='info' float='right'>
    <span>Good Good Study</span>
    <a href='www.zhihu.com'></a>
    <strong><!--没用--></strong>
</div>
'''

soup = BeautifulSoup(html, "lxml")
print("--------获取标签--------")
print(soup.title)
print(soup.div)
print(soup.span)
print("------属性-------")
print(soup.div.attrs)
print(soup.div.get("class"))
print(soup.div["float"])
print(soup.a["href"])
print("-----内容------")
print(type(soup.title.string))
print(soup.title.text)
print(soup.strong.string)
print("-----findall------")
print(soup.find_all("div"))
print(soup.find_all(id="someid"))
print(soup.find_all(class_="info"))
