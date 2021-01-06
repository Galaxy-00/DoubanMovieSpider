from Spider import DoubanSpider
from PageParser import MovieParser
from StoreHelper import CsvHelper
from constants import *
from time import sleep
import json


def main():
    douban_spider = DoubanSpider.DoubanSpider()  # 爬虫
    page_parser = MovieParser.MovieParser()  # 解析器
    csv_helper = CsvHelper.CsvHelper(CSV_FILE_NAME)  # 存储器

    count = START_RANGE  # 计数
    for start in range(START_RANGE, END_RANGE,
                       20):  # 从START_RANGE开始到END_RANGE以20为间隔爬取数据
        movies_data = json.loads(
            douban_spider.getMovieInfoByParams(sortType=SORT_TYPE,
                                               rateRange=RATE_RANGE,
                                               tags=TAGS,
                                               geners=GENERES,
                                               countries=COUNTRIES,
                                               year_range=YEAR_RANGES,
                                               start=start))['data']
        for single_movie in movies_data:  # 遍历这20个数据
            douban_id = single_movie['id']  # 获取对应电影的豆瓣id
            print('Num {}: start crawling movie id {}'.format(
                count, douban_id))
            html = douban_spider.getMoveRawPage(douban_id)  # 获取相应电影的页面
            page_parser.set_html(html, douban_id)  # 设置解析器
            movie = page_parser.parser_html()  # 进行解析数据
            csv_helper.write_row(movie.values())  # 存储到csv文件中
            count += 1
            sleep(SLEEP_TIME)  # sleep


if __name__ == '__main__':
    main()
