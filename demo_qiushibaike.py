# /usr/bin/python
# -*- coding:utf-8 -*-

import re
import urllib
import urllib2

page = 1
url = 'https://www.qiushibaike.com/hot/page/1' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent':user_agent}
try:
    request = urllib2.Request(url, headers= headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile(
        '<div. *?author clearfix">.*?<a. *?<img. *?>(.*?)</a>.*?<div. *?' +
        'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>', re.S)
    items = re.findall(pattern, content)
    print 'items:'
    print items
    for item in items:
        print item[0], item[1], item[2], item[3], item[4]
except urllib2.URLError, e:
    if hasattr(e, 'code'):
        print e.code
    if hasattr(e, 'reason'):
        print e.reason


