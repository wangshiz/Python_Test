"""
第一个爬虫
"""
from urllib import request


def fun():
    # 如果不加上下面的这行出现会出现urllib2.HTTPError: HTTP Error 403: Forbidden错误
    # 主要是由于该网站禁止爬虫导致的，可以在请求加上头信息，伪装成浏览器访问User-Agent,具体的信息可以通过火狐的FireBug插件查询
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    chaper_url = "http://www.d21b.com/cn/vl_bestrated.php"
    data = None
    req = request.Request(url=chaper_url, data=data, headers=headers, method="GET")
    content = str(request.urlopen(req).read(), "utf-8")

    def inner():
        return content
    return inner


fn = fun()
content = fn()
print(content)