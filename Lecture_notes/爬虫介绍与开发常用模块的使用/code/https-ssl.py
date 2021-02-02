from urllib.request import Request, urlopen
import ssl


url = "https://expired.badssl.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"
}

req = Request(url, headers=headers)
context = ssl._create_unverified_context()
resp = urlopen(req, context=context)

print(resp.read().decode())
