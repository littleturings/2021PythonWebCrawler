#import ssl
from urllib.request import Request,urlopen
from urllib.parse import quote
#ssl._create_default_https_context = ssl._create_unverified_context
arg = "孙嘉乐"

url = "https://www.baidu.com/s?wd={}".format(quote(arg))

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
}

req = Request(url,headers = headers)
#print(req.get_header("User-Agent"))
resp = urlopen(req)
print(resp.read().decode())