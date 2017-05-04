# -*- coding:utf-8 -*-

import urllib.request
import re
import  sys
import os
print(sys.getdefaultencoding())
num = 1
number = 1
fileurl = open('csdn_url.txt','w+')
fileurl.write("csdn资源url*************\n\n")

while num <2:
    url = 'http://download.csdn.net/user/eastmount/uploads/' + str(number)
    fileurl.write('下载URL:'+url+'\n')
    print(url.encode('utf-8'))
    requst = urllib.request.Request(url)
    content = urllib.request.urlopen(requst)
    htmlvalue = content.read()
    print(htmlvalue)
    open('csdn.html','w+').write(str(htmlvalue))

    value = str(htmlvalue)

    start = value.find(r'<div class="list-container mb-bg">')
    print('个数：%d',start)

    end = value.find(r'<div class="page_nav">')
    print('个数：%d', end)

    cutCount = value[start : end]
    print(cutCount)

    res_dt = r'<dt>(.*?)</dt>'
    m_dt = re.findall(res_dt,cutCount)
    print(m_dt.__sizeof__())

    for obj in m_dt:
        print('******************')
        num=num+1
        print('第'+str(num)+'资源')
        url_list = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')",obj)
        for url in url_list:
            print('url:'+str(url))

        res_title = r'<a href=.*>(.*?)</a>'
        title = re.findall(res_title,obj)
        for t in title:
            print(type(t))
           # t = t.encode('utf-8').decode('unicode_escape')
            t = t .encode('').decode('unicode_escape')
            print(t)



    num = num+1

