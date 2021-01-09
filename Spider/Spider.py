import random

import requests
from settings import (COOKIES, PROXY_URL, SOCKET_URL, USE_HTTP_PROXY,
                      USE_SOCKET, USER_AGENT)


class Spider(object):
    def __init__(self) -> None:
        self.movieQueryUrl = "https://movie.douban.com/j/new_search_subjects?sort={sortType}&range={rateRange}&tags={tags}&start={start}&genres={geners}&countries={countries}&year_range={year_range}"
        self.moviePage = "https://movie.douban.com/subject/{id}/"

    def get_random_header(self) -> dict:
        '''
        返回随机构造的header
        '''
        headers = {
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cookie": COOKIES,
            "Host": "movie.douban.com",
            "Origin": "https://movie.douban.com",
            "Referer": "https://movie.douban.com/",
            "User-Agent": random.choice(USER_AGENT),
            # "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
        }
        return headers

    def get_proxy(self) -> dict:
        '''
        返回一个代理
        '''
        proxies = {}
        if USE_HTTP_PROXY:
            proxy = requests.get(PROXY_URL).text
            proxies = {"https": "https://" + proxy, "http": "http://" + proxy}
        if USE_SOCKET:
            proxies = {
                "https": "socks5://" + SOCKET_URL,
                "http": "socks5://" + SOCKET_URL
            }
        print('Using proxy: {}'.format(proxies))
        return proxies
