from urllib.request import urlopen

url = "http://www.baidu.com/"

response = urlopen(url)

info = response.read()

# print(info)

# print(info.decode())

# print(response.getcode())

# print(response.geturl())

print(response.info())