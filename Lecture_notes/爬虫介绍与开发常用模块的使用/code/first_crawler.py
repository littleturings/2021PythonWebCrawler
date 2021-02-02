from urllib.request import urlopen


url = "http://www.baidu.com/"

resp = urlopen(url)
info = resp.read()

# tip: 将有大量输出 善用断点查看
print(info)
print(info.decode())
print(resp.getcode())
print(resp.geturl())
print(resp.info())
