import requests
from retrying import retry


class DoubanSpider(object):
    def __init__(self) -> None:
        self.headers = {
            "Accept-Lanuage":
            "zh-CN,zh;q=0.9,en;q=0.8",
            "User-Agent":
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        }
        self.movieQueryUrl = "https://movie.douban.com/j/new_search_subjects?sort={sortType}&range={rateRange}&tags={tags}&start={start}&genres={geners}&countries={countries}&year_range={year_range}"
        self.moviePage = "https://movie.douban.com/subject/{id}/"

    @retry(stop_max_attempt_number=3,
           wait_random_min=600,
           wait_random_max=1500)
    def __crawl(self, url: str) -> str:
        '''
        爬取url页面, 返回获取的内容
        :param url: url
        '''
        data = requests.get(url, headers=self.headers).text
        return data

    def getMovieInfoByParams(self,
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
        data = self.__crawl(
            self.movieQueryUrl.format(sortType=sortType,
                                      rateRange=rateRange,
                                      start=start,
                                      tags=tags,
                                      geners=geners,
                                      countries=countries,
                                      year_range=year_range))
        return data

    def getMoveRawPage(self, id: str) -> str:
        '''
        根据豆瓣电影id获取所属页面html
        :param id: 豆瓣电影id
        '''
        return self.__crawl(self.moviePage.format(id=id))
