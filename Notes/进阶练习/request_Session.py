import requests

session = requests.session()
login_url = 'https://accounts.douban.com/j/mobile/login/basic'
home_url = 'https://www.douban.com/note/776966831/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony'
}


# def get_cookies():
#     login_user = {'name': 'a541541000@163.com', 'password': 'aa1234bb'}
#
#     print('=============获取cookies================')
#     cookiesjar = session.post(login_url, data=login_user, headers=headers).cookies
#     cookie_t = requests.utils.dict_from_cookiejar(cookiesjar)
#     return cookie_t



if __name__ == '__main__':
    #cookies = get_cookies()
    #home = session.get(home_url, headers=headers,cookies).text
    login_user = {'name': 'a541541000@163.com', 'password': 'aa1234bb'}

    print('=============获取cookies================')
    session.post(login_url, data=login_user, headers=headers)
    home = session.get(home_url, headers=headers).text
    print(home)



