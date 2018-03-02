# from selenium import webdriver
import time
from bs4 import BeautifulSoup
import json
# from beautiful_爬虫 import conn_mysql
import requests
from urllib.parse import quote

def write_data(price,title,comment):
    f = open('手机3.txt','a')
    dict = {'价格':price, '标题':title, '评论':comment}
    data = json.dumps(dict, ensure_ascii=False)
    f.write(data + '\n')
    # conn_mysql.addPhone(price,title,comment)
def search(page_source):
    soup = BeautifulSoup(page_source,'lxml')
    contents = soup.find_all('div',{'class':'gl-i-wrap'})
    for content in contents:
        price = content.find('div',{'class':'p-price'}).find('em').string + content.find('div',{'class':'p-price'}).find('i').string
        title = content.find('a').attrs['title']
        comment = content.find('div',{'class':'p-commit'}).find('strong').find('a').string
        # gevent.spawn(write_data,price,title,comment)
        write_data(price,title,comment)

def nextPage():

    k = 0
    while True:
        try:

            k = k + 1
            m = 2 * k + 1
            # goods = quote('电脑')
            url = 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=' +str(m)
            # url = 'https://search.jd.com/Search?keyword=%E7%94%B5%E8%84%91&enc=utf-8&suggest=1.def.0.V07&wq=diann&pvid=d6fc7a3deac347f5819ebb9a3f418c07'

            print(url)
            # driver1 = webdriver.Firefox()
            # driver1.get(url)
            #
            # js = "window.scrollTo(0, document.body.scrollHeight);"
            # driver1.execute_script(js)
            #
            # search(driver1.page_source)
            # driver1.close()
            # time.sleep(5)
            response = requests.get(url)
            response.encoding='utf-8'
            search(response.text)

        except Exception as e:
            print(e)
            pass

def main():

    # driver = webdriver.Firefox()
    # # driver.get('https://www.jd.com/')
    # # time.sleep(1)
    # # key = driver.find_element_by_id('key')
    # # button = driver.find_element_by_class_name('button')
    # key.clear()
    # key.send_keys('手机')
    # time.sleep(1)
    # button.click()
    # js = "window.scrollTo(0, document.body.scrollHeight);"
    # driver.execute_script(js)
    # time.sleep(1)
    # search(driver.page_source)
    # time.sleep(3)

    nextPage()

    # nextPage()


if __name__ == '__main__':
    # main()
    nextPage()
    # driver = webdriver.Firefox()
    # driver.get('https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=3')
    # print(driver.page_source)
