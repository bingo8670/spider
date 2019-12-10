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





