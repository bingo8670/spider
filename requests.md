```python
>>> import requests
>>> r = requests.get("http://www.baidu.com")
>>> r.status_code
200
>>> r.encoding = 'utf-8'
>>> r.text
```



Requests库的7个主要方法

| 方法               | 说明                                             |
| ------------------ | ------------------------------------------------ |
| requests.request() | 构造一个请求，支撑以下各方法的基础方法           |
| requests.get()     | 获取HTML网页的主要方法，对应于HTTP的GET          |
| requests.head()    | 获取HTML网页头信息的方法，对应于HTTP的HEAD       |
| requests.post()    | 向HTML网页提交POST请求的方法，对应于HTTP的POST   |
| requests.put()     | 向HTML网页提交PUT请求的方法，对应于HTTP的PUT     |
| requests.patch()   | 向HTML网页提交局部修改请求，对应于HTTP的PATCH    |
| requests.delete()  | 向HTML网页提交删除请求的方法，对应于HTTP的DELETE |

HTTP协议

- Hypertext Transfer Protocol，超文本传输协议；
- 是一个基于“请求与响应”模式的、无状态的应用层协议；
- 采用URL作为定位网络资源的标识。 http://host[:port]/[path]

Requests库的2个重要对象：Response && Request

r = requests(method, url,  **kwargs) 

**kwargs：控制访问的参数，均为可选项

params, data, json, headers, cookies, auth, files, timeout, proxies, allow_redirects, stream, verify, cert

Response：Response对象包含爬虫返回的内容；

| 属性                | 说明                                             |
| ------------------- | ------------------------------------------------ |
| r.status_code       | HTTP请求的返回状态，200表示连接成功，404表示失败 |
| r.text              | HTTP相应内容的字符串形式，即URL对应的页面内容    |
| r.encoding          | 从HTTP header中猜测的响应内容编码方式            |
| r.apparent_encoding | 从内容中分析出的响应内容编码方式(备选编码方式)   |
| r.content           | HTTP响应内容的二进制形式                         |

Request：requests库创建的对象；

------

爬取网页的通用代码框架

```python
import requests
def getHTMLText(url):
		try:
				r = requests.get(url, timeout=30)
				r.raise_for_status() #如果状态不是200，引发HTTPError异常
				r.encoding = r.apparent_encoding
				return r.text
		except:
				return "产生异常"
				
if __name__ == "__main__":
		url = "http://www.baidu.com"
		print(getHTMLText(url))
```

