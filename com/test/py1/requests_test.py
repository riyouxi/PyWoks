import re
import urllib.request
import gzip

import requests

#coding:utf-8
#http://blog.csdn.net/fly_yr/article/details/51570339

class csdnSpider:
    def __init__(self,pageIndex):
        self.pageIndex = pageIndex
        strUrl = "http://blog.csdn.net/fly_yr/article/list/1"
        self.url = strUrl[0:strUrl.rfind('/')+1]+str(pageIndex)
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
            ,'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
            ,'Accept-Encoding': 'gzip, deflate, sdch'
            ,'Accept-Language': 'zh-CN,zh;q=0.8'}

    def unzip(self,data):
        try:
            data = gzip.decompress(data)
        except:
            print('解压失败')
        return data


    def getContent(self):
        req = urllib.request.Request(self.url,headers=self.headers)
        response = urllib.request.urlopen(req)

        data = response.read()
        data = self.unzip(data)
        data = data.decode('utf-8')
        return data

    def getPage(self):
        content = self.getContent()
        page = r'<div.*?pagelist">.*?<span>.*?共(.*?)页</span>'
        patter = re.compile(page, re.S)
        pageNum = re.findall(patter, content)[0]
        return pageNum

    def readData(self):
        content = self.getContent()
        #
        #<span class="link_view".*?</a>.*?(.*?)</span>
        #<span class="link_postdate">(.*?)</span>
        compilestr = '<span .*?title"><a href=".*?(.*?)">.*?(.*?)</a></span>.*?<span .*?postdate">(.*?)</span>.*?<span class="link_view".*?</a>.*?(.*?)</span>'
        patter = re.compile(compilestr,re.S)
        items = re.findall(patter,content)

        for item in items:
            print(item)

csdn = csdnSpider(1)
csdn.readData()
