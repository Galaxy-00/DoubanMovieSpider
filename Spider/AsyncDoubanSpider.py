import requests
from retrying import retry
from aiohttp.client import ClientSession
from settings import HEADERS, USE_PROXY


class AsyncDoubanSpider(object):
    def __init__(self) -> None:
        self.headers = HEADERS
        self.movieQueryUrl = "https://movie.douban.com/j/new_search_subjects?sort={sortType}&range={rateRange}&tags={tags}&start={start}&genres={geners}&countries={countries}&year_range={year_range}"
        self.moviePage = "https://movie.douban.com/subject/{id}/"

    @retry(stop_max_attempt_number=3,
           wait_random_min=600,
           wait_random_max=1500)
    async def __crawl(self, url: str) -> str:
        '''
        爬取url页面, 返回获取的内容
        :param url: url
        '''
        try:
            async with ClientSession() as session:
                async with session.get(url, headers=self.headers) as res:
                    return await res.text()
        except:
            pass

    def __get_proxy(self) -> dict:
        '''
        返回一个代理
        '''
        proxy_url = "http://localhost:5555/random"
        proxy = requests.get(proxy_url).text
        proxies = {"https": "https://" + proxy, "http": "http://" + proxy}
        print(proxies)
        return proxies

    @retry(stop_max_attempt_number=3,
           wait_random_min=600,
           wait_random_max=1500)
    async def __crawl_proxy(self, url: str) -> str:
        '''
        爬取url页面, 返回获取的内容, 使用代理
        :param url: url
        '''
        try:
            async with ClientSession() as session:
                async with session.get(url,
                                       headers=self.headers,
                                       proxies=self.__get_proxy()) as res:
                    return await res.text()
        except:
            pass

    async def getMovieInfoByParams(self,
                                   sortType: str = "U",
                                   rateRange: str = "0,10",
                                   start: str = "0",
                                   tags: str = "",
                                   geners: str = "",
                                   countries: str = "",
                                   year_range: str = "") -> str:
        '''
        根据参数获取电影数据
        :param sortType: 电影数据的排序方式, U近期热门 T标记最多 S评分最高 R最新上映 
        :param rateRange: 电影数据评分的区间
        :param start: 电影数据的起始偏移, 一次返回20个电影数据
        :param tags: 电影特色, 例如经典 青春 文艺 搞笑 励志 魔幻等
        :param geners: 电影类型, 例如剧情 喜剧 动作 爱情 科幻 动画 悬疑 惊悚 恐怖 犯罪 同性 音乐 歌舞 传记 历史 战争 西部 奇幻 冒险 灾难 武侠 情色
        :param countries: 地区, 例如中国大陆 欧美 美国 中国香港 中国台湾 日本 韩国 英国 法国 德国 意大利 西班牙 印度 泰国 俄罗斯 伊朗 加拿大 澳大利亚 爱尔兰 瑞典 巴西 丹麦
        :param years_range: 电影上映的时间区间, 例如2010,2019
        '''
        url = self.movieQueryUrl.format(sortType=sortType,
                                        rateRange=rateRange,
                                        start=start,
                                        tags=tags,
                                        geners=geners,
                                        countries=countries,
                                        year_range=year_range)
        return await self.__crawl_proxy(url) if USE_PROXY else await self.__crawl(
            url)

    async def getMovieRawPage(self, id: str) -> str:
        '''
        根据豆瓣电影id获取所属页面html
        :param id: 豆瓣电影id
        '''
        url = self.moviePage.format(id=id)
        return await self.__crawl_proxy(url) if USE_PROXY else await self.__crawl(
            url)
