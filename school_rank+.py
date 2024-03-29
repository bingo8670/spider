# chr(12288) 是中文空格，解决中文对齐问题；
# 格式对齐问题还是没有解决；
import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "爬取失败"

def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string])


def printUnivList(ulist, num):
    # {:^10} 表示中间对齐 (宽度为10)
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}\t{3:^10}"
    # print(tplt.format("排名", "学校名称", "省市", "评分", chr(12288)))
    print("排名", "学校名称", "省市", "评分", chr(12288))
    for i in range(num):
        u = ulist[i]
        # print(tplt.format(u[0], u[1], u[2], u[3], chr(12288)))
        print(u[0], u[1], u[2], u[3], chr(12288))

def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)   # 20 univs

main()
