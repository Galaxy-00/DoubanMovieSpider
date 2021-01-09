import asyncio
import json
from json.decoder import JSONDecodeError
from random import uniform
from time import sleep

from requests import TooManyRedirects

from PageParser import MovieParser
from settings import *
from Spider import AsyncDoubanSpider, DoubanSpider, Spider
from StoreHelper import CsvHelper


def linear_crawl(douban_spider: Spider.Spider,
                 page_parser: MovieParser.MovieParser,
                 store_helper: CsvHelper.CsvHelper):
    '''
    线性爬取
    :param douban_spider: 爬虫
    :param page_parser: 页面解析器
    :param store_helper: 存储器
    '''
    try:
        count = START_RANGE  # 计数
        for start in range(START_RANGE, END_RANGE,
                           20):  # 从START_RANGE开始到END_RANGE以20为间隔爬取数据
            print('Crawling Movie Start: {}'.format(start))
            res = douban_spider.getMovieInfoByParams(sortType=SORT_TYPE,
                                                     rateRange=RATE_RANGE,
                                                     tags=TAGS,
                                                     geners=GENERES,
                                                     countries=COUNTRIES,
                                                     year_range=YEAR_RANGES,
                                                     start=start)
            try:
                movies_data = json.loads(res)['data']
                for single_movie in movies_data:  # 遍历这20个数据
                    douban_id = single_movie['id']  # 获取对应影剧的豆瓣id
                    print('Num {}: crawling movie id: {}'.format(
                        count, douban_id))
                    html = douban_spider.getMovieRawPage(
                        douban_id)  # 获取相应影剧的页面
                    movie_dict = page_parser.set_html(
                        html, douban_id).parser_html()  # 设置解析器并解析
                    store_helper.write_row(movie_dict.values())  # 存储到csv文件中
                    count += 1
                    sleep(uniform(SLEEP_MIN_TIME, SLEEP_MAX_TIME))  # sleep
            except (JSONDecodeError, KeyError) as e:
                print('Error: 豆瓣返回数据{}'.format(res))
                return
    except TooManyRedirects as e:
        print('Error: {}\n重定向过多, 请更新账号Cookie'.format(e))


async def async_crawl(asy_douban_spider: Spider.Spider,
                      page_parser: MovieParser.MovieParser,
                      store_helper: CsvHelper.CsvHelper, start: int):
    '''
    异步爬取
    :param asy_douban_spider: 异步爬虫
    :param page_parser: 页面解析器
    :param store_helper: 存储器
    :param start: 起始数据偏移
    '''
    try:
        print('Crawling Movie Start: {}'.format(start))
        res = await asy_douban_spider.getMovieInfoByParams(
            sortType=SORT_TYPE,
            rateRange=RATE_RANGE,
            tags=TAGS,
            geners=GENERES,
            countries=COUNTRIES,
            year_range=YEAR_RANGES,
            start=start)
        try:
            movies_data = json.loads(res)['data']
            for single_movie in movies_data:  # 遍历这20个数据
                douban_id = single_movie['id']  # 获取对应影剧的豆瓣id
                print('Crawling movie id: {}'.format(douban_id))
                html = await asy_douban_spider.getMovieRawPage(douban_id
                                                               )  # 获取相应影剧的页面
                movie_dict = page_parser.set_html(
                    html, douban_id).parser_html()  # 设置解析器并解析
                store_helper.write_row(movie_dict.values())  # 存储到csv文件中
        except (JSONDecodeError, KeyError) as e:
            print('Error: 豆瓣返回数据:{}'.format(res))
            return
    except TooManyRedirects as e:
        print('Error: {}\n重定向过多, 请更新账号Cookie'.format(e))


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
                async_crawl(asy_douban_spider, page_parser, csv_helper,
                            start))  # for循环在函数外
            for start in range(START_RANGE, END_RANGE, 20)
        ]
        loop.run_until_complete(asyncio.wait(tasks))


if __name__ == '__main__':
    main()
