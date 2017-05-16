import urllib.request
import  re
class QSBK:
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.header ={'User-Agent':self.user_agent}
        self.stories=[]
        self.enable = False
    def getPage(self,pageIndex):
        url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
        request = urllib.request.Request(url,headers=self.header)
        response = urllib.request.urlopen(request)
        pageCode = response.read().decode('UTF-8')
        return pageCode

    def getPageItem(self,pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print('页面加载失败')
            return None
        #<div.*?content">(.*?)</div>(.*?)<div class="stats.*?class="number">(.*?)</i>
        pattern = re.compile('<div class="author clearfix">.*?href.*?<img src.*?title=.*?<h2>(.*?)</h2>.*?<div.*?content">(.*?)</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
        items = re.findall(pattern,pageCode)
        pageStroies = []
        for item in items:
            replaceBR = re.compile('<.?span>')
            text = re.sub(replaceBR,"\n",item[1])
            pageStroies.append([item[0].strip(), text.strip(), item[2].strip()])

            print(pageStroies)
        return  pageStroies

    def loadPage(self):
        if self.enable == True:
            if len(self.stories)<2:
                pageStroies = self.getPageItem(self.pageIndex)
                if pageStroies:
                    self.stories.append(pageStroies)
                    self.pageIndex+=1

    def getOneStroy(self,pageStories,page):
        for story in pageStories:
            inputStr = input()
            self.loadPage()
            if inputStr =='Q':
                self.enable = False
                return
            print("第%d页\t发布人:%s\t内容：%s"%(page,story[0],story[1]))

    def start(self):
        print('正在读取糗事而百科段子。。。')
        self.enable =True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.stories)>0:
                pageStroies = self.stories[0]
                nowPage+=1
                del self.stories[0]
                self.getOneStroy(pageStroies,nowPage)


qs = QSBK()
qs.start()

