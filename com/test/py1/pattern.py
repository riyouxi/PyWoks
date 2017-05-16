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
        pattern = re.compile('<h2>.*?(.*?)</h2>(.*?)<div.*?content">(.*?)</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
        items = re.findall(pattern,pageCode)
        pageStroies = []
        for item in items:
            #print(item)
            havImg = re.search("img", item[2])
            if not havImg:
                repalceBR = re.compile('<br/>')
                text = re.sub(repalceBR, "\n", item[1])
                pageStroies.append([item[0].strip(), item[1].strip(), item[2].strip(), item[3].strip()])
                print(pageStroies)
        #return  pageStroies



qs = QSBK()
qs.getPageItem(1)
