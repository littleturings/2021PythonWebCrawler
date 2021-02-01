from urllib.request import Request,urlopen
import random
url = "http://www.baidu.com/"

user_agents = [
    "ua1",
    "ua2",
    "ua3"
]

headers = {
    "user-Agents": choice(user_agents)
}
#headers = {
#    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
#}

req = Request(url,headers = headers)
#print(req.get_header("User-Agent"))

resp = urlopen(req)

print(resp.read().decode())