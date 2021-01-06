from Spider import DoubanSpider
from PageParser import MovieParser
from StoreHelper import CsvHelper
from constants import *
from time import sleep
import json


def main():
    douban_spider = DoubanSpider.DoubanSpider()
    page_parser = MovieParser.MovieParser()
    csv_helper = CsvHelper.CsvHelper(CSV_FILE_NAME)

    for start in range(START_RANGE, END_RANGE, 20):
        movies_data = json.loads(
            douban_spider.getMovieInfoByParams(sortType=SORT_TYPE,
                                               rateRange=RATE_RANGE,
                                               tags=TAGS,
                                               geners=GENERES,
                                               countries=COUNTRIES,
                                               year_range=YEAR_RANGES,
                                               start=start))['data']
        for single_movie in movies_data:
            douban_id = single_movie['id']
            html = douban_spider.getMoveRawPage(douban_id)
            page_parser.set_html(html, douban_id)
            movie = page_parser.parser_html()
            csv_helper.write_row(movie.values())
            sleep(SLEEP_TIME)


if __name__ == '__main__':
    main()
