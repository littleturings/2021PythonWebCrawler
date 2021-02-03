### 1 Scrapy 提取项目

从网页中提取数据，Scrapy 使用基于 XPath 和 CSS 表达式的技术叫做选择器。以下是 XPath 表达式的一些例子：

- 这将选择 HTML 文档中的 `<head>` 元素中的 `<title>` 元素

  ```text
  /html/head/title
  ```

- 这将选择 `<title>` 元素中的文本

  ```text
  /html/head/title/text()
  ```

- 这将选择所有的 `<td>` 元素

  ```text
  //td
  ```

- 选择 div 包含一个属性 class=”slice” 的所有元素

  ```text
  //div[@class=”slice”]
  ```

选择器有四个基本的方法，如下所示：

| S.N.            | 方法 & 描述                                                   |
| --------------- | ------------------------------------------------------------- |
| extract()       | 它返回一个 unicode 字符串以及所选数据                         |
| extract_first() | 它返回第一个 unicode 字符串以及所选数据                       |
| re()            | 它返回 Unicode 字符串列表，当正则表达式被赋予作为参数时提取   |
| xpath()         | 它返回选择器列表，它代表由指定 XPath 表达式参数选择的节点     |
| css()           | 它返回选择器列表，它代表由指定 CSS 表达式作为参数所选择的节点 |

### 2 Scrapy Shell

如果使用选择器想快速的到到效果，我们可以使用 Scrapy Shell

```sh
scrapy shell "http://www.163.com"
```

注意 windows 系统必须使用双引号

#### 2.1 举例

从一个普通的 HTML 网站提取数据，查看该网站得到的 XPath 的源代码。检测后，可以看到数据将在 UL 标签，并选择 li 标签中的 元素。

代码的下面行显示了不同类型的数据的提取：

- 选择 li 标签内的数据：

```python
response.xpath('//ul/li')
```

- 对于选择描述：

```python
response.xpath('//ul/li/text()').extract()
```

- 对于选择网站标题：

```python
response.xpath('//ul/li/a/text()').extract()
```

- 对于选择网站的链接：

```python
response.xpath('//ul/li/a/@href').extract()
```
