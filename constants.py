# 参数文件

# csv文件存储文件名
CSV_FILE_NAME = "douban_movies0.csv"

# 爬取电影数据参数
START_RANGE = 0  # 开始爬取电影的偏移量
END_RANGE = 20  # 结束爬取电影的偏移, 开始与结束差值最好为20的整数倍
SORT_TYPE = "U"  # 电影数据的排序方式, U近期热门 T标记最多 S评分最高 R最新上映
RATE_RANGE = "0,10"  # 电影数据评分的区间, 默认0-10分
TAGS = ""  # 电影特色, 例如 经典 青春 文艺 搞笑 励志 魔幻等
GENERES = ""  # 电影类型, 例如 剧情 喜剧 动作 爱情 科幻 动画 悬疑 惊悚 恐怖 犯罪 同性 音乐 歌舞 传记 历史 战争 西部 奇幻 冒险 灾难 武侠 情色
COUNTRIES = ""  # 地区, 例如 中国大陆 欧美 美国 中国香港 中国台湾 日本 韩国 英国 法国 德国 意大利 西班牙 印度 泰国 俄罗斯 伊朗 加拿大 澳大利亚 爱尔兰 瑞典 巴西 丹麦
YEAR_RANGES = ""  # 电影上映的时间区间, 例如"2010,2019"

# 爬取间隔时间, 单位s
SLEEP_TIME = 1

# 是否使用异步爬取
IS_ASYNC = True

# 是否使用代理
USE_PROXY = False

# Cookies
COOKIES = 'bid=W97JzV_kst8; douban-fav-remind=1; ll="118371"; _vwo_uuid_v2=D8ECA37DE57FEB48EF9B9D2C15CD72420|2095a6ccc7ec36a819ded52cf4ac3153; _ga=GA1.2.1440352438.1598784356; __utma=30149280.1440352438.1598784356.1609937385.1609945715.11; __utmz=30149280.1609945715.11.7.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; dbcl2="97949738:Y1802AsV/e8"; push_noty_num=0; push_doumail_num=0; __utmv=30149280.9794; douban-profile-remind=1; __utmb=30149280.15.10.1609945715; __utma=223695111.1833664814.1598879488.1609937322.1609947313.9; __utmb=223695111.0.10.1609947313; __utmz=223695111.1609947313.9.5.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/97949738/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1609947313%2C%22https%3A%2F%2Fwww.douban.com%2Fpeople%2F97949738%2F%22%5D; _pk_ses.100001.4cf6=*; _pk_id.100001.4cf6=d073e9d00bfd1884.1598879488.9.1609948996.1609937397.; ck=pzKo'

# Headers
HEADERS = {
    "Accept-Lanuage": "zh-CN,zh;q=0.9,en;q=0.8",
    "User-Agent":
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Referer": "https://www.douban.com/",
    "Cookie": COOKIES
}
