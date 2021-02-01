from urllib.request import Request,urlopen

url = 'https://cart.taobao.com/cart.htm?spm=a1z0d.6639537.0.0.19d47484KIDotv&from=mini&pm_id=1501036000a02c5c3739'

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
    "Cookie": "cna=xkGeGLxdQEcCAbfBJ1VJS+tw; cdpid=UUBc%2FvRDkzzv8A%3D%3D; cnaui=2845646859; aui=2845646859; sca=9aa6d2b6; tbsa=f0847fc83bad620652693618_1612151901_2; atpsida=3855b886fdb15b78a41c92ee_1612151901_2"
}
    
req = Request(url,headers=headers)

resp=urlopen(req)

print(resp.read().decode())