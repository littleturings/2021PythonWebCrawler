from urllib.request import Request, urlopen
import random


url = "http://httpbin.org/get"

user_agents = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5050.400 QQBrowser/10.0.941.400",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    # ...
]

headers = {
    "User-Agent": random.choice(user_agents)
}

req = Request(url, headers=headers)
print(req.get_header("User-agent"))

resp = urlopen(req)
print(resp.read().decode())
