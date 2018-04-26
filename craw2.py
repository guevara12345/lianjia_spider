import requests
from urllib.parse import urljoin
from requests.exceptions import Timeout, RequestException
import os
import time
from bs4 import BeautifulSoup


from src.parser1 import parse_max_page_num


# static






def get_house_list_html_for_sale():
    base_url = DISTRICT[u'海淀']

    url = urljoin(base_url, para_url)
    rsp = requests.get(url, timeout=2, headers=HEADERS)
    max_page_num = parse_max_page_num(rsp.text)
    with open(os.path.join(os.path.abspath('..'), 'data/text{}.html'.format(1)), 'w', encoding='utf-8') as f:
        f.write(rsp.text)
    for i in range(max_page_num-1):
        time.sleep(1)
        base_url = DISTRICT[u'海淀']
        para_url = 'pg{}{}{}bp{}ep{}'.format(i, build_age['0-15'], house_type['2'], min_price, max_price)
        url = urljoin(base_url, para_url)
        try:
            rsp = requests.get(url, timeout=5, headers=HEADERS)
            HTML_PATH = os.path.join(os.path.abspath('..'), 'data/text{}.html'.format(i+2))
            with open(HTML_PATH, 'w', encoding='utf-8') as f:
                f.write(rsp.text)
        except Timeout as e:
            print(e)
            print('page = {}'.format(i+2))
            stop = -1
        except RequestException as e:
            print(e)
            print('page = {}'.format(i+2))
            stop = -1
    return -1


def handle_house_url_for_sale(html):
    soup = BeautifulSoup(html, 'html.parser')
    p_list = soup.find_all('div', 'sub_nav section_sub_nav')
    return -1


if __name__ == '__main__':
    get_house_list_html_for_sale()
    html = ''
    with open(os.path.join(os.path.abspath('..'), 'data/text{}.html'.format(1)), 'r') as f:
        html = f.read()
    handle_house_url_for_sale(html)
    print(parse_max_page_num(html))
