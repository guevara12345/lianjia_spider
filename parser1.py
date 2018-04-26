from bs4 import BeautifulSoup
import re
import os


proj_path = os.path.abspath('..')

'''parse https://bj.lianjia.com/ershoufang/haidian/'''
def parse_max_page_num(html):
    soup = BeautifulSoup(html, 'html.parser')
    p_list = soup.find_all('div', 'page-box house-lst-page-box')
    l = p_list[0].attrs
    m = re.match(r'{"totalPage":(\d+),"curPage":1}', l['page-data'])
    r = int(m.group(1))
    print('{} page of html'.format(r))
    return r


def parse_house_url(html):
    soup = BeautifulSoup(html, 'html.parser')
    l_tag = soup.find_all('div', 'info clear')
    return -1


if __name__ == '__main__':
    with open(os.path.join(proj_path, u'data/海淀/house_url_page1.html'), 'r') as f:
        parse_house_url(f.read())