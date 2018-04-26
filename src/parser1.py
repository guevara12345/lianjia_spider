from bs4 import BeautifulSoup
import re
import os


#import src.db_helper


tb_house_info = ['id', 'code', 'region']


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
    dict_house_info = dict()
    soup = BeautifulSoup(html, 'html.parser')
    l_tag = soup.find_all('div', 'info clear')
    for i1 in l_tag:
        l = i1.find('div', 'title').a.attrs
        list_url.append(l['href'])
    for i2 in l_tag:
        dict_house_info['code'] = i2.find('div', 'title').a.attrs['data-housecode']
        dict_house_info['region'] = i2.find('div', 'houseInfo').a.string
        re.match(r'<a.*?>(.+?)</a><span class="divide">/</span>(.*?)<span class="divide">/</span>'
                 r'(.*?)<span class="divide">/</span>(.*?)<span class="divide">/</span>'
                 r'(.*?)<span class="divide">/</span>(.*?)$', i2.find('div', 'houseInfo').string)
        dict_house_info['']=
    return (list_url, dict_house_info)

def persis_house_abbr_info():
    pass


if __name__ == '__main__':
    with open(os.path.join(proj_path, u'data/海淀/house_url_page1.html'), 'r') as f:
        parse_house_url(f.read())