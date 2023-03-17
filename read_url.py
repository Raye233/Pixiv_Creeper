from filepath_create import filepath_generator
from lxml import etree
from jsonpath import jsonpath
import json


def read_URL(html_path):
    html_file = open(html_path, 'r', encoding='utf-8', errors='ignore')
    html_handle = html_file.read()
    html = etree.HTML(html_handle)
    # print(html_handle)
    content = html.xpath("//head//meta[contains(@name, 'preload')]/@content")
    content_json = content[0]
    # print(content)
    content_dict = json.loads(content_json)
    result = jsonpath(content_dict, "$..original")
    original_url = result[0]
    print(original_url)
    return original_url


if __name__ == '__main__':
    filepath_list = filepath_generator(r'F:/Rayedata2/Creeper/Pixiv/page/')
    for filepath in filepath_list:
        read_URL(filepath)
