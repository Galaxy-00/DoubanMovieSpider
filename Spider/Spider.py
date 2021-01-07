from settings import COOKIES, PROXY_URL, USER_AGENT
import requests
import random


class Spider(object):
    def __init__(self) -> None:
        self.movieQueryUrl = "https://movie.douban.com/j/new_search_subjects?type=movie&sort={sortType}&range={rateRange}&tags={tags}&start={start}&genres={geners}&countries={countries}&year_range={year_range}"
        self.moviePage = "https://movie.douban.com/subject/{id}/"

    def get_random_header(self) -> dict:
        '''
        返回随机构造的header
        '''
        headers = {
            "User-Agent": random.choice(USER_AGENT),
            "Referer": "https://www.douban.com/",
            "Cookie": COOKIES
        }
        return headers

    def get_proxy(self) -> dict:
        '''
        返回一个代理
        '''
        proxy = requests.get(PROXY_URL).text
        proxies = {"https": "https://" + proxy, "http": "http://" + proxy}
        # print(proxies)
        return proxies