import time
from bs4 import BeautifulSoup
import json
import requests
from urllib.parse import quote

def write_data(price,title,comment):
    f = open('货架.txt','a')
    dict = {'价格':price, '标题':title, '评论':comment}
    data = json.dumps(dict, ensure_ascii=False)
    f.write(data + '\n')

def search(page_source):
    soup = BeautifulSoup(page_source,'lxml')
    contents = soup.find_all('div',{'class':'gl-i-wrap'})
    for content in contents:
        price = content.find('div',{'class':'p-price'}).find('em').string + content.find('div',{'class':'p-price'}).find('i').string
        title = content.find('a').attrs['title']
        comment = content.find('div',{'class':'p-commit'}).find('strong').find('a').string
        write_data(price,title,comment)

def nextPage():

    k = 0
    while True:
        try:

            k = k + 1
            m = 2 * k + 1

            url = 'https://search.jd.com/Search?keyword=%E8%B6%85%E5%B8%82%E8%B4%A7%E6%9E%B6&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E8%B6%85%E5%B8%82%E8%B4%A7%E6%9E%B6&psort=' + str(m)

            print(url)
            response = requests.get(url)
            response.encoding='utf-8'
            search(response.text)

        except Exception as e:
            print(e)
            pass

def main():
    nextPage()


if __name__ == '__main__':
    nextPage()
