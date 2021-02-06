from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()

driver.get("https://www.huya.com/g/lol")

while True:
    names = driver.find_elements_by_class_name("nick")
    counts = driver.find_elements_by_class_name("js-num")
    for name, count in zip(names,counts):
        print(name.text,":",count.text)

    if driver.page_source.find("laypage_next") != -1:
        driver.find_element_by_class_name("laypage_next").click()
        sleep(3)
    else:
        break

driver.quit()