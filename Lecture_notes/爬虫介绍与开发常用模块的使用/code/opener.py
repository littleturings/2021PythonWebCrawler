from urllib.request import Request
from fake_useragent import UserAgent
from urllib.request import build_opener


url = "http://httpbin.org/get"

headers = {
    "User-Agent": UserAgent().chrome
}

req = Request(url, headers=headers)

opener = build_opener()
resp = opener.open(req)
print(resp.read().decode())
