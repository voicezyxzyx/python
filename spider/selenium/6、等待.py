#隐式等待
# 当使用了隐式等待的时候，如果没有找到元素，将继续等待，超出设定时间后，抛出找不到元素的异常
from selenium import webdriver
browser=webdriver.Chrome()
browser.implicitly_wait(10)
browser.get('https://zhihu.com/explore')
input=browser.find_elements_by_class_name('zu-top-add-question')
print(input)

#显式等待
