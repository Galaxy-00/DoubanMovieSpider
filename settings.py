# 参数文件

# csv文件存储文件名
CSV_FILE_NAME = "douban_movies0.csv"

# 爬取电影数据参数
START_RANGE = 820  # 开始爬取电影的偏移量
END_RANGE = 1000  # 结束爬取电影的偏移, 开始与结束差值最好为20的整数倍
SORT_TYPE = "U"  # 电影数据的排序方式, U近期热门 T标记最多 S评分最高 R最新上映
RATE_RANGE = "0,10"  # 电影数据评分的区间, 默认0-10分
TAGS = ""  # 电影特色, 例如 经典 青春 文艺 搞笑 励志 魔幻等
GENERES = ""  # 电影类型, 例如 剧情 喜剧 动作 爱情 科幻 动画 悬疑 惊悚 恐怖 犯罪 同性 音乐 歌舞 传记 历史 战争 西部 奇幻 冒险 灾难 武侠 情色
COUNTRIES = ""  # 地区, 例如 中国大陆 欧美 美国 中国香港 中国台湾 日本 韩国 英国 法国 德国 意大利 西班牙 印度 泰国 俄罗斯 伊朗 加拿大 澳大利亚 爱尔兰 瑞典 巴西 丹麦
YEAR_RANGES = ""  # 电影上映的时间区间, 例如"2010,2019"

# 爬取间隔时间, 单位s
SLEEP_TIME = 1

# 是否使用异步爬取, 速度快, 易被ban, 建议同时设置
IS_ASYNC = True

# 是否使用代理
USE_PROXY = False

# Cookies
COOKIES = ''

# Headers
HEADERS = {
    "Accept-Lanuage": "zh-CN,zh;q=0.9,en;q=0.8",
    "User-Agent":
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Referer": "https://www.douban.com/",
    # "Cookie": COOKIES
}
