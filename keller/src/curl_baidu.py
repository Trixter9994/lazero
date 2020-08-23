import urllib.parse
import sys
def format_url(url, params: dict = None) -> str:
    query_str = urllib.parse.urlencode(params)
    return f'{ url }?{ query_str }'


def get_url(keyword):
    params = {
        'wd': str(keyword)
    }
    url = "https://www.baidu.com/s"
    url = format_url(url, params)
    # print(url)

    return url

for x in sys.stdin:
    print(get_url(x))
