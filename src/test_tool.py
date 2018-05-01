import src.db_helper
import csv
import os
import time

tb_house_info = ['code','total_price','unit_price','room',
                 'floor','build_area','huxing','house_area','orientations',
                 'buiding_texture','decoration','elevator_house_proportion','heating','is_elevator',
                 'property_right','building_type','xiaoqu','region','guapai_time',
                 'property_type','last_deal_time','house_usage','deal_year','property_ownership',
                 'mortgage']
proj_path = os.path.abspath('..')

def select():
    db_hanlder = src.db_helper.DbExeu()
    sql = '''
        SELECT t.xiaoqu, t.total_price, t.unit_price, t.region, t.build_area
            , t.house_area, t.room, t.orientations, t.guapai_time
            , CONCAT('https://bj.lianjia.com/ershoufang/', t.code, '.html')
        FROM tb_house_info t, tb_region_info s
        WHERE t.region = s.region
            AND house_usage = '普通住宅'
            AND s.is_too_far = 0
        ORDER BY region, xiaoqu
        '''
    r = db_hanlder.return_many_without_para(sql)
    time_str = time.strftime("%Y-%b-%d %H:%M:%S")
    with open(os.path.join(proj_path, 'result/house_info_{}.csv'.format(time_str)), 'w') as f:
        i=list(r[0])
        f_csv = csv.writer(f)
        f_csv.writerow(['xiaoqu','total_price','unit_price','region','build_area','house_area', 'room','orientations','guapai_time','href'])
        f_csv.writerows(i)


def select_region():
    db_hanlder = src.db_helper.DbExeu()
    sql = '''select * from tb_region_info'''
    r = db_hanlder.return_many_without_para(sql)
    print(r)
    sql = '''select * from tb_region_info where region=%s'''
    r = db_hanlder.return_many_with_para(sql, ('三里屯'))
    print(r)


if __name__=='__main__':
    select()
    #select_region()