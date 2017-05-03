import  urllib.request,re,os,sys

def save_info(data):
    path = "E:\\PyWoks\\02_douban.out"
    f = open(path,'wb')
    f.write(data)
    f.close()

def save_image_info(path):
    targetPath = "E:\\PyWoks\\03_images"
    if not os.path.isdir(targetPath):
        os.mkdir(targetPath)
    pos = path.rindex('/')
    t = os.path.join(targetPath,path[pos+1:])
    return t



url = "http://www.douban.com/"
headers = {
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '                            'Chrome/51.0.2704.63 Safari/537.36'
           }
request = urllib.request.Request(url=url,headers =headers)
response = urllib.request.urlopen(request)
data = response.read()
print(data)
for link,t in set(re.findall(r'(https:[^s]*?(jpg|png|gif))', str(data))):
    print(link)
    try:
        urllib.request.urlretrieve(link,save_image_info(link))
    except:
        print("失败")
save_info(data)
data = data.decode('utf-8')


print(type(response))
print(response.geturl())
print(response.info())
print(response.getcode())
