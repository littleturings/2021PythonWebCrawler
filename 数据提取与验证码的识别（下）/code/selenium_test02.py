from selenium import webdriver

def headless():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    chrome = webdriver.Chrome(chrome_options = options)
    chrome.get('http://www.baidu.com')
    print(chrome.page_source)
    chrome.quit()

def Proxy():
    options = webdriver.ChromeOptions()
    options.add_argument('--proxy-server=http://124.77.24.212:10032')
    chrome = webdriver.Chrome(chrome_options = options)
    chrome.get("http://httpbin.org/get")
    print(chrome.page_source)
    chrome.quit()

if __name__ == '__main__':
    Proxy()