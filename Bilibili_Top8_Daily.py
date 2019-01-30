import requests
import re
import json
from requests.exceptions import RequestException
import time

def get_one_page(url):
    try:
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
        }
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('<div.*?groom-module.*?href=\"(.*?)\".*?title=\"(.*?)\"',re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield{
            'href':'http://www.bilibili.com/'+item[0],
            'title':item[1]
        }

def write_to_file(content):
    with open('BiliTop8result.txt','a',encoding='utf-8') as f:
        print(type(json.dumps(content)))
        f.write(json.dumps(content,ensure_ascii=False)+'\n')

def main():
    url = 'http://www.bilibili.com/'
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__ == '__main__':
    pass

main()
