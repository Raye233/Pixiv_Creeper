import base64
import subprocess

# url = 'https://i.pximg.net/img-master/img/2022/08/20/00/05/11/100612932_p0.jpg'  假url
# urL = 'https://i.pximg.net/img-original/img/2022/08/20/00/05/11/100612932_p0.png'  真url

thunder_path = r'E:\Program Files (x86)\Thunder Network\Thunder\Program\Thunder.exe'


def Url2Thunder(url):
    url = 'AA' + url + 'ZZ'
    url = base64.b64encode(url.encode('ascii'))
    url = b'thunder://' + url
    thunder_url = url.decode()
    return thunder_url


def download_with_thunder(file_url):
    thunder_url = Url2Thunder(file_url)
    subprocess.call([thunder_path, thunder_url])



