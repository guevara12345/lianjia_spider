from urllib.parse import urljoin
from requests.exceptions import Timeout, RequestException
import os
import re


import src.downloader1
import src.parser1


max_price = 800
min_price = 600
build_age = {'0-5': 'y1', '0-10': 'y2', '0-15': 'y3', '0-20': 'y4', }
house_type = {'1': 'l1', '2': 'l2', '3': 'l3', '4': 'l4'}
bond = '{}{}bp{}ep{}'.format(build_age['0-15'], house_type['2'], min_price, max_price)

district_url_map = {
    u'海淀': 'https://bj.lianjia.com/ershoufang/haidian/'}
district_url_map_f = {
    u'东城': 'https://bj.lianjia.com/ershoufang/dongcheng/',
    u'西城': 'https://bj.lianjia.com/ershoufang/xicheng/',
    u'朝阳': 'https://bj.lianjia.com/ershoufang/chaoyang/',
    u'海淀': 'https://bj.lianjia.com/ershoufang/haidian/',
    u'丰台': 'https://bj.lianjia.com/ershoufang/fengtai/',
    u'石景山': 'https://bj.lianjia.com/ershoufang/shijingshan/',
    u'通州': 'https://bj.lianjia.com/ershoufang/tongzhou/',
    u'昌平': 'https://bj.lianjia.com/ershoufang/changping/',
    u'大兴': 'https://bj.lianjia.com/ershoufang/daxing/',
    u'亦庄开发区': 'https://bj.lianjia.com/ershoufang/yizhuangkaifaqu/',
    u'顺义': 'https://bj.lianjia.com/ershoufang/shunyi/',
    u'房山': 'https://bj.lianjia.com/ershoufang/fangshan/',
    u'门头沟': 'https://bj.lianjia.com/ershoufang/mentougou/',
    u'平谷': 'https://bj.lianjia.com/ershoufang/pinggu/',
    u'怀柔': 'https://bj.lianjia.com/ershoufang/huairou/',
    u'密云': 'https://bj.lianjia.com/ershoufang/miyun/',
    u'延庆': 'https://bj.lianjia.com/ershoufang/yanqing/'}
proj_path = os.path.abspath('..')


def mkdir4house_url_page():
    for k in district_url_map:
        path = os.path.join(proj_path, 'data/{}'.format(k))
        if not os.path.isdir(path):
            os.makedirs(path)
        path = os.path.join(proj_path, 'data/house_detail'.format(k))
        if not os.path.isdir(path):
            os.makedirs(path)


'''
1
#下载并解析各区挂出二手房第一页，获取各区二手房挂出的页面数
#根据页数，下载各区二手房信息    
'''
def download_house_4_sale():
    #1
    for key in district_url_map:
        url = urljoin(district_url_map[key], 'pg{}{}'.format(1, bond))
        path = os.path.join(proj_path, 'data/{}/house_url_page{}.html'.format(key, 1))
        src.downloader1.download_html(url, path)
    #2
    for key in district_url_map:
        path = os.path.join(proj_path, 'data/{}/house_url_page{}.html'.format(key, 1))
        with open(path, 'r') as f:
            page_num = src.parser1.parse_max_page_num(f.read())
            for i in range(page_num-1):
                url = urljoin(district_url_map[key], 'pg{}{}'.format(i+2, bond))
                path = os.path.join(proj_path, 'data/{}/house_url_page{}.html'.format(key, i+2))
                src.downloader1.download_html(url, path)
'''
2
'''
def download_house_info(l_url):
    for i in  l_url:
        f_name = re.match(r'https.*/(.*)$', i).group(1)
        path = os.path.join(proj_path, 'data/house_detail/{}'.format(f_name))
        src.downloader1.download_html(i, path)

#main of this proj
def lianjia_spider_dispatcher():
    mkdir4house_url_page()
    #download_house_4_sale()
    for k in district_url_map:
        dir_path = os.path.join(proj_path, 'data/{}'.format(k))
        for file in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file)
            if os.path.isfile(file_path):
                with open(file_path, 'r') as f:
                    l_url, l_d_info = src.parser1.parse_house_url(f.read())
                    download_house_info(l_url)
                    src.parser1.persis_house_abbr_info(l_d_info)



if __name__ == '__main__':
    lianjia_spider_dispatcher()