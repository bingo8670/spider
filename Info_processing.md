### 信息处理

#### 信息的标记

- 标记后的信息可形成信息组织结构，增加了信息维度；
- 标记后的信息可用于通信、存储或展示；
- 标记的结构与信息一样具有重要价值；
- 标记后的信息更利于程序理解和运用；

##### 信息标记的三种形式

- XML：eXtensible Markup Language，扩展标记语言
- JSON：JavaScript Object Notation，有类型的键值对  key:value
- YAML：YAML Ain't Markup Language，无类型键值对 key:value

------

#### 信息的提取

方法一：完整解析信息的标记形式，再提取关键信息；XML、JSON、YAML，需要标记解析器，例如：bs4库的标签树遍历；

- 优点：信息解析准确；
- 缺点：提取过程繁琐，速度慢；

方法二：无视标记形式，直接搜索关键信息；搜索，对信息的文本查找函数即可；

- 优点：提取过程简洁，速度较快；
- 缺点：提取结果准确性与信息内容相关

方法三：融合方法：结合形式解析和搜索方法，提取关键信息；XML、JSON、YAML、搜索，需要标记解析器及文本查找函数；

```python
for link in soup.find_all('a'):
    print(link.get('href'))
```

------

#### 基于bs4库的HTML内容查找方法

```python
for tag in soup.find_all(True):   # 标签为True，打印所有标签
    print(tag.name)
```

<>.find_all(name, attires, recursive, string, **kwargs)

返回一个列表类型，存储查找的结果；

Name：对标签名称的检索字符串；

attrs：对标签属性值对检索字符串，可标注属性检索；属性值必须精确；

Recursive：是否对子孙全部检索，默认True；

String：<>...</>中字符串区域的检索字符串；

------

#### 正则表达式库

```python
import re 
soup.find_all(id=re.compile('link'))
soup.find_all(string = re.compile("python")
for tag in soup.find_all(re.compile('b')):
    print(tag.name)
```

<tag>(..) 等价于 <tag>.find_all(..)

soup(..) 等价于 soup.find_all(..)



