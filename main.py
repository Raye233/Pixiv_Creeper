import time
import os
from Pixiv.filepath_create import filepath_generator
from read_url import read_URL
import requests
import random
import shutil


path = r'F:\Rayedata2\Creeper\Pixiv\realesrgan-ncnn-vulkan-20211212-windows\input'


def del_file(filepath):
    """
    删除某一目录下的所有文件或文件夹
    :param filepath: 路径
    :return:
    """
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    print('已删除原input文件夹的所有文件')


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security '
                  'Firefox/1.5.0.12',
    'Referer': 'https://www.pixiv.net/ranking.php',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed'
              '-exchange;v=b3;q=0.7',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    # 'connection': 'close',
    'cookie': 'first_visit_datetime_pc=2023-03-06+12%3A12%3A34; p_ab_id=1; p_ab_id_2=1; p_ab_d_id=1636898900; '
              'yuid_b=KYWYckY; _gcl_au=1.1.809539283.1678072358; _fbp=fb.1.1678072358801.1794956768; '
              'PHPSESSID=29836642_LElgp6Z4WrAAKWa8tUs3hlhBBKR1bAFm; device_token=30f8e1bdb17b77a99fd0082de2b7356d; '
              'privacy_policy_agreement=5; c_type=28; privacy_policy_notification=0; a_type=0; b_type=0; '
              'login_ever=yes; _ga_MZ1NL4PHH0=GS1.1.1678602567.2.0.1678602567.0.0.0; p_b_type=1; '
              'QSI_S_ZN_5hF4My7Ad6VNNAi=v:0:0; _gid=GA1.2.2108439320.1678705637; '
              'tag_view_ranking=RTJMXD26Ak~5AKOA9olwV~kP7msdIeEU~iL7wk5q0c2~uNzD6EQwPd~RKAHEY3QDd~HBYFbIUAS8~Lt'
              '-oEicbBr~uI6TujULvb~RdrlEFKlk9~YRDwjaiLZn~K8esoIs2eW~jH0uD88V6F~uusOs0ipBx~-GotrwNg8L~mHukPa9Swj'
              '~LtJkZvfOj-~X1DdklZd8L~nRp2ZLPLbj~5sExEHA8P5~69v3aNJnS3~tIqkVZurKP~OEHogw1GmU~_pwIgrV8TB~_EOd7bsGyl'
              '~ziiAzr_h04~hW_oUTwHGx~4S_nJehaZd~b9fzxe_axh~Dbqsikb5Qu~BSlt10mdnm~GBEqsM0er3~LJo91uBPz4~aXpoVct1M'
              '-~TBAh5YDdLW~tvgK2ZR46G~wKl4cqK7Gl~vh2pcbcKY3~3HOQNXdtcb~PX4ekh0cSp~qRGnbYPA4E~9ODMAZ0ebV~eVxus64GZU'
              '~BQhcNnYpNk~tTS3aRujTx~ahHegnNVxX~v3nOtgG77A; '
              '__cf_bm=TbRQZwd3dueUVAR2BcGoWOULVi1rkA3WrmuXBL1usVI-1678966375-0-AeA+yXnv30iJ3AZHmydxfOP2Hf0ktLRJOW1'
              '+Dbiuw4jTEZie0J2QXT6r89gegTji4dJeL4c2eyvUkWOLGQA5L6WCz9HuR5'
              '/wAjZFmfw7aE8cCMQdN2Z488UnBINNRm3sr6XFPHp8ArCnsTjFuSUE6OfI6WJ0cqgTW3BW/cGG59Pp3ezkJ4eA1331jpcwD8/iAw'
              '==; _ga_75BBYNYN9J=GS1.1.1678966374.20.1.1678966376.0.0.0; _ga=GA1.2.2144054266.1678072358; '
              '_gat_UA-1830249-3=1 '
}

proxies = {
    'https': 'http://127.0.0.1:7890'
}

# print(name_list)
requests.packages.urllib3.disable_warnings()
session = requests.session()
# session.trust_env = False
dir_path = r'F:/Rayedata2/Creeper/Pixiv/page/'
save_path = r'F:/Rayedata2/Creeper/Pixiv/realesrgan-ncnn-vulkan-20211212-windows/input/'
filepath_list = filepath_generator(dir_path)
for filepath in filepath_list:
    URL = read_URL(filepath)
    response = session.get(url=URL, headers=headers, verify=False, proxies=proxies)
    name_list = str(random.randint(0, 1000))
    with open(save_path + name_list + '.png', 'wb') as f:
        f.write(response.content)
        time.sleep(2)


os.chdir(r'F:\Rayedata2\Creeper\Pixiv\realesrgan-ncnn-vulkan-20211212-windows')
retval = os.getcwd()
print("目录修改成功 %s" % retval)
os.system('start cmd.exe /K F:/Rayedata2/Creeper/Pixiv/realesrgan-ncnn-vulkan-20211212-windows/全部图片.bat')
os.startfile(r"F:\Rayedata2\Creeper\Pixiv\realesrgan-ncnn-vulkan-20211212-windows\output")
del_file(path)