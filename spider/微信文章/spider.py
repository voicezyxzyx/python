import requests
from urllib.parse import urlencode
from requests.exceptions import ConnectionError
from pyquery import PyQuery as pq
import pymongo
client=pymongo.MongoClient('localhost')
db=client['weixin']

base_url='http://weixin.sogou.com/weixin?'
headers={
    'Cookie': 'SUID=7A6968DF6119940A000000005B6ED056; SUV=1533988952933378; CXID=7A38D092CE4E107663397042364285BE; ad=6dxhSyllll2bWloNlllllVHcjP1lllllNBD3alllll9lllll9klll5@@@@@@@@@@; ld=JZllllllll2bbHxQlllllVHc9bGlllllTLPIWkllll9lllll9klll5@@@@@@@@@@; LSTMV=153%2C402; LCLKINT=2465; SNUID=4427936E1B1F6E96E8CFD7B81BBFB97C; IPLOC=CN4100; ABTEST=5|1535527916|v1; weixinIndexVisited=1; JSESSIONID=aaaboB8BR0-ZQ4mJRNBvw;sct=3;ppinf=5|1535529754|1536739354|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo1OnZvaWNlfGNydDoxMDoxNTM1NTI5NzU0fHJlZm5pY2s6NTp2b2ljZXx1c2VyaWQ6NDQ6bzl0Mmx1R2dpcTVHSjVOMEdkeVYzM3poTTlITUB3ZWl4aW4uc29odS5jb218; pprdig=HuI3vMF0Ifweo4OAHgHH6vlt9whB8cMLqr75rL7ak2jW9WrIyvQw7q2uLxjQHfc1hc0YeNAFNnty7U0ExlX5zD6JhhndV38iKIS_dxYoGXn45rIjmfuSunI58qvXtDzRZrDBijRRGzN9ZhWadcUViaXo6-7Oe7mGvd2Xve0LvwM; sgid=02-34760559-AVuGUxoks8ajTn7NYXQdrdc; ppmdig=15355297550000009c0982737c449bb6c9a69b5084aaf6e0',
    'Host': 'weixin.sogou.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
keyword='风景'
proxy_pool_url = 'http://127.0.0.1:5000/get'

proxy=None
max_count=5  #请求次数

def get_proxy():
    try:
        response=requests.get(proxy_pool_url)
        if response.status_code==200:
            return response.text
        return None
    except ConnectionError:
        return None


def get_html(url,count=1):
    print('crawing',url)
    print('tring count',count)
    global proxy
    if count>=max_count:
        print("请求次数过多")
        return None
    try:
        if proxy:
            proxies={
                'http':'http://'+proxy
            }
            response=requests.get(url,allow_redirects=False,headers=headers,proxies=proxies)
        else:
            response = requests.get(url, allow_redirects=False, headers=headers)
        if response.status_code==200:
            return response.text
        if response.status_code==302:
            print("302")
            proxy=get_proxy()
            if proxy:
                print("Using proxy",proxy)
                count+=1
                return get_html(url,count)
            else:
                print('Get Proxy Failed')
                return None
    except ConnectionError:
        proxy=get_proxy()
        count+=1
        return get_html(url,count)

def get_index(keyword,page):
    data={
        'query':keyword,
        'type':2,
        'page':page
    }
    queries=urlencode(data)
    url=base_url+queries
    html=get_html(url)
    return html

def parse_index(html):
    doc=pq(html)
    items=doc('.news-box .news-list li .txt-box h3 a').items()
    for item in items:
        yield item.attr('href')

def get_detail(url):
    try:
        response=requests.get(url)
        if response.status_code==200:
            return response.text
        return None
    except ConnectionError:
        return None

def parse_detail(html):
    doc=pq(html)
    title=doc('.rich_media_title').text()
    content=doc('.rich_media_content ').text()
    data=doc('.publish_time').text()
    return {
        'title':title,
        'content':content,
        'data':data
    }

def save_to_Mongo(data):
    if db['articles'].update({'title': data['title']},{'$set':data},True):
        print('Saved to Mongo',data['title'])
    else:
        print("savad to mongo failed",data['title'])


def main():
    for page in range(1,101):
        html=get_index(keyword,page)
        if html:
            article_urls=parse_index(html)
            for article_url in article_urls:
                article_html=get_detail(article_url)
                if article_html:
                    article_data=parse_detail(article_html)
                    print(article_data)
                    save_to_Mongo(article_data)
if __name__=="__main__":
    main()