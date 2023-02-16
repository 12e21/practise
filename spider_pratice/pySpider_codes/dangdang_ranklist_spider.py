import json
import requests
import re

def main(page):
    url="http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-"\
        +str(page)
    html=request_dangdang(url)
    items = parse_result(html)
    for item in items:
        write_item_to_file(item)

#请求网页源码函数
def request_dangdang(url):
    try:
        response =requests.get(url)
        if response.status_code ==200:
            return response.text
    except requests.RequestException:
        return None
#解析网页源码
def parse_result(html):
    pattern=re.compile('<li>.*?list_num.*?(\d+).*?class="pic".*?img src="(.*?)".*?class="name".*?title="(.*?)".*?class="star".*?style="width:(.*?)".*?class="publisher_info".*?title="(.*?)".*?class="biaosheng".*?<span>(.*?)</span>.*?class="price_n".*?&yen;(.*?)</span>.*?</li>',re.S)
    items=re.findall(pattern,html)
    for item in items:
        yield {
            'rank':item[0],
            'imag':item[1],
            'title':item[2],
            'recommend':item[3],
            'author':item[4],
            'perfect_comment_times':item[5],
            'price':item[6]
        }

#将数据写入文件函数
def write_item_to_file(item):
    print('写入数据中...')
    with open('dangdang_rank.txt','a',encoding='UTF-8') as file:
        file.write(json.dumps(item,ensure_ascii=False)+'\n')
        file.close()

if __name__ =='__main__':
    for i in range(1,20):
        main(i)