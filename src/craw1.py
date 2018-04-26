import requests

HOME_URL = 'https://bj.lianjia.com/'
USERINFO_URL = 'https://upassport.lianjia.com/login'
USERINFO_DATA = {
    'service': 'https%3A%2F%2Fajax.api.lianjia.com%2Flogin%2Flogin%2Fgetuserinfo',
    'type': '1',
    'get-lt': 'true',
    'isajax': 'true',
    'from': 'lianjiaweb',
    'username': '1521059720'}
AUTH_URL = 'https://passport.lianjia.com/cas/login?service=http%3A%2F%2Fbj.lianjia.com%2F'
DEAL_URL = 'http://bj.lianjia.com/chengjiao/'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'bj.lianjia.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
def get_cookies():
    s = requests.Session()
    s.get(HOME_URL, headers=HEADERS)
    rsp = s.get(AUTH_URL, headers=HEADERS)
    print(rsp.status_code)
    for key, value in rsp.cookies.items():
        print(key+"="+value)

    rsp = s.get('https://bj.lianjia.com/chengjiao/haidian/')
    print(rsp.)


if __name__=='__main__':
    get_cookies()