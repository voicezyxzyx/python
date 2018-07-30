import requests
r = requests.get('http://www.wise.xmu.edu.cn/people/faculty')
html = r.content

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'xml')

div_people_list = soup.find('div', attrs={'class': 'people_list'})
a_s = div_people_list.find_all('a', attrs={'target': '_blank'})

for a in a_s:
    url = a['href']
    name = a.get_text()
    print(name, url)

#测试
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get('http://www.baidu.com/')