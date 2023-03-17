import json
import time
from selenium import webdriver
from lxml import etree
from urllib import request, error
from selenium.webdriver.chrome.service import Service
import gzip
import random
from urllib.request import ProxyHandler
from Pixiv.filepath_create import filepath_generator
import os
from thunder_download import download_with_thunder
from read_url import read_URL
from header import *


options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--incognito")
options.add_argument("--disable-site-isolation-trials")
user_agent = (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) " +
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36"
)

options.add_argument('user-agent=%s' % user_agent)

# options.add_experimental_option('detach', True)
path = r'F:\Rayedata2\Creeper\chromedriver.exe'
service = Service(path)
url = 'https://www.pixiv.net/ranking.php'

browser = webdriver.Chrome(service=service, options=options)
browser.get(url)
time.sleep(3)
browser.delete_all_cookies()

with open(r'F:\Rayedata2\Creeper\cookies_1.txt', 'r') as f:
    cookies_list = json.load(f)
    for cookie in cookies_list:
        if isinstance(cookie.get('expiry'), float):
            cookie['expiry'] = int(cookie['expiry'])
        browser.add_cookie(cookie)

browser.refresh()
time.sleep(3)

proxies = {
    # 'http': random.choice(my_http_proxies),
    'https': random.choice(my_https_proxies)
}

headers = {
    'User-Agent': random.choice(my_headers),
    'Referer': 'https://www.pixiv.net/ranking.php',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed'
              '-exchange;v=b3;q=0.7',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    # 'connection': 'close'
}

# urllib代理
# proxy_handler = ProxyHandler(proxies)
#
# opener = request.build_opener(proxy_handler)
# request.install_opener(opener)

req = request.Request(url, headers=headers)
response = request.urlopen(req, timeout=100000)
data = gzip.decompress(response.read())
content = data.decode('utf-8')
# print(content)
result = etree.HTML(content)
LIST = result.xpath("//div[contains(@class, 'ranking-image-item')]/a/@href")
URL_LIST = []
for i in LIST:
    if 'series' in i:
        LIST.remove(i)
# print(LIST)
for j in LIST:
    URL_LIST.append('https://www.pixiv.net' + j)
# print(URL_LIST)

page_list = []
pic_dir = r'F:/Rayedata2/Creeper/Pixiv/pic/'

pic_number = 10

for num in range(len(URL_LIST[:pic_number])):
    new_page = f"window.open('{format(URL_LIST[num])}')"  # idea one
    browser.execute_script(new_page)
    browser.implicitly_wait(10)
    handle = browser.current_window_handle
    all_handles = browser.window_handles
    for i in all_handles:
        if i != handle:
            browser.switch_to.window(i)
            # print(browser.title)
            page = browser.page_source
            # print(page)
            with open(fr'F:\Rayedata2\Creeper\Pixiv\page\{format(num)}.html', mode='w+', encoding='utf-8') as fp:
                fp.write(page)


# if __name__ == '__main__':
#     filepath_list = filepath_generator(r'F:/Rayedata2/Creeper/Pixiv/page/')
#     for filepath in filepath_list:
#         true_url = read_URL(filepath)
#         download_with_thunder(true_url)
#         time.sleep(3)





