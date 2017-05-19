import urllib.request


class Lottery:

    def __init__(self):
        self.url = 'http://www.sporttery.cn/specs/pjrqd.html'
        self.headers={'User-Agen':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
                        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                     'Referer':'http://www.sporttery.cn/',
                    'Accept-Encoding':	'gzip, deflate, sdch',
                    'Accept-Language':	'zh-CN,zh;q=0.8'}

    def getContent(self):
        req = urllib.request.Request(self.url,headers=self.headers)
        response = urllib.request.urlopen(req)
        content = response.read()
        print(content)



lott = Lottery()
lott.getContent()
