#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib.parse import urljoin
from requests.exceptions import Timeout, RequestException
import os
import re


from src.downloader1 import HtmlDownloader
from src.parser1 import HouseInfoHandler, XiaoquInfoHandler, RegionInfoHandler


max_price = 850
min_price = 650
build_age = {'0-5': 'y1', '0-10': 'y2', '0-15': 'y3', '0-20': 'y4', }
house_type = {'1': 'l1', '2': 'l2', '3': 'l3', '4': 'l4'}
bond = '{}{}bp{}ep{}'.format(build_age['0-15'], house_type['2'], min_price, max_price)


district_url_map = {
#    u'东城': 'https://bj.lianjia.com/ershoufang/dongcheng/',
#    u'西城': 'https://bj.lianjia.com/ershoufang/xicheng/',
    u'朝阳': 'https://bj.lianjia.com/ershoufang/chaoyang/',
    u'海淀': 'https://bj.lianjia.com/ershoufang/haidian/',
#    u'丰台': 'https://bj.lianjia.com/ershoufang/fengtai/',
#    u'石景山': 'https://bj.lianjia.com/ershoufang/shijingshan/',
#    u'通州': 'https://bj.lianjia.com/ershoufang/tongzhou/',
#    u'昌平': 'https://bj.lianjia.com/ershoufang/changping/'
    }
xiaoqu_district_url_map = {
#    u'东城': 'https://bj.lianjia.com/xiaoqu/dongcheng/',
#    u'西城': 'https://bj.lianjia.com/xiaoqu/xicheng/',
    u'朝阳': 'https://bj.lianjia.com/xiaoqu/chaoyang/',
    u'海淀': 'https://bj.lianjia.com/xiaoqu/haidian/',
#    u'丰台': 'https://bj.lianjia.com/xiaoqu/fengtai/',
#    u'石景山': 'https://bj.lianjia.com/xiaoqu/shijingshan/',
#    u'通州': 'https://bj.lianjia.com/xiaoqu/tongzhou/',
#    u'昌平': 'https://bj.lianjia.com/xiaoqu/changping/'
    }
proj_path = os.path.abspath('..')


def mkdir4house_url_page():
    for k in district_url_map:
        path_house_url= os.path.join(proj_path, 'data/{}/house_url'.format(k))
        path_xiaoqu = os.path.join(proj_path, 'data/{}/xiaoqu'.format(k))
        if not os.path.isdir(path_house_url):
            os.makedirs(path_house_url)
        if not os.path.isdir(path_xiaoqu):
            os.makedirs(path_xiaoqu)
    path = os.path.join(proj_path, 'data/house_detail')
    if not os.path.isdir(path):
        os.makedirs(path)
    path = os.path.join(proj_path, 'result')
    if not os.path.isdir(path):
        os.makedirs(path)

'''
house_info-1:
#下载并解析各区挂出二手房第一页，获取各区二手房挂出的页面数
#根据页数，下载各区二手房信息    
'''
def download_house_4_sale_url():
    #1
    for key in district_url_map:
        url = urljoin(district_url_map[key], 'pg{}{}'.format(1, bond))
        path = os.path.join(proj_path, 'data/{}/house_url/house_url_page{}.html'.format(key, 1))
        HtmlDownloader().download_html(url, path)
    #2
    for key in district_url_map:
        path = os.path.join(proj_path, 'data/{}/house_url/house_url_page{}.html'.format(key, 1))
        with open(path, 'r') as f:
            page_num = HouseInfoHandler().parse_max_page_num(f.read(), path)
            for i in range(page_num-1):
                url = urljoin(district_url_map[key], 'pg{}{}'.format(i+2, bond))
                path = os.path.join(proj_path, 'data/{}/house_url/house_url_page{}.html'.format(key, i+2))
                HtmlDownloader().download_html(url, path)
'''
house_info-2:
#download detail info of house
'''
def download_house_info(l_url):
    for i in  l_url:
        f_name = re.match(r'https.*/(.*)$', i).group(1)
        path = os.path.join(proj_path, 'data/house_detail/{}'.format(f_name))
        HtmlDownloader().download_html(i, path)

'''
xiaoqu_info
'''
def download_xiaoqu_url():
    for key in xiaoqu_district_url_map:
        url = '{}/pg{}/'.format(xiaoqu_district_url_map[key], 1)
        path = os.path.join(proj_path, 'data/{}/xiaoqu'.format(key))
        HtmlDownloader().download_html(url, path)

    for key in xiaoqu_district_url_map:
        num = XiaoquInfoHandler().parse_xiaoqu_url_max_pagenum()
        for i in range(num-1):
            path = os.path.join(proj_path, 'data/{}/xiaoqu/url_info_page{}'.format(key, i+2))
            url = '{}/pg{}/'.format(xiaoqu_district_url_map[key], i+2)
            HtmlDownloader().download_html(url, path)


def down_load_xiaoqu_detail(l_url):
    pass


#main of this proj
def lianjia_spider_dispatcher():

    mkdir4house_url_page()
    # get house 4 sale info
    """
    download_house_4_sale_url()
    # get region_info
    for k in district_url_map:
        region_info_html_path = os.path.join(proj_path,
                                             'data/{}/house_url/house_url_page1.html'.format(k))
        with open(region_info_html_path, 'r') as f:
            r = RegionInfoHandler().parse_region(f.read(), region_info_html_path)
            RegionInfoHandler().persist_region(r)
    for k in district_url_map:
        #download house_info_detail
        html_dir_path = os.path.join(proj_path,
                                     'data/{}/house_url'.format(k))
        for file in os.listdir(html_dir_path):
            html_path = os.path.join(html_dir_path, file)
            if os.path.isfile(html_path):
                with open(html_path, 'r') as f:
                    l_url = HouseInfoHandler().parse_house_url(f.read(), html_path)
                    download_house_info(l_url)
    """
    #parse and persist house_info_detail
    info_path = os.path.join(proj_path, 'data/house_detail')
    for file in os.listdir(info_path):
        file_path = os.path.join(info_path, file)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as f:
                r = HouseInfoHandler().parse_house_info(f.read(), file_path)
                HouseInfoHandler().persis_house_info(r)
    #get xiaoqu info

if __name__ == '__main__':
    lianjia_spider_dispatcher()