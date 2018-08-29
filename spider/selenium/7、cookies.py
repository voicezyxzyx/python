from selenium import webdriver
import time
browser=webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
print(browser.get_cookies())
browser.add_cookie({'name':'name','domain':'www.zhihu.com','value':'germey'})
browser.delete_all_cookies()
print(browser.get_cookies())


#浏览器选项卡创建和切换
# browser.execute_script('window.open()')
# print(browser.window_handles)
# time.sleep(5)
# browser.switch_to_window(browser.window_handles[1])