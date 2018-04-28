from bs4 import BeautifulSoup
import re
import os


#import src.db_helper


tb_house_info = ['id','code','total_price','unit_price','room',
                 'floor','biuld_area','huxing','house_area','orientations',
                 'biuding_texture','decoration','elevator_house_proportion','heating','is_elevator',
                 'property_right','building_type','xiaoqu','region','guapai_time',
                 'property_type','last_deal_time','house_usage','deal_year','property_ownership',
                 'mortgage']

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
    list_url=[]
    list_dict_house_info=[]
    dict_house_info = dict()
    soup = BeautifulSoup(html, 'html.parser')
    l_tag = soup.find_all('div', 'info clear')
    # get house detail info url list
    for i1 in l_tag:

        l = i1.find('div', 'title').a.attrs
        list_url.append(l['href'])
    return list_url


def parse_house_info(html):
    dict_house_info = dict()
    soup = BeautifulSoup(html, 'html.parser')
    overview = soup.find('div', 'overview').find('div', 'content')
    basic = soup.find('div', 'm-content').find('div', 'base')
    transaction = soup.find('div', 'm-content').find('div', 'transaction')
    # fill dict_house_info
    # code for 房屋代码
    dict_house_info['code'] = overview.find('div', 'houseRecord').find_all('span')[1].contents[0]
    # total_price for 总价
    dict_house_info['total_price'] = overview.find('div', 'price ').find_all('span')[0].string
    # unit_price for 单价
    dict_house_info['unit_price'] = overview.find('div', 'price ').find_all('span')[3].contents[0]
    # room like 两室一厅
    dict_house_info['room'] = basic.find_all('li')[0].contents[1]
    # floor like 顶层(共13层)
    dict_house_info['floor'] = basic.find_all('li')[1].contents[1]
    # biuld_area for 建筑面积
    dict_house_info['biuld_area'] = basic.find_all('li')[2].contents[1]
    # huxing like 平层
    dict_house_info['huxing'] = basic.find_all('li')[3].contents[1]
    # house_area for 套内面积
    dict_house_info['house_area'] = basic.find_all('li')[4].contents[1]
    # orientations for 朝向
    dict_house_info['orientations'] = basic.find_all('li')[6].contents[1]
    # biuding_texture like 材质
    dict_house_info['buiding_texture'] = basic.find_all('li')[7].contents[1]
    # decoration like 精装
    dict_house_info['decoration'] = basic.find_all('li')[8].contents[1]
    # elevator_house_proportion like 一梯三户
    dict_house_info['elevator_house_proportion'] = basic.find_all('li')[9].contents[1]
    # heating like 自供暖
    dict_house_info['heating'] = basic.find_all('li')[10].contents[1]
    # is_elevator like 有电梯
    dict_house_info['is_elevator'] = basic.find_all('li')[11].contents[1]
    # property_right like 70年
    dict_house_info['property_right'] = basic.find_all('li')[12].contents[1]
    # building_type like 2003年建塔楼
    dict_house_info['building_type'] = overview.find('div', 'area').find('div', 'subInfo').string
    # xiaoqu for 小区
    dict_house_info['xiaoqu'] = overview.find('div', 'communityName').a.string
    # region like 清河
    dict_house_info['region'] = overview.find('div', 'areaName').find_all('a')[1].string

    # guapai_time is 挂牌时间
    dict_house_info['guapai_time'] = transaction.find_all('li')[0].find_all('span')[1].string
    # property_type like 商品房
    dict_house_info['property_type'] = transaction.find_all('li')[1].find_all('span')[1].string
    # last_deal_time is 上次交易
    dict_house_info['last_deal_time'] = transaction.find_all('li')[2].find_all('span')[1].string
    # house_usage is 房屋用途
    dict_house_info['house_usage'] = transaction.find_all('li')[3].find_all('span')[1].string
    # deal_year is 房屋年限
    dict_house_info['deal_year'] = transaction.find_all('li')[4].find_all('span')[1].string\
    # property_ownership is 产权所属
    dict_house_info['property_ownership'] = transaction.find_all('li')[5].find_all('span')[1].string
    # mortgage is 抵押信息
    dict_house_info['mortgage'] = transaction.find_all('li')[6].find_all('span')[1].string
    return dict_house_info


def persis_house_info(dict_house_info):

    pass


if __name__ == '__main__':
    '''
    with open(os.path.join(proj_path, u'data/海淀/house_url_page1.html'), 'r') as f:
        i,j = parse_house_url(f.read())
    '''
    with open(os.path.join(proj_path, u'data/house_detail/101102803649.html'), 'r') as f:
        r = parse_house_info(f.read())
        print(r)
