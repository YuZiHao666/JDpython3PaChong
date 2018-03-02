import time
from bs4 import BeautifulSoup
import json
import requests
from urllib.parse import quote
import pandas

# def write_data(price,title,comment):
#     f = open('手机.txt','a')
#     dict = {'价格':price, '标题':title, '评论':comment}
#     data = json.dumps(dict, ensure_ascii=False)
#     f.write(data + '\n')



def search(page_source):
    soup = BeautifulSoup(page_source,'lxml')
    contents = soup.find_all('div',{'class':'gl-i-wrap'})
    data=[]
    for content in contents:
        result={}
        result['price'] = content.find('div',{'class':'p-price'}).find('em').string + content.find('div',{'class':'p-price'}).find('i').string
        result['title'] = content.find('a').attrs['title']
        result['comment'] = content.find('div',{'class':'p-commit'}).find('strong').find('a').string
        data.append(result)
        # write_data(price,title,comment)
    return data

def nextPage():
    k = 0
    news=[]
    while True:
        try:
            k = k + 1
            m = 2 * k + 1
            url = 'https://search.jd.com/Search?keyword=%E8%B6%85%E5%B8%82%E8%B4%A7%E6%9E%B6&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E8%B6%85%E5%B8%82%E8%B4%A7%E6%9E%B6&psort=' + str(m)
            # print(url)
            response = requests.get(url)
            response.encoding='utf-8'
            for i in search(response.text):
                news.append(i)

            print(k)
            if k==3:
                break
        except Exception as e:
            print(e)
            pass
        print(news)
    return news

def main():
    data=nextPage()
    df = pandas.DataFrame(data)
    print(df.head(10))
    # 保存到本地excel文档
    df.to_excel('商品信息.xlsx')


if __name__ == '__main__':
    main()
