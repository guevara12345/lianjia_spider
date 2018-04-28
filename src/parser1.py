from bs4 import BeautifulSoup
import re
import os


#import src.db_helper


tb_house_info = ['id', 'code', 'xiaoqu', 'room', 'area', 'orientations', 'decoration', 'is_elevator', 'region', 'floor', 'building_info', '', '', '', '', '', '', '']


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
    # get list of dict_house_info
    for i2 in l_tag:
        #fill dict_house_info

        dict_house_info['code'] = i2.find('div', 'title').a.attrs['data-housecode']
        m = re.split(r'/', i2.find('div', 'houseInfo').text)
        print('{}:{}'.format(dict_house_info['code'], m))
        #xiaoqu for 小区, room like 两室一厅, area for 面积, orientations for 朝向, decoration like 精装, is_elevator like 有电梯
        for i in range(len(m)):
            dict_house_info[tb_house_info[i+1]] = m[i]
        #region like 清河
        dict_house_info['region'] = i2.find('div', 'positionInfo').a.string
        m = re.split(r'/', i2.find('div', 'positionInfo').text)
        #floor like 顶层(共13层)
        dict_house_info['floor'] = m[0]
        # building like 2003年建塔楼
        dict_house_info['building_info'] = m[1]
        list_dict_house_info.append(dict_house_info)
    return (list_url, list_dict_house_info)


def parse_house_info(html):
    dict_house_info = dict()
    soup = BeautifulSoup(html, 'html.parser')
    # code for 房屋代码
    dict_house_info[tb_house_info[0]] = soup.find('div', 'houseRecord').find_all('span')[1].contents[0]
    

def persis_house_info(dict_house_info):
    pass


if __name__ == '__main__':
    '''
    with open(os.path.join(proj_path, u'data/海淀/house_url_page1.html'), 'r') as f:
        i,j = parse_house_url(f.read())
    '''
    with open(os.path.join(proj_path, u'data/house_detail/101102803649.html'), 'r') as f:
        parse_house_info(f.read())
        print('fuck')