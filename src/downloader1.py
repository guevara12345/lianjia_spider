#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
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


class HtmlDownloader:

    def download_html(self, url, file_path):
        try:
            time.sleep(0)
            rsp = requests.get(url, timeout=5, headers=HEADERS)
            if 200 == rsp.status_code:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(rsp.text)
                    print('{} downloaded'.format(url))
                    return rsp.text
            else:
                return None
        except Exception as e:
            print('download {} throw exception {}'.format(url, e))
            num = 0
            r = None
            while num < 3 and r is None:
                r = self.redo(url, file_path)
                num += 1

    def redo(self, url, file_path):
        try:
            time.sleep(5)
            rsp = requests.get(url, timeout=5, headers=HEADERS)
            if 200 == rsp.status_code:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(rsp.text)
                    print('{} downloaded'.format(url))
                    return rsp.text
            else:
                return None
        except Exception as e:
            print('download {} throw exception {}'.format(url, e))
