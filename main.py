from json.decoder import JSONDecodeError
from Spider import DoubanSpider
from Spider import AsyncDoubanSpider
from PageParser import MovieParser
from StoreHelper import CsvHelper
from settings import *
from time import sleep
import json
import asyncio


def linear_crawl(douban_spider: DoubanSpider, page_parser: MovieParser,
                 store_helper: CsvHelper):
    try:
        count = START_RANGE  # 计数
        for start in range(START_RANGE, END_RANGE,
                           20):  # 从START_RANGE开始到END_RANGE以20为间隔爬取数据
            res = douban_spider.getMovieInfoByParams(sortType=SORT_TYPE,
                                                     rateRange=RATE_RANGE,
                                                     tags=TAGS,
                                                     geners=GENERES,
                                                     countries=COUNTRIES,
                                                     year_range=YEAR_RANGES,
                                                     start=start)
            # print(res)
            movies_data = json.loads(res)['data']
            for single_movie in movies_data:  # 遍历这20个数据
                douban_id = single_movie['id']  # 获取对应影剧的豆瓣id
                print('Num {}: crawling movie id: {}'.format(
                    count, douban_id))
                html = douban_spider.getMovieRawPage(douban_id)  # 获取相应影剧的页面
                movie_dict = page_parser.set_html(
                    html, douban_id).parser_html()  # 设置解析器并解析
                store_helper.write_row(movie_dict.values())  # 存储到csv文件中
                count += 1
                sleep(SLEEP_TIME)  # sleep
    except JSONDecodeError:
        print('Error: Json解析错误, 可能是豆瓣暂时ban了ip, 请设置COOKIES')


async def async_crawl(asy_douban_spider: AsyncDoubanSpider,
                      page_parser: MovieParser, store_helper: CsvHelper,
                      start: int):
    try:
        movies_data = json.loads(await asy_douban_spider.getMovieInfoByParams(
            sortType=SORT_TYPE,
            rateRange=RATE_RANGE,
            tags=TAGS,
            geners=GENERES,
            countries=COUNTRIES,
            year_range=YEAR_RANGES,
            start=start))['data']

        for single_movie in movies_data:  # 遍历这20个数据
            douban_id = single_movie['id']  # 获取对应影剧的豆瓣id
            print('crawling movie id: {}'.format(douban_id))
            html = await asy_douban_spider.getMovieRawPage(douban_id
                                                           )  # 获取相应影剧的页面
            movie_dict = page_parser.set_html(
                html, douban_id).parser_html()  # 设置解析器并解析
            store_helper.write_row(movie_dict.values())  # 存储到csv文件中
    except JSONDecodeError:
        print('Error: Json解析错误, 可能是豆瓣暂时ban了ip, 请设置COOKIES')


def main():
    page_parser = MovieParser.MovieParser()  # 解析器
    csv_helper = CsvHelper.CsvHelper(CSV_FILE_NAME)  # 存储器
    douban_spider = DoubanSpider.DoubanSpider()  # 爬虫
    asy_douban_spider = AsyncDoubanSpider.AsyncDoubanSpider()  # 异步爬虫

    if not IS_ASYNC:
        # 非异步爬取
        linear_crawl(douban_spider, page_parser, csv_helper)
    else:
        # 异步爬取
        loop = asyncio.get_event_loop()
        tasks = [
            loop.create_task(
                async_crawl(asy_douban_spider, page_parser, csv_helper, start)) # for循环在函数外
            for start in range(START_RANGE, END_RANGE, 20)
        ]
        loop.run_until_complete(asyncio.wait(tasks))


if __name__ == '__main__':
    main()
