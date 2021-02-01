from urllib.request import Request,urlopen
from urllib.parse import quote

def get_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"
    }
    request = Request(url,headers=headers)
    response = urlopen(request)
    return response.read().decode()

def save_html(html,filename):
    with open(filename,"w",encoding="utf-8") as f:
        f.write(html)


def main():
    content = input("请输入要获取哪个贴吧：")
    num = int(input("请输入要获取多少页："))
    for i in range(num):
        url = "http://tieba.baidu.com/f?kw=" +quote(content) + "&ie=utf-8&pn={}".format(i*50)
        html = get_html(url)
        filename = "第"+str(i+1)+"页.html"
        save_html(html,filename)

if __name__ == "__main__":
    main()
