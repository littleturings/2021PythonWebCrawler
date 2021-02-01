from urllib.request import Request, build_opener
from fake_useragent import UserAgent
from urllib.request import ProxyHandler


url = "http://httpbin.org/get"
headers = {"User-Agent": UserAgent().chrome}
req = Request(url, headers=headers)

handler = ProxyHandler({"<type>": """(<name>:<password>@)<ip>:<port>"""})

opener = build_opener(handler)
resp = opener.open(req)
print(resp.read().decode())
