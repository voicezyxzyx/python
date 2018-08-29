#获取属性
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# browser=webdriver.Chrome()
# url='http://www.zhihu.com/explore'
# browser.get(url)
# logo=browser.find_element_by_id('zh-top-link-logo')
# print(logo)
# print(logo.get_attribute('class'))

#获取文本值

# from selenium import webdriver
# from selenium.webdriver import ActionChains
# browser=webdriver.Chrome()
# url='http://www.zhihu.com/explore'
# browser.get(url)
# input=browser.find_element_by_class_name('zu-top-add-question')
# print(input.text)

#获取ID、位置、标签名、大小
from selenium import webdriver
from selenium.webdriver import ActionChains
browser=webdriver.Chrome()
url='http://www.zhihu.com/explore'
browser.get(url)
input=browser.find_element_by_class_name('zu-top-add-question')
print(input.id)
print(input.location)
print(input.tag_name)
print(input.size)


#  Frame

