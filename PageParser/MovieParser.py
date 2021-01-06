from config import Entity
from pyquery import PyQuery as pq
import re


class MovieParser(object):
    def __init__(self) -> None:
        self.__movie_info = Entity.movie.copy()
        self.__html_doc = None
        self.__pq_doc = None

    def set_html(self, html: str, douban_id: str):
        '''
        设置解析器的html
        :param html: 豆瓣电影页面的html
        :param douban_id: 豆瓣电影对应的id
        '''
        self.__html_doc = html
        self.__pq_doc = pq(self.__html_doc)
        self.__movie_info['douban_id'] = douban_id
        
        return self

    def __get_title(self) -> None:
        try:
            self.__movie_info['title'] = self.__pq_doc.find(
                'span[property="v:itemreviewed"]').text()
        except:
            pass

    def __get_year(self) -> None:
        try:
            res = self.__pq_doc.find('.year').text()
            self.__movie_info['year'] = re.search(r'\((.*)\)', res).group(1)
        except:
            pass

    def __get_directors(self) -> None:
        try:
            self.__movie_info['directors'] = self.__pq_doc.find(
                'a[rel="v:directedBy"]').text().replace(' ', ' / ')
        except:
            pass

    def __get_script_writers(self) -> None:
        try:
            res = re.search(
                r"<span.*<span class='pl'>编剧</span>[\s\S]*?</span>",
                self.__html_doc).group(0)
            self.__movie_info['scriptwriters'] = pq(res).find('.attrs').text()
        except:
            pass

    def __get_actors(self) -> None:
        try:
            self.__movie_info['actors'] = self.__pq_doc.find(
                '.actor .attrs').text()
        except:
            pass

    def __get_types(self) -> None:
        try:
            self.__movie_info['types'] = self.__pq_doc.find(
                'span[property="v:genre"]').text().replace(' ', ' / ')
        except:
            pass

    def __get_release_region(self) -> None:
        try:
            res = re.search(r'<span class="pl">制片国家/地区:</span> (.*)<br/>',
                            self.__html_doc).group(1)
            self.__movie_info['release_region'] = res
        except:
            pass

    def __get_languages(self) -> None:
        try:
            res = re.search(r'<span class="pl">语言:</span> (.*)<br/>',
                            self.__html_doc).group(1)
            self.__movie_info['languages'] = res
        except:
            pass

    def __get_release_date(self) -> None:
        try:
            self.__movie_info['release_date'] = self.__pq_doc.find(
                'span[property="v:initialReleaseDate"]').text()
        except:
            pass

    def __get_rate(self) -> None:
        try:
            self.__movie_info['rate'] = self.__pq_doc.find(
                'strong[property="v:average"]').text()
        except:
            pass

    def __get_rate_num(self) -> None:
        try:
            self.__movie_info['rate_num'] = self.__pq_doc.find(
                'span[property="v:votes"]').text()
        except:
            pass

    def __get_star_pre(self) -> None:
        try:
            items = self.__pq_doc.find('.ratings-on-weight').children().items()
            star = 5
            for i in items:
                self.__movie_info["{}star".format(star)] = i.find(
                    '.rating_per').text()
                star -= 1
        except:
            pass

    def __get_short_comment_num(self) -> None:
        try:
            res = self.__pq_doc.find('.mod-hd .pl').text()
            self.__movie_info['shortCommentNum'] = re.search(r'([0-9]+)',
                                                             res).group(0)
        except:
            pass

    def __get_show_comment_num(self) -> None:
        try:
            res = self.__pq_doc.find('#reviews-wrapper .pl').text()
            self.__movie_info['showCommentNum'] = re.search(r'([0-9]+)',
                                                            res).group(0)
        except:
            pass

    def parser_html(self) -> dict:
        '''
        解析电影页面的html, 并返回对应的数据, 格式dict
        '''
        self.__get_title()
        self.__get_year()
        self.__get_directors()
        self.__get_script_writers()
        self.__get_actors()
        self.__get_types()
        self.__get_release_region()
        self.__get_languages()
        self.__get_release_date()
        self.__get_rate()
        self.__get_rate_num()
        self.__get_star_pre()
        self.__get_short_comment_num()
        self.__get_show_comment_num()

        return self.__movie_info
