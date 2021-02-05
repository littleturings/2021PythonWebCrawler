### 问题

有的页面的很多部分都是用 JS 生成的，而对于用 scrapy 爬虫来说就是一个很大的问题，因为 scrapy 没有 JS engine，所以爬取的都是静态页面，对于 JS 生成的动态页面都无法获得

[官网](http://splash.readthedocs.io/en/stable/)

### 解决方案

- 利用第三方中间件来提供 JS 渲染服务： `scrapy-splash` 等
- 利用 `webkit` 或者基于 `webkit` 库

> Splash 是一个 Javascript 渲染服务。它是一个实现了 HTTP API 的轻量级浏览器，Splash 是用 Python 实现的，同时使用 `Twisted` 和 `QT`。`Twisted` 和 `QT` 用来让服务具有异步处理能力，以发挥 `webkit` 的并发能力

### 安装

1. pip 安装 `scrapy-splash` 库

   ```sh
   pip install scrapy-splash
   ```

2. `scrapy-splash` 使用的是 Splash HTTP API， 所以需要一个 `splash instance` ，一般采用 `docker` 运行 splash，所以需要安装 `docker`

3. 安装并运行 `docker`

4. 拉取镜像

   ```sh
   docker pull scrapinghub/splash
   ```

5. 用 `docker` 运行 `scrapinghub/splash`

   ```sh
   docker run -p 8050:8050 scrapinghub/splash
   ```

6. 配置 splash 服务（以下操作全部在 settings.py）:

   1. 使用 splash 解析，要在配置文件中设置 splash 服务器地址：

      ```python
      SPLASH_URL = 'http://localhost:8050/'
      ```

   2. 将 splash middleware 添加到 `DOWNLOADER_MIDDLEWARE` 中

      ```python
      DOWNLOADER_MIDDLEWARES = {
          'scrapy_splash.SplashCookiesMiddleware': 723,
          'scrapy_splash.SplashMiddleware': 725,
          'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
      }
      ```

   3. Enable `SplashDeduplicateArgsMiddleware`

      ```python
      SPIDER_MIDDLEWARES = {
          'scrapy_splash.SplashDeduplicateArgsMiddleware': 100
      }
      ```

      这个中间件需要支持 `cache_args` 功能; 它允许通过不在磁盘请求队列中多次存储重复的 Splash 参数来节省磁盘空间。如果使用 Splash 2.1+，则中间件也可以通过不将这些重复的参数多次发送到 Splash 服务器来节省网络流量

   4. 配置消息队列所使用的过滤类

      ```python
      DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
      ```

   5. 配置消息队列需要使用的类

      ```python
      HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
      ```

### 样例

```python
import scrapy
from scrapy_splash import SplashRequest


class DoubanSpider(scrapy.Spider):
    name = 'douban'

    allowed_domains = ['douban.com']


def start_requests(self):
    yield SplashRequest('https://movie.douban.com/typerank?type_name=剧情&type=11&interval_id=100:90', args={'wait': 0.5})


def parse(self, response):
    print(response.text)

```
