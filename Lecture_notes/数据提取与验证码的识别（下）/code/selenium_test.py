from selenium import webdriver

#构造我们的浏览器
chrome = webdriver.Chrome()
url = "http://www.baidu.com"
chrome.get(url)

chrome.save_screenshot("baidu.png")
html = chrome.page_source
print(html)
chrome.quit()