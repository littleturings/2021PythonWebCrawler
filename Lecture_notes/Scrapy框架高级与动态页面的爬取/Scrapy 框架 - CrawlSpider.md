### 1. CrawlSpiders

#### 原理图

```text
sequenceDiagram
start_urls ->>调度器: 初始化url
调度器->>下载器: request
下载器->>rules: response
rules->>数据提取: response
rules->>调度器: 新的url
```

通过下面的命令可以快速创建 `CrawlSpiders` 模板 的代码

```sh
scrapy genspider -t crawl 文件名 (allowed_url)
```

首先再说下 Spider，它是所有爬虫的基类，而 `CrawSpiders` 就是 `Spider` 的派生类。对于设计原则是只爬取 `start_url` 列表中的网页，而从爬取的网页中获取 link 并继续爬取的工作 `CrawlSpider` 类更适合

### 2. Rule 对象

`Rule` 类与 `CrawlSpider` 类都位于 `scrapy.contrib.spiders` 模块中

```python
class scrapy.contrib.spiders.Rule (
link_extractor, callback=None,cb_kwargs=None,follow=None,process_links=None,process_request=None )
```

参数含义：

- `link_extractor` 为 `LinkExtractor` ，用于定义需要提取的链接
- `callback`：当 `link_extractor` 获取到链接时参数所指定的值作为回调函数

  - `callback` 参数使用注意：
    当编写爬虫规则时，请避免使用 `parse` 作为回调函数。于 `CrawlSpider` 使用 `parse` 方法来实现其逻辑，如果您覆盖了 `parse` 方法，`CrawlSpider` 将会运行失败

- `follow`：指定了根据该规则从 `response` 提取的链接是否需要跟进。当 `callback` 为 `None`,默认值为 `True`
- `process_links`：主要用来过滤由 `link_extractor` 获取到的链接
- `process_request`：主要用来过滤在 `rule` 中提取到的 `request`

### 3.LinkExtractors

#### 3.1 概念

> 顾名思义，链接提取器

#### 3.2 作用

`Response` 对象中获取链接，并且该链接会被接下来爬取
每个 `LinkExtractor` 有唯一的公共方法是 `extract_links()` ，它接收一个 `Response` 对象，并返回一个 `scrapy.link.Link` 对象

#### 3.3 使用

```python
class scrapy.linkextractors.LinkExtractor(
    allow = (),
    deny = (),
    allow_domains = (),
    deny_domains = (),
    deny_extensions = None,
    restrict_xpaths = (),
    tags = ('a','area'),
    attrs = ('href'),
    canonicalize = True,
    unique = True,
    process_value = None
)
```

| 主要参数        | 说明                                                                 |
| --------------- | -------------------------------------------------------------------- |
| allow           | 满足括号中“正则表达式”的值会被提取，如果为空，则全部匹配。           |
| deny            | 与这个正则表达式(或正则表达式列表)不匹配的 URL 一定不提取。          |
| allow_domains   | 会被提取的链接的 domains。                                           |
| deny_domains    | 一定不会被提取链接的 domains。                                       |
| restrict_xpaths | 使用 xpath 表达式，和 allow 共同作用过滤链接(只选到节点，不选到属性) |

##### 3.3.1 查看效果（shell 中验证)

首先运行

```sh
scrapy shell http://www.fhxiaoshuo.com/read/33/33539/17829387.shtml
```

继续 import 相关模块

```python
from scrapy.linkextractors import LinkExtractor
```

提取当前网页中获得的链接

```python
link = LinkExtractor(restrict_xpaths=(r'//div[@class="bottem"]/a[4]')
```

调用 LinkExtractor 实例的 extract_links()方法查询匹配结果

```python
link.extract_links(response)
```

##### 3.3.2 查看效果 CrawlSpider 版本

```python
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from xiaoshuo.items import XiaoshuoItem


class XiaoshuoSpiderSpider(CrawlSpider):
    name = 'xiaoshuo_spider'
    allowed_domains = ['fhxiaoshuo.com']
    start_urls = ['http://www.fhxiaoshuo.com/read/33/33539/17829387.shtml']

    rules = [
        Rule(LinkExtractor(restrict_xpaths=(r'//div[@class="bottem"]/a[4]')), callback='parse_item'),]

    def parse_item(self, response):
        info = response.xpath("//div[@id='TXT']/text()").extract()
        it = XiaoshuoItem()
        it['info'] = info
        yield it

```

注意

```python
rules = [
    Rule(LinkExtractor(restrict_xpaths=(r'//div[@class="bottem"]/a[4]')), callback='parse_item'),
]
```

- `callback` 后面函数名用引号引起
- 函数名不能是 `parse`
- 格式问题
