import json
from selenium import webdriver
import requests
from lxml import etree
from urllib import request
from selenium.webdriver.chrome.service import Service
# driver = webdriver.Chrome()

# driver.get('https://www.pixiv.net/ranking.php')

# input('输入回车后继续:')
#
# with open('cookies_1.txt', 'w') as f:
#     # 将cookies保存为json格式
#     f.write(json.dumps(driver.get_cookies()))
#
# driver.close()


option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
# 加载个人资料路径
option.add_argument('--profile-directory=Default')
option.add_argument(r'--user-data-dir=C:\Users\Raye\AppData\Local\Google\Chrome\User Data')
path = r'/chromedriver.exe'
service = Service(path)
driver = webdriver.Chrome(service=service, options=option)  # 启动Chrome驱动
driver.get('https://www.pixiv.net/ranking.php')
input('输入回车后继续:')

with open('../cookies_1.txt', 'w') as f:
    # 将cookies保存为json格式
    f.write(json.dumps(driver.get_cookies()))

driver.close()