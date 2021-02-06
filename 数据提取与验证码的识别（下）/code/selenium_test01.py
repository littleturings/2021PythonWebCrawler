from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()

url = "https://cn.bing.com/"
driver.get(url)

driver.find_element_by_id("sb_form_q").send_keys("Python")

driver.find_element_by_id("sb_form_go").click()

sleep(3)

html = driver.page_source
print(html)
driver.quit()
