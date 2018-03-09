import requests
import re
#changepage用来产生不同页数的链接
def changepage(url,total_page):
    page_group = ['https://www.dygod.net/html/gndy/jddy/index.html']
    for i in range(2,total_page+1):
        link = re.sub('jddy/index','jddy/index_'+str(i),url,re.S)
        page_group.append(link)
    return page_group
#pagelink用来产生页面内的视频链接页面
def pagelink(url):
    base_url = 'https://www.dygod.net/html/gndy/jddy/'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
    req = requests.get(url , headers = headers)
    req.encoding = 'gbk'#指定编码，否则会乱码
    pat = re.compile('<a href="/html/gndy/jddy/(.*?)" class="ulink" title=(.*?)/a>',re.S)#获取电影列表网址
    reslist = re.findall(pat, req.text)
    finalurl = []
    for i in range(1,25):
        xurl = reslist[i][0]
        finalurl.append(base_url + xurl)
    return finalurl #返回该页面内所有的视频网页地址
#getdownurl获取页面的视频地址
def getdownurl(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
    req = requests.get(url , headers = headers)
    req.encoding = 'gbk'#指定编码，否则会乱码
    pat = re.compile('<a href="ftp(.*?)">ftp',re.S)#获取下载地址
    reslist = re.findall(pat, req.text)
    furl = 'ftp'+reslist[0]
    return furl
if __name__ == "__main__" :
    html = "https://www.dygod.net/html/gndy/jddy/index.html"
    print('你即将爬取的网站是：https://www.dygod.net/html/gndy/jddy/index.html')
    pages = input('请输入需要爬取的页数：')
    p1 = changepage(html,int(pages))
    with open ('电影天堂下载地址.lst','w') as f :
        j = 0
        for p1i in p1 :
            j = j + 1
            print('正在爬取第%d页,网址是 %s ...'%(j,p1i))
            p2 = pagelink(p1i)
            for p2i in p2 :
                p3 = getdownurl(p2i)
                if len(p3) == 0 :
                    pass
                else :
                    finalurl = p3
                    f.write(finalurl + '\n')
    print('所有页面地址爬取完毕!')