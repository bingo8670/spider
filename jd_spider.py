# -*- coding:utf-8 -*-
#！python3
import requests
url = "https://item.jd.com/100000287145.html"
try:
    r =requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败")
