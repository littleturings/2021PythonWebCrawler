from urllib.request import Request, urlopen


url = 'https://cart.taobao.com/cart.htm'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
    "Cookie": "<your cookie>"
}

req = Request(url, headers=headers)
resp = urlopen(req)

print(resp.read().decode())
