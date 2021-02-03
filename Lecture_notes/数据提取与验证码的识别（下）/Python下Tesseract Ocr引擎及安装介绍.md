### 1. Tesseract 介绍

tesseract 是一个 google 支持的开源 ocr 项目

> [GitHub 项目](https://github.com/tesseract-ocr/tesseract)

目前最新的源码可以在这里下载

### 2. Tesseract 安装包下载

[Tesseract 的 release 版本下载](https://github.com/tesseract-ocr/tesseract/wiki/Downloads)，这里需要注意这一段话：

> Currently, there is no official Windows installer for newer versions

意思就是官方不提供最新版 windows 平台安装包，只有相对略老的`3.02.02`版本，[下载地址](https://sourceforge.net/projects/tesseract-ocr-alt/files/)

最新版 `3.03` 和 `3.05` 版本，都是三方维护和管理的安装包，有好几个发行机构，分别是：

- https://www.dropbox.com/s/8t54mz39i58qslh/tesseract-3.05.00dev-win32-vc19.zip?dl=1
- https://github.com/UB-Mannheim/tesseract/wiki
- http://domasofan.spdns.eu/tesseract/

### 3. 小结

1. [官方发布的 3.02 版本下载地址](http://downloads.sourceforge.net/project/tesseract-ocr-alt/tesseract-ocr-setup-3.02.02.exe?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Ftesseract-ocr-alt%2Ffiles%2F&ts=1464880498&use_mirror=jaist)

2. [德国曼海姆大学发行的 3.05 版本下载地址](http://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-setup-3.05.00dev.exe)

3. [imon Eigeldinger (@DomasoFan) 维护的另一个版本](http://3.onj.me/tesseract/)
   值得称道的是，这个网址里还有一个比较详细的说明

### 4. Tesseract ocr 使用

安装之后，默认目录`C:\Program Files (x86)\Tesseract-OCR`，你需要把这个路径放到你操作系统的 path 搜索路径中，否则后面使用起来会不方便。

在安装目录`C:\Program Files (x86)\Tesseract-OCR`下可以看到 `tesseract.exe`这个命令行执行程序

```sh
tesseract 1.png output -l eng -psm 7
```

`-psm 7` 表示用单行文本识别

pagesegmode 值：

- 0 =定向和脚本检测（OSD）。
- 1 =带 OSD 的自动页面分割。
- 2 =自动页面分割，但没有 OSD 或 OCR
- 3 =全自动页面分割，但没有 OSD。（默认）
- 4 =假设一列可变大小的文本。
- 5 =假设一个统一的垂直对齐文本块。
- 6 =假设一个统一的文本块。
- 7 =将图像作为单个文本行处理。
- 8 =把图像当作一个单词。
- 9 =把图像当作一个圆圈中的一个词来对待。
- 10 =将图像作为单个字符处理

`-l eng` 代表使用英语识别
