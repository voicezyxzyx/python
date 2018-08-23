import requests
import re
import json
import time
from multiprocessing import Pool
def get_one_page(url):
    headers={
        'User-Agent': 'User-Agent  Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    }
    response=requests.get(url,headers=headers)
    if response.status_code==200:
        return response.text
    else:
        return None

def parse_one_page(html):
    pattern=re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S)
    items=re.findall(pattern,html)
    for item in items:
        yield {
            'index':item[0],
            'image':item[1],
            'title':item[2],
            'actor':item[3],
            'time':item[4].strip()[5:],
            'score':item[5].strip()+item[6].strip()
        }
def write_to_file(content):
    with open('maoyan.txt','a',encoding='utf-8') as f:

        f.write(json.dumps(content,ensure_ascii=False)+'\n')
def main(offset):
    url="http://maoyan.com/board/4?offset="+str(offset)
    html=get_one_page(url)
    for item in parse_one_page(html):
        write_to_file(item)

if __name__=='__main__':
    #单进程爬取：
    time1 = time.time()
    for i in range(10):
        main(offset=i*10)
        time2 = time.time()
    print("总时间为：%.2f"%(time2-time1))
    #多进程爬取
    # pool = Pool()
    # time1=time.time()
    # pool.map(main, [i * 10 for i in range(10)])
    # time2=time.time()
    # print("总时间为：%.2f"%(time2-time1))

