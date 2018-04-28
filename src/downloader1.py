import requests
from requests.exceptions import Timeout, RequestException
import time


HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'bj.lianjia.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}


def download_html(url, file_path):
    try:
        time.sleep(1)
        rsp = requests.get(url, timeout=5, headers=HEADERS)
        if 200 == rsp.status_code:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(rsp.text)
                print('{} downloaded'.format(url))
                return rsp.text
        else:
            return None
    except Timeout as e:
        print('download {} throw exception {}'.format(url, e))
    except RequestException as e:
        print('download {} throw exception {}'.format(url, e))
