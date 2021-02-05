### 1. Scrapy - Request 和 Response（请求和响应）

Scrapy 的 `Request` 和 `Response` 对象用于爬网网站。

通常，`Request` 对象在爬虫程序中生成并传递到系统，直到它们到达下载程序，后者执行请求并返回一个 `Response` 对象，该对象返回到发出请求的爬虫程序。

```text
sequenceDiagram
爬虫->>Request: 创建
Request->>Response:获取下载数据
Response->>爬虫:数据
```

### 2. Request 对象

```python
class scrapy.http.Request(url[, callback, method='GET', headers, body, cookies, meta, encoding='utf-8', priority=0, dont_filter=False, errback])
```

一个 `Request` 对象表示一个 HTTP 请求，它通常是在爬虫生成，并由下载执行，从而生成 `Response`

| 参数                   | 说明                                                                                                                                                                                                                 |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| url（string）          | 此请求的网址                                                                                                                                                                                                         |
| callback（callable）   | 将使用此请求的响应（一旦下载）作为其第一个参数调用的函数。有关更多信息，请参阅下面的将附加数据传递给回调函数。如果请求没有指定回调，parse()将使用 spider 的 方法。请注意，如果在处理期间引发异常，则会调用 errback。 |
| method（string）       | 此请求的 HTTP 方法。默认为'GET'。可设置为"GET", "POST", "PUT"等，且保证字符串大写                                                                                                                                    |
| meta（dict）           | 属性的初始值 Request.meta,在不同的请求之间传递数据使用                                                                                                                                                               |
| body（str 或 unicode） | 请求体。如果 unicode 传递了 a，那么它被编码为 str 使用传递的编码（默认为 utf-8）。如果 body 没有给出，则存储一个空字符串。不管这个参数的类型，存储的最终值将是一个 str（不会是 unicode 或 None）。                   |
| headers（dict）        | 这个请求的头。dict 值可以是字符串（对于单值标头）或列表（对于多值标头）。如果 None 作为值传递，则不会发送 HTTP 头.一般不需要                                                                                         |
| encoding               | 使用默认的 'utf-8' 就行。                                                                                                                                                                                            |
| cookie（dict 或 list） | 请求 cookie。这些可以以两种形式发送。                                                                                                                                                                                |

- 使用 dict：

  ```python
  request_with_cookies = Request(url="http://www.sxt.cn/index/login/login.html",)
  ```

- 使用列表：

  ```python
  request_with_cookies = Request(url="http://www.example.com",
                              cookies=[{'name': 'currency',
                                      'value': 'USD',
                                      'domain': 'example.com',
                                      'path': '/currency'}])
  ```

  后一种形式允许定制 cookie 的 `domain` 属性和 `path` 属性。这只有在保存 Cookie 用于以后的请求时才有用

  ```python
  request_with_cookies = Request(url="http://www.example.com",
                              cookies={'currency': 'USD', 'country': 'UY'},
                              meta={'dont_merge_cookies': True})
  ```

#### 将附加数据传递给回调函数

请求的回调是当下载该请求的响应时将被调用的函数。将使用下载的 Response 对象作为其第一个参数来调用回调函数

```python
def parse_page1(self, response):
    item = MyItem()
    item['main_url'] = response.url
    request = scrapy.Request("http://www.example.com/some_page.html",
                             callback=self.parse_page2)
    request.meta['item'] = item
    return request

def parse_page2(self, response):
    item = response.meta['item']
    item['other_url'] = response.url
    return item
```

### 3. 请求子类 FormRequest 对象

`FormRequest` 类扩展了 Request 具有处理 HTML 表单的功能的基础。它使用 `lxml.html` 表单 从 `Response` 对象的表单数据预填充表单字段

```python
class scrapy.http.FormRequest(url[, formdata, ...])
```

本 `FormRequest` 类增加了新的构造函数的参数。其余的参数与 `Request` 类相同，这里没有记录

- 参数：`formdata`（元组的 dict 或 iterable） - 是一个包含 HTML Form 数据的字典（或（key，value）元组的迭代），它将被 url 编码并分配给请求的主体。

该 `FormRequest` 对象支持除标准以下类方法 Request 的方法：

```python
classmethod from_response(response[, formname=None, formid=None, formnumber=0, formdata=None, formxpath=None, formcss=None, clickdata=None, dont_click=False, ...])
```

返回一个新 `FormRequest` 对象，其中的表单字段值已预先 `<form>` 填充在给定响应中包含的 HTML 元素中.

| 参数                       | 说明                                                                                                                                                                         |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| response（Responseobject） | 包含将用于预填充表单字段的 HTML 表单的响应                                                                                                                                   |
| formname（string）         | 如果给定，将使用 name 属性设置为此值的形式                                                                                                                                   |
| formid（string）           | 如果给定，将使用 id 属性设置为此值的形式                                                                                                                                     |
| formxpath（string）        | 如果给定，将使用匹配 xpath 的第一个表单                                                                                                                                      |
| formcss（string）          | 如果给定，将使用匹配 css 选择器的第一个形式                                                                                                                                  |
| formnumber（integer）      | 当响应包含多个表单时要使用的表单的数量。第一个（也是默认）是 0                                                                                                               |
| formdata（dict）           | 要在表单数据中覆盖的字段。如果响应元素中已存在字段，则其值将被在此参数中传递的值覆盖                                                                                         |
| clickdata（dict）          | 查找控件被点击的属性。如果没有提供，表单数据将被提交，模拟第一个可点击元素的点击。除了 html 属性，控件可以通过其相对于表单中其他提交表输入的基于零的索引，通过 nr 属性来标识 |
| dont_click（boolean）      | 如果为 True，表单数据将在不点击任何元素的情况下提交                                                                                                                          |

#### 3.1 请求使用示例

使用 `FormRequest` 通过 HTTP POST 发送数据

如果你想在你的爬虫中模拟 HTML 表单 POST 并发送几个键值字段，你可以返回一个 `FormRequest` 对象（从你的爬虫）像这样：

```python
return [FormRequest(url="http://www.example.com/post/action",
                    formdata={'name': 'John Doe', 'age': '27'},
                    callback=self.after_post)]
```

使用 `FormRequest.from_response()` 来模拟用户登录

网站通常通过元素（例如会话相关数据或认证令牌（用于登录页面））提供预填充的表单字段。进行剪贴时，您需要自动预填充这些字段，并且只覆盖其中的一些，例如用户名和密码。您可以使用 此作业的方法。这里有一个使用它的爬虫示例：

```html
<input type="hidden" /> FormRequest.from_response()
```

```python
import scrapy

class LoginSpider(scrapy.Spider):
    name = 'example.com'
    start_urls = ['http://www.example.com/users/login.php']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'username': 'john', 'password': 'secret'},
            callback=self.after_login
        )

    def after_login(self, response):
        # check login succeed before going on
        if "authentication failed" in response.body:
            self.logger.error("Login failed")
            return

        # continue scraping with authenticated session...
```

### 4 响应对象

```python
class scrapy.http.Response(url[, status=200, headers=None, body=b'', flags=None, request=None])
```

一个 `Response` 对象表示的 HTTP 响应，这通常是下载（由下载），并供给到爬虫进行处理

| 参数                     | 说明                                                                                  |
| ------------------------ | ------------------------------------------------------------------------------------- |
| url（string）            | 此响应的 URL                                                                          |
| status（integer）        | 响应的 HTTP 状态。默认为 200                                                          |
| headers（dict）          | 这个响应的头。dict 值可以是字符串（对于单值标头）或列表（对于多值标头）               |
| body（str）              | 响应体。它必须是 str，而不是 unicode，除非你使用一个编码感知响应子类，如 TextResponse |
| flags（list）            | 是一个包含属性初始值的 Response.flags 列表。如果给定，列表将被浅复制                  |
| request（Requestobject） | 属性的初始值 Response.request。这代表 Request 生成此响应                              |

### 5. 模拟登录

使用的函数

| 函数                        | 说明                                                                                                                    |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| start_requests()            | 可以返回一个请求给爬虫的起始网站，这个返回的请求相当于 start_urls，start_requests()返回的请求会替代 start_urls 里的请求 |
| Request()                   | get 请求，可以设置，url、cookie、回调函数                                                                               |
| FormRequest.from_response() | 表单 post 提交，第一个必须参数，上一次响应 cookie 的 response 对象，其他参数，cookie、url、表单内容等                   |
| yield Request()             | 可以将一个新的请求返回给爬虫执行                                                                                        |

在发送请求时 cookie 的操作

| 操作                                          | 说明                                                                             |
| --------------------------------------------- | -------------------------------------------------------------------------------- |
| meta={'cookiejar':1}                          | 表示开启 cookie 记录，首次请求时写在 Request() 里                                |
| meta={'cookiejar':response.meta['cookiejar']} | 表示使用上一次 response 的 cookie，写在 FormRequest.from_response() 里 post 授权 |
| meta={'cookiejar':True}                       | 表示使用授权后的 cookie 访问需要登录查看的页面                                   |

#### 获取 Scrapy 框架 Cookies

样例代码

`start_requests()`方法，可以返回一个请求给爬虫的起始网站，这个返回的请求相当于 `start_urls`, `start_requests()` 返回的请求会替代 `start_urls` 里的请求

在发送请求时 cookie 的操作

`meta={'cookiejar':1}`表示开启 cookie 记录，首次请求时写在 `Request()` 里

`meta={'cookiejar':response.meta['cookiejar']}`表示使用上一次 Response 的 cookie，写在 `Request` 里 POST 授权

```python
import scrapy
from scrapy import Request
from scrapy import FormRequest


class SxtSpiderSpider(scrapy.Spider):
    name = 'sxt1'
    allowed_domains = ['sxt.cn']

    def start_requests(self):
        return [Request('http://www.sxt.cn/index/login/login.html', meta={'cookiejar': 1}, callback=self.parse)]

    def parse(self, response):
        formdata = {
            "user": "17703181473", "password": "123456"
        }
        return FormRequest(                                        formdata=formdata,
                                        url='http://www.sxt.cn/index/login/login.html',
                                        meta={'cookiejar': response.meta['cookiejar']},
                                        callback=self.login_after)

    def login_after(self, response):
        yield scrapy.Request('http://www.sxt.cn/index/user.html',
                             meta={"cookiejar": response.meta['cookiejar']},
                             callback=self.next)
    def next(self,response):
        print(response.text)
```
