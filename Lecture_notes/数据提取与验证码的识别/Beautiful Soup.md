### 1. Beautiful Soup 的简介

> Beautiful Soup 提供一些简单的、python 式的函数用来处理导航、搜索、修改分析树等功能。它是一个工具箱，通过解析文档为用户提供需要抓取的数据，因为简单，所以不需要多少代码就可以写出一个完整的应用程序。
> Beautiful Soup 自动将输入文档转换为 Unicode 编码，输出文档转换为 utf-8 编码。你不需要考虑编码方式，除非文档没有指定一个编码方式，这时，Beautiful Soup 就不能自动识别编码方式了。然后，你仅仅需要说明一下原始编码方式就可以了。
> Beautiful Soup 已成为和 lxml、html6lib 一样出色的 python 解释器，为用户灵活地提供不同的解析策略或强劲的速度

[官网](https://beautifulsoup.readthedocs.io/zh_CN/latest/)

### 2. Beautiful Soup 安装

> Beautiful Soup 3 目前已经停止开发，推荐在现在的项目中使用 Beautiful Soup 4，不过它已经被移植到 BS4 了,也就是说导入时我们需要 import bs4

```sh
pip install beautifulsoup4
```

> Beautiful Soup 支持 Python 标准库中的 HTML 解析器,还支持一些第三方的解析器，如果我们不安装它，则 Python 会使用 Python 默认的解析器，lxml 解析器更加强大，速度更快，推荐安装

| 解析器           | 使用方法                                                            | 优势                                                                      | 劣势                                            |
| ---------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------- | ----------------------------------------------- |
| Python 标准库    | BeautifulSoup(markup, “html.parser”)                                | 1. Python 的内置标准库 2. 执行速度适中 3.文档容错能力强                   | Python 2.7.3 or 3.2.2)前 的版本中文档容错能力差 |
| lxml HTML 解析器 | BeautifulSoup(markup, “lxml”)                                       | 1. 速度快 2.文档容错能力强                                                | 需要安装 C 语言库                               |
| lxml XML 解析器  | BeautifulSoup(markup, [“lxml”, “xml”]) BeautifulSoup(markup, “xml”) | 1. 速度快 2.唯一支持 XML 的解析器 3.需要安装 C 语言库                     |
| html5lib         | BeautifulSoup(markup, “html5lib”)                                   | 1. 最好的容错性 2.以浏览器的方式解析文档 3.生成 HTML5 格式的文档 4.速度慢 | 不依赖外部扩展                                  |

### 3. 创建 Beautiful Soup 对象

```python
from bs4 import BeautifulSoup

bs = BeautifulSoup(html,"lxml")
```

### 4. 四大对象种类

> Beautiful Soup 将复杂 HTML 文档转换成一个复杂的树形结构,每个节点都是 Python 对象,所有对象可以归纳为 4 种:

- Tag
- NavigableString
- BeautifulSoup
- Comment

#### 4.1 Tag 是什么？通俗点讲就是 HTML 中的一个个标签

例如：`<div>` `<title>`

使用方式：

```html
#以以下代码为例子
<title>知乎</title>
<div class="info" float="left">Welcome to SXT</div>
<div class="info" float="right">
  <span>Good Good Study</span>
  <a href="www.bilibili.com"></a>
  <strong><!--没用--></strong>
</div>
```

##### 4.1.1 获取标签

```python
#以lxml方式解析
soup = BeautifulSoup(info, 'lxml')
print(soup.title)
# <title>bilibili</title>
```

**注意**

> 相同的标签只能获取第一个符合要求的标签

##### 4.1.2 获取属性

```python
#获取所有属性
print(soup.title.attrs)
#class='info' float='left'

#获取单个属性的值
print(soup.div.get('class'))
print(soup.div['class'])
print(soup.a['href'])
#info
```

#### 4.2 NavigableString 获取内容

```python
print(soup.title.string)
print(soup.title.text)
#bilibili
```

#### 4.3 BeautifulSoup

> BeautifulSoup 对象表示的是一个文档的全部内容.大部分时候,可以把它当作 Tag 对象,它支持 遍历文档树 和 搜索文档树 中描述的大部分的方法.
> 因为 BeautifulSoup 对象并不是真正的 HTML 或 XML 的 tag,所以它没有 `name` 和 `attribute` 属性.但有时查看它的 `.name` 属性是很方便的,所以 BeautifulSoup 对象包含了一个值为 `[document]` 的特殊属性 `.name`

```python
print(soup.name)
print(soup.head.name)
# [document]
# head
```

#### 4.4 Comment

> Comment 对象是一个特殊类型的 NavigableString 对象，其实输出的内容仍然不包括注释符号，但是如果不好好处理它，可能会对我们的文本处理造成意想不到的麻烦

```python
if type(soup.strong.string)==Comment:
    print(soup.strong.prettify())
else:
    print(soup.strong.string)
```

### 5 搜索文档树

> Beautiful Soup 定义了很多搜索方法,这里着重介绍 2 个: find() 和 find_all() .其它方法的参数和用法类似,请同学们举一反三

#### 5.1 过滤器

> 介绍 find_all() 方法前,先介绍一下过滤器的类型 ,这些过滤器贯穿整个搜索的 API.过滤器可以被用在 tag 的 name 中,节点的属性中,字符串中或他们的混合中

##### 5.1.1 字符串

> 最简单的过滤器是字符串.在搜索方法中传入一个字符串参数,Beautiful Soup 会查找与字符串完整匹配的内容,下面的例子用于查找文档中所有的`<div>`标签

```python
#返回所有的div标签
print(soup.find_all('div'))
```

> 如果传入字节码参数,Beautiful Soup 会当作 UTF-8 编码,可以传入一段 Unicode 编码来避免 Beautiful Soup 解析编码出错

##### 5.1.2 正则表达式

如果传入正则表达式作为参数,Beautiful Soup 会通过正则表达式的 match() 来匹配内容

```python
#返回所有的div标签
print (soup.find_all(re.compile("^div")))
```

##### 5.1.3 列表

> 如果传入列表参数,Beautiful Soup 会将与列表中任一元素匹配的内容返回

```python
#返回所有匹配到的span a标签
print(soup.find_all(['span','a']))
```

##### 5.1.4 keyword

> 如果一个指定名字的参数不是搜索内置的参数名,搜索时会把该参数当作指定名字 tag 的属性来搜索,如果包含一个名字为 id 的参数,Beautiful Soup 会搜索每个 tag 的”id”属性

```python
#返回id为welcom的标签
print(soup.find_all(id='welcom'))
```

##### 5.1.4 True

> True 可以匹配任何值,下面代码查找到所有的 tag,但是不会返回字符串节点

##### 5.1.5 按 CSS 搜索

> 按照 CSS 类名搜索 tag 的功能非常实用,但标识 CSS 类名的关键字 class 在 Python 中是保留字,使用 class 做参数会导致语法错误.从 Beautiful Soup 的 4.1.1 版本开始,可以通过 class\_ 参数搜索有指定 CSS 类名的 tag

```python
# 返回class等于info的div
print(soup.find_all('div',class_='info'))
```

#### 5.1.6 按属性的搜索

```python
soup.find_all("div", attrs={"class": "info"})
```

### 6. CSS 选择器（扩展）

soup.select(参数)

| 表达式                      | 说明                                          |
| --------------------------- | --------------------------------------------- |
| tag                         | 选择指定标签                                  |
| \*                          | 选择所有节点                                  |
| #id                         | 选择 id 为 container 的节点                   |
| .class                      | 选取所有 class 包含 container 的节点          |
| li a                        | 选取所有 li 下的所有 a 节点                   |
| ul + p                      | (兄弟)选择 ul 后面的第一个 p 元素             |
| div#id > ul                 | (父子)选取 id 为 id 的 div 的第一个 ul 子元素 |
| table ~ div                 | 选取与 table 相邻的所有 div 元素              |
| a[title]                    | 选取所有有 title 属性的 a 元素                |
| a[class=”title”]            | 选取所有 class 属性为 title 值的 a            |
| a[href*=”sxt”]              | 选取所有 href 属性包含 sxt 的 a 元素          |
| a[href^=”http”]             | 选取所有 href 属性值以 http 开头的 a 元素     |
| a[href$=”.png”]             | 选取所有 href 属性值以.png 结尾的 a 元素      |
| input[type="redio"]:checked | 选取选中的 hobby 的元素                       |
