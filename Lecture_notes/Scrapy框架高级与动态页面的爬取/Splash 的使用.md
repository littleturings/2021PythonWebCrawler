### 1. Splash 介绍

> Splash 是一个 JavaScript 渲染服务，是一个带有 HTTP API 的轻量级浏览器，同时它对接了 Python 中的 `Twisted` 和 `QT` 库。利用它，我们同样可以实现动态渲染页面的抓取

### 2. 安装

#### 2.1 安装 docker

#### 2.2 拉取镜像

```sh
docker pull scrapinghub/splash
```

#### 2.3 用 docker 运行 scrapinghub/splash

```sh
docker run -p 8050:8050 scrapinghub/splash
```

#### 2.4 查看效果

> 我们在 8050 端口上运行了 Splash 服务，打开`http://localhost:8050/`即可看到其 Web 页面
> ![image](https://note.youdao.com/yws/api/personal/file/366AEA0862FF4B77B584F99F058FD0FE?method=download&shareKey=1becb4e3fd74346d3e247a6cf7d8406d)

### 3 Splash 对象属性

> 上图中 `main()` 方法的第一个参数是 `splash`，这个对象非常重要，它类似于 `Selenium` 中的 `WebDriver` 对象

#### 3.1 images_enabled

> 设置图片是否加载，默认情况下是加载的。禁用该属性后，可以节省网络流量并提高网页加载速度
> 注意的是，禁用图片加载可能会影响 JavaScript 渲染。因为禁用图片之后，它的外层 DOM 节点的高度会受影响，进而影响 DOM 节点的位置
> 因此，如果 JavaScript 对图片节点有操作的话，其执行就会受到影响

```javascript
function main(splash, args)
  splash.images_enabled = false
  splash:go('https://www.baidu.com')
  return {html=splash:html()}
end
```

#### 3.2 plugins_enabled

> 可以控制浏览器插件（如 Flash 插件）是否开启
> 默认情况下，此属性是 `false` ，表示不开启

```javascript
splash.plugins_enabled = true / false;
```

#### 3.3 scroll_position

> 控制页面上下或左右滚动

```javascript
splash.scroll_position = {x=100, y=200}
```

### 4. Splash 对象的方法

#### 4.1 go()

> 该方法用来请求某个链接，而且它可以模拟 `GET` 和 `POST` 请求，同时支持传入请求头、表单等数据

```javascript
ok, reason = splash:go{url, baseurl=nil, headers=nil, http_method="GET", body=nil, formdata=nil}
```

> 返回结果是结果 ok 和原因 reason
> 如果 ok 为空，代表网页加载出现了错误，此时 reason 变量中包含了错误的原因

| 参数        | 含义                                                                                                      |
| ----------- | --------------------------------------------------------------------------------------------------------- |
| url         | 请求的 URL                                                                                                |
| baseurl     | 可选参数，默认为空，表示资源加载相对路径                                                                  |
| headers     | 可选参数，默认为空，表示请求头                                                                            |
| http_method | 可选参数，默认为 `GET` ，同时支持 `POST`                                                                  |
| body        | 可选参数，默认为空，发 `POST` 请求时的表单数据，使用的 `Content-type` 为 `application/json`               |
| formdata    | 可选参数，默认为空，`POST` 的时候的表单数据，使用的 `Content-type` 为 `application/x-www-form-urlencoded` |

```javascript
splash:go{"http://www.sxt.cn", http_method="POST", body="name=17703181473"}
```

#### 4.2 wait()

> 控制页面的等待时间

```javascript
splash:wait{time, cancel_on_redirect=false, cancel_on_error=true}
```

| 参数               | 含义                                                                        |
| ------------------ | --------------------------------------------------------------------------- |
| time               | 等待的秒数                                                                  |
| cancel_on_redirect | 可选参数，默认为 `false` ，表示如果发生了重定向就停止等待，并返回重定向结果 |
| cancel_on_error    | 可选参数，默认为 `false` ，表示如果发生了加载错误，就停止等待               |

```javascript
function main(splash)
    splash:go("https://www.taobao.com")
    splash:wait(2)
    return {html=splash:html()}
end
```

#### 4.3 jsfunc()

> 直接调用 JavaScript 定义的方法，但是所调用的方法需要用双中括号包围，这相当于实现了 JavaScript 方法到 Lua 脚本的转换

```javascript
function main(splash, args)
  splash:go("http://www.sxt.cn")
  local scroll_to = splash:jsfunc("window.scrollTo")
  scroll_to(0, 300)
  return {png=splash:png()}
end
```

#### 4.4 evaljs()与 runjs()

- `evaljs()` 以执行 JavaScript 代码并返回最后一条 JavaScript 语句的返回结果
- `runjs()` 以执行 JavaScript 代码，它与 `evaljs()` 的功能类似，但是更偏向于执行某些动作或声明某些方法

```javascript
function main(splash, args)
  splash:go("https://www.baidu.com")
  splash:runjs("foo = function() { return 'sxt' }")
  local result = splash:evaljs("foo()")
  return result
end
```

#### 4.5 html()

> 获取网页的源代码

```javascript
function main(splash, args)
  splash:go("https://www.bjsxt.com")
  return splash:html()
end
```

#### 4.6 png()

> 获取 PNG 格式的网页截图

```javascript
function main(splash, args)
  splash:go("https://www.bjsxt.com")
  return splash:png()
end
```

#### 4.7 har()

> 获取页面加载过程描述

```javascript
function main(splash, args)
  splash:go("https://www.bjsxt.com")
  return splash:har()
end
```

#### 4.8 url()

> 获取当前正在访问的 URL

```javascript
function main(splash, args)
  splash:go("https://www.bjsxt.com")
  return splash:url()
end
```

#### 4.9 get_cookies()

> 获取当前页面的 `Cookies`

```javascript
function main(splash, args)
  splash:go("https://www.bjsxt.com")
  return splash:get_cookies()
end
```

#### 4.10 add_cookie()

> 当前页面添加 `Cookies`

```javascript
cookies = splash:add_cookie{name, value, path=nil, domain=nil, expires=nil, httpOnly=nil, secure=nil}
```

```javascript
function main(splash)
    splash:add_cookie{"sessionid", "123456abcdef", "/", domain="http://bjsxt.com"}
    splash:go("http://bjsxt.com/")
    return splash:html()
end
```

#### 4.11 clear_cookies()

> 可以清除所有的 `Cookies`

```javascript
function main(splash)
    splash:go("https://www.bjsxt.com/")
    splash:clear_cookies()
    return splash:get_cookies()
end
```

#### 4.12 set_user_agent()

> 设置浏览器的 `User-Agent`

```javascript
function main(splash)
  splash:set_user_agent('Splash')
  splash:go("http://httpbin.org/get")
  return splash:html()
end
```

#### 4.13 set_custom_headers()

> 设置请求头

```javascript
function main(splash)
  splash:set_custom_headers({
     ["User-Agent"] = "Splash",
     ["Site"] = "Splash",
  })
  splash:go("http://httpbin.org/get")
  return splash:html()
end
```

#### 4.14 select()

> 选中符合条件的第一个节点
> 如果有多个节点符合条件，则只会返回一个
> 其参数是 CSS 选择器

```javascript
function main(splash)
  splash:go("https://www.baidu.com/")
  input = splash:select("#kw")
  splash:wait(3)
  return splash:png()
end
```

#### 4.15 send_text()

> 填写文本

```javascript
function main(splash)
  splash:go("https://www.baidu.com/")
  input = splash:select("#kw")
  input:send_text('Splash')
  splash:wait(3)
  return splash:png()
end
```

#### 4.16 mouse_click()

> 模拟鼠标点击操作

```javascript
function main(splash)
  splash:go("https://www.baidu.com/")
  input = splash:select("#kw")
  input:send_text('Splash')
  submit = splash:select('#su')
  submit:mouse_click()
  splash:wait(3)
  return splash:png()
end
```

#### 4.17 代理 Ip

```javascript
function main(splash)
    splash:on_request(function(request)
        request:set_proxy{
            'host':'61.138.33.20',
            'port':808,
            'username':'uanme',
            'password':'passwrod'
        }

     end)

    -- 设置请求头
    splash:set_user_agent("Mozilla/5.0")

    splash:go("https://httpbin.org/get")
    return splash:html()
end
```

### 5 Splash 与 Python 结合

#### 5.1 render.html

> 此接口用于获取 JavaScript 渲染的页面的 HTML 代码，接口地址就是 Splash 的运行地址加此接口名称，例如`http://localhost:8050/render.html`

```python
import requests
url = 'http://localhost:8050/render.html?url=https://www.bjsxt.com&wait=3'
response = requests.get(url)
print(response.text)
```

#### 5.2 render.png

> 此接口可以获取网页截图

```python
import requests

url = 'http://localhost:8050/render.png?url=https://www.jd.com&wait=5&width=1000&height=700'
response = requests.get(url)
with open('taobao.png', 'wb') as f:
    f.write(response.content)
```

#### 5.3 execute

> 最为强大的接口。前面说了很多 Splash Lua 脚本的操作，用此接口便可实现与 Lua 脚本的对接

```python
import requests
from urllib.parse import quote

lua = '''
function main(splash)
    return 'hello'
end
'''

url = 'http://localhost:8050/execute?lua_source=' + quote(lua)
response = requests.get(url)
print(response.text)
```
