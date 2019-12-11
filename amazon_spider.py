import requests
url = "https://www.amazon.cn/dp/B0798J3G37/ref=sr_1_1?qid=1576050433&s=digital-text&sr=1-1&text=%E8%96%9B%E5%85%86%E4%B8%B0"
try:
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url, headers= kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print("爬取失败")

