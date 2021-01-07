# 参数文件

# csv文件存储文件名
CSV_FILE_NAME = "douban_movies0.csv"

# 爬取影剧数据参数
START_RANGE = 3330  # 开始爬取偏移量
END_RANGE = 10000  # 结束爬取偏移, 开始与结束差值最好为20的整数倍
SORT_TYPE = "U"  # 数据的排序方式, U近期热门 T标记最多 S评分最高 R最新上映
RATE_RANGE = "0,10"  # 数据评分的区间, 默认0-10分
TAGS = "电影"  # 特色, 例如 经典 青春 文艺 搞笑 励志 魔幻等
GENERES = ""  # 类型, 例如 剧情 喜剧 动作 爱情 科幻 动画 悬疑 惊悚 恐怖 犯罪 同性 音乐 歌舞 传记 历史 战争 西部 奇幻 冒险 灾难 武侠 情色
COUNTRIES = ""  # 地区, 例如 中国大陆 欧美 美国 中国香港 中国台湾 日本 韩国 英国 法国 德国 意大利 西班牙 印度 泰国 俄罗斯 伊朗 加拿大 澳大利亚 爱尔兰 瑞典 巴西 丹麦
YEAR_RANGES = ""  # 上映的时间区间, 例如"2010,2019"

# 爬取间隔最短和最长时间, 随机取最短和最长之间的数, 单位s, 仅对非异步爬虫有效
SLEEP_MIN_TIME = 3
SLEEP_MAX_TIME = 20

# Cookies
COOKIES = ''

# 是否使用异步爬取, 启用时爬取速度快, 易被ban, 建议同时设置cookies, 但是也容易ban号hhhh
IS_ASYNC = False
# 是否使用代理
USE_PROXY = False
# 代理池的地址
PROXY_URL = "http://localhost:5555/random"

# 搜索引擎（SEO爬虫）的请求头
USER_AGENT = [
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)',
    'Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)',
    'DuckDuckBot/1.0; (+http://duckduckgo.com/duckduckbot.html)',
    'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)',
    'Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)',
    'ia_archiver (+http://www.alexa.com/site/help/webmasters; crawler@alexa.com)'
]
AGENT_SIZE = 7
