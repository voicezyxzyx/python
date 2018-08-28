from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get('http://www.taobao.com')
# lis=browser.find_elements_by_css_selector('.service-bd li')
lis=browser.find_elements(By.CSS_SELECTOR,'.service-bd li')
print(lis)
browser.close()
